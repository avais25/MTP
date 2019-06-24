#include "fblib/firebird.h"
#include "cor_c/cor.h"
unsigned long micros();


unsigned long int timer0_overflow_count=0;


void inputDriver(int *blocked,int *leftOut,int *rightOut,int *centreOut) {
  unsigned char Left_white_line = ADC_Conversion(3);	//Getting data of Left WL Sensor
  unsigned char Center_white_line = ADC_Conversion(2);	//Getting data of Center WL Sensor
  unsigned char Right_white_line = ADC_Conversion(1);	//Getting data of Right WL Sensor

  unsigned char Front_Sharp_Sensor = ADC_Conversion(11);


//debugging puropse
//   print_sensor(2,1,3);	//Prints value of White Line Sensor1
//   print_sensor(2,5,2);	//Prints Value of White Line Sensor2
//   print_sensor(2,9,1);	//Prints Value of White Line Sensor3


  if (Front_Sharp_Sensor > 150)
  *blocked=1;
  else
  *blocked=0;


  if(Left_white_line>0x40)
  *leftOut=1;
  else
  *leftOut=0;

  if(Right_white_line>0x40)
  *rightOut=1;
  else
  *rightOut=0;

  if(Center_white_line>0x40)
  *centreOut=1;
  else
  *centreOut=0;


}

int getSpeed(int s)
{
  switch (s) {
    case 0:
    return 0;
    case 1:
    return 50;
    case 2:
    return 130;
    case 3:
    return 150;
    default:
    return 0;
  }
}


void outputDriver(Cor__acc_out *out) {
    int left=getSpeed(0);
    int right=getSpeed(0);

    // lcd_print(2, 1, left, 3);

    // lcd_print(2, 5, right, 3);


    forward();

    velocity(left, right);
}


int main(int argc, char  *argv[]) {

// // Cor__acc_out out;
// Cor__lw_out lwOut;
// Cor__rw_out rwOut;



init_devices();
TCCR0A = 0;

// TCCR0B = (1 << CS00);    //version micro second
TCCR0B = (1 << CS00) | (1 << CS01) ; //version millisec
TIMSK0 = (1 << TOIE0);

  while (1) {

      int blocked, leftOut, rightOut, centreOut;
    unsigned long long int a,b,c;

    Cor__acc_out acc,out;

    a=micros();

    
    // inputDriver(&blocked,&leftOut,&rightOut,&centreOut);

    Cor__acc_step(blocked,leftOut,rightOut,centreOut, &out);
    // outputDriver(&acc);
    // _delay_ms(200);
    b=micros();
    c=(b-a)/1000;
    lcd_print(1, 1, c, 5);


  }

  return 0;
}

ISR(TIMER0_OVF_vect)
{

    timer0_overflow_count++;
}


unsigned long micros()
{
    unsigned long m;
    unsigned char cnt;
    cli();
    cnt= TCNT0;
    m = (cnt + (timer0_overflow_count * 256))*4.34;
    sei();
    return m;
}
