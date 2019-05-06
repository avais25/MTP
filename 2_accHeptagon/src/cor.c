/* --- Generated the 7/10/2018 at 5:56 --- */
/* --- heptagon compiler, version 1.05.00 (compiled sat. oct. 6 4:33:59 CET 2018) --- */
/* --- Command line: /home/avais/.opam/system/bin/heptc -target c -s acc-hepts cor.ept --- */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "cor.h"

void Cor__acc_step(int blocked, Cor__acc_out* _out) {
  
  int v_1;
  int v;
  v_1 = (blocked==1);
  if (v_1) {
    _out->wlf = 0;
  } else {
    _out->wlf = 1;
  };
  v = (blocked==1);
  if (v) {
    _out->stop = 1;
  } else {
    _out->stop = 0;
  };;
}

