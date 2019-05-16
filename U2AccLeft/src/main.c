#include "fblib/firebird.h"
#include "cor_c/cor.h"
#include "drivers.h"


int main(int argc, char  *argv[]) {

// Cor__acc_out out;
Cor__lw_out lwOut;
Cor__rw_out rwOut;


init_devices();

  while (1) {

      int blocked, leftOut, rightOut, centreOut;
      int blocked2, leftOut2, rightOut2, centreOut2;

      // lwActuator(&lwOut);
      // rwActuator(&rwOut);

      fwActuator(&lwOut,&rwOut);

      inputDriver(&blocked,&leftOut,&rightOut,&centreOut);
      inputDriver2(blocked,leftOut,rightOut,centreOut,&blocked2,&leftOut2,&rightOut2,&centreOut2);

      Cor__lw_step( blocked,  leftOut,  rightOut,  centreOut, &lwOut) ;
      Cor__rw_step( blocked2,  leftOut2,  rightOut2,  centreOut2, &rwOut);


  }

  return 0;
}
