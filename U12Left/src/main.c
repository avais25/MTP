#include "fblib/firebird.h"
#include "rightO_c/rightO.h"



void inputDriver2(float *,float *);
void actDriver2();
RightO__rightO_out _out;
int main(int argc, char  *argv[]) {



float rf,rb;
init_devices();

  while (1) {


       inputDriver2(&rf,&rb);

    RightO__rightO_step(rf, rb, &_out);

      actDriver2();
  }

  return 0;
}



void inputDriver2(float *rightF,float *rightB) {

  *rightF = ADC_Conversion(7);
print_sensor(1,8,7);
  
  *rightB = ADC_Conversion(8);
print_sensor(2,8,8);
}


void actDriver2() {
    if(_out.rightBlocked == 0)
    {
    buzzer_on();
    // _delay_ms(1000); //delay
    print_sensor(2,1,123);
    buzzer_off();
    }
}

