#include "fblib/firebird.h"
#include "cor_c/cor.h"



void inputDriver(int *blocked,int *leftOut,int *rightOut,int *centreOut);
void outputDriver(Cor__acc_out *);
int getSpeed(int);

int main(int argc, char  *argv[]) {

Cor__acc_out out;

init_devices();

  while (1) {


      int blocked, leftOut, rightOut, centreOut;

      inputDriver(&blocked,&leftOut,&rightOut,&centreOut);

      Cor__acc_step(blocked,leftOut,rightOut,centreOut, &out);
      //lcd_print(2, 1, centreOut, 3);
      outputDriver(&out);


  }


  return 0;
}



void inputDriver(int *blocked,int *leftOut,int *rightOut,int *centreOut) {
  unsigned char Left_white_line = ADC_Conversion(3);	//Getting data of Left WL Sensor
  unsigned char Center_white_line = ADC_Conversion(2);	//Getting data of Center WL Sensor
  unsigned char Right_white_line = ADC_Conversion(1);	//Getting data of Right WL Sensor

  unsigned char Front_Sharp_Sensor = ADC_Conversion(11);
  //unsigned char Front_IR_Sensor = ADC_Conversion(6);

//  print_sensor(2,4,11);	//Prints Value of Front Sharp Sensor
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


void outputDriver(Cor__acc_out *out) {
    int left=getSpeed(out->wheelLeft);
    int right=getSpeed(out->wheelRight);

    lcd_print(2, 1, left, 3);

    lcd_print(2, 5, right, 3);


    forward();

    velocity(left, right);
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
