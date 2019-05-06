#include "cor.h"
#include "fblib/firebird.h"

int main(int argc, char  *argv[]) {

Cor__acc_out out;

Cor__acc_mem mem;

init_devices();

  while (1) {

    // int blocked=is_front_blocked();

    Cor__acc_step(&out,&mem);

   (out.wlf==1) ? white_line_follow() : 0;

   (out.stop==1) ? stop() : 0 ;

  }


  return 0;
}
