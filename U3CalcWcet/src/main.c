#define F_CPU 14745600
#include <time.h>
#include "fblib/firebird.h"
#include "cor_c/cor.h"
void inputDriver(int *blocked,int *leftOut,int *rightOut,int *centreOut);
unsigned long micros();

unsigned long timer0_micros=0;
unsigned long timer0_fract=0;

int main(int argc, char  *argv[]) {

Cor__acc_out out;

  init_devices();
  TCCR0A = 0;
  TCCR0B = (1 << CS00);
  TIMSK0 = (1 << TOIE0);



  while (1) {
    unsigned long a,b,c;

    a=micros();
    _delay_ms (1000);
    b=micros();
    c=(b-a)%1000;
    lcd_print(1, 1, c, 5);

  }
  return 0;
}

SIGNAL(TIMER0_OVF_vect)
{
    unsigned long m = timer0_micros;
    unsigned long f = timer0_fract;
 
    m += 17;
    f += 3612;
    if (f >= 10000) {
        f -= 10000;
        m += 1;
    }
    timer0_fract = f;
    timer0_micros = m;
}

    
unsigned long micros()
{
    unsigned long m;
    cli();
    m = timer0_micros;
    sei();
    return m;
}

void inputDriver(int *blocked,int *leftOut,int *rightOut,int *centreOut) {

  unsigned char Left_white_line = ADC_Conversion(3);	//Getting data of Left WL Sensor
  unsigned char Center_white_line = ADC_Conversion(2);	//Getting data of Center WL Sensor
  unsigned char Right_white_line = ADC_Conversion(1);	//Getting data of Right WL Sensor

  unsigned char Front_Sharp_Sensor = ADC_Conversion(11);
  _delay_ms (1000);

  // cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;

  lcd_print(2, 1, F_CPU/1000, 5);

  //unsigned char Front_IR_Sensor = ADC_Conversion(6);

  //print_sensor(2,4,11);	//Prints Value of Front Sharp Sensor
  //print_sensor(2,8,6);	//Prints Value of Front IR Sensor

  print_sensor(1,1,3);	//Prints value of White Line Sensor1
  print_sensor(1,5,2);	//Prints Value of White Line Sensor2
  print_sensor(1,9,1);	//Prints Value of White Line Sensor3


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
