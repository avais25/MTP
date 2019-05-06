/* --- Generated the 6/10/2018 at 9:40 --- */
/* --- heptagon compiler, version 1.05.00 (compiled sat. oct. 6 4:33:59 CET 2018) --- */
/* --- Command line: /home/avais/.opam/system/bin/heptc -target c -s acc -hepts cor.ept --- */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "cor.h"

void Cor__acc_reset(Cor__acc_mem* self) {
  Fblib__blocked_reset(&self->blocked_1);
  Fblib__blocked_reset(&self->blocked);
}

void Cor__acc_step(Cor__acc_out* _out, Cor__acc_mem* self) {
  Fblib__blocked_out Fblib__blocked_out_st;
  
  int v_3;
  int v_2;
  int v_1;
  int v;
  Fblib__blocked_step(&Fblib__blocked_out_st, &self->blocked_1);
  v_2 = Fblib__blocked_out_st.o;
  v_3 = (v_2==1);
  if (v_3) {
    _out->wlf = 0;
  } else {
    _out->wlf = 1;
  };
  Fblib__blocked_step(&Fblib__blocked_out_st, &self->blocked);
  v = Fblib__blocked_out_st.o;
  v_1 = (v==1);
  if (v_1) {
    _out->stop = 1;
  } else {
    _out->stop = 0;
  };;
}

