void inputDriver(int *blocked,int *leftOut,int *rightOut,int *centreOut);
void inputDriver2(int blocked,int leftOut,int rightOut,int centreOut,int *blocked2,int *leftOut2,int *rightOut2,int *centreOut2);
void outputDriver(Cor__lw_out *, Cor__rw_out *);
void lwActuator(Cor__lw_out *);
void rwActuator(Cor__rw_out *);
int getSpeed(int);
void fwActuator(Cor__lw_out *,Cor__rw_out *);



void inputDriver(int *blocked,int *leftOut,int *rightOut,int *centreOut) {
  unsigned char Left_white_line = ADC_Conversion(3);	//Getting data of Left WL Sensor
  unsigned char Center_white_line = ADC_Conversion(2);	//Getting data of Center WL Sensor
  unsigned char Right_white_line = ADC_Conversion(1);	//Getting data of Right WL Sensor

  unsigned char Front_Sharp_Sensor = ADC_Conversion(11);
  //unsigned char Front_IR_Sensor = ADC_Conversion(6);

  //print_sensor(2,4,11);	//Prints Value of Front Sharp Sensor
  //print_sensor(2,8,6);	//Prints Value of Front IR Sensor

//debugging puropse
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


void inputDriver2(int blocked,int leftOut,int rightOut,int centreOut,int *blocked2,int *leftOut2,int *rightOut2,int *centreOut2) {
  *blocked2=blocked;
  *leftOut2=leftOut;
  *rightOut2=rightOut;
  *centreOut2=centreOut;
}



// void lwActuator(Cor__lw_out *lwOut) {
//     left=getSpeed(lwOut->wheelLeft);
    
// }

// void rwActuator(Cor__rw_out *rwOut) {
//     right=getSpeed(rwOut->wheelRight);

// }

void fwActuator(Cor__lw_out *lwOut,Cor__rw_out *rwOut)
{
  int left,right;
  left=getSpeed(lwOut->wheelLeft);
  right=getSpeed(rwOut->wheelRight);
  velocity(left, right);
  forward();
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
