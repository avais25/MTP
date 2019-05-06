/* --- Generated the 29/3/2019 at 2:26 --- */
/* --- heptagon compiler, version 1.05.00 (compiled sat. oct. 6 4:33:59 CET 2018) --- */
/* --- Command line: /home/avais/.opam/system/bin/heptc -target c cor.ept --- */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "cor.h"

void Cor__acc_step(int blocked, int leftOut, int rightOut, int centreOut,
                   Cor__acc_out* _out) {
  
  int v_25;
  int v_24;
  int v_23;
  int v_22;
  int v_21;
  int v_20;
  int v_19;
  int v_18;
  int v_17;
  int v_16;
  int v_15;
  int v_14;
  int v_13;
  int v_12;
  int v_11;
  int v_10;
  int v_9;
  int v_8;
  int v_7;
  int v_6;
  int v_5;
  int v_4;
  int v_3;
  int v_2;
  int v_1;
  int v;
  v_21 = (leftOut==true);
  if (v_21) {
    v_22 = 1;
  } else {
    v_22 = 0;
  };
  v_20 = (rightOut==true);
  if (v_20) {
    v_23 = 2;
  } else {
    v_23 = v_22;
  };
  v_18 = (rightOut==true);
  v_16 = (leftOut==true);
  v_15 = (centreOut==true);
  v_17 = (v_15&&v_16);
  v_19 = (v_17&&v_18);
  if (v_19) {
    v_24 = 0;
  } else {
    v_24 = v_23;
  };
  v_14 = (centreOut==false);
  if (v_14) {
    v_25 = 3;
  } else {
    v_25 = v_24;
  };
  v_13 = (blocked==true);
  if (v_13) {
    _out->wheelRight = 0;
  } else {
    _out->wheelRight = v_25;
  };
  v_8 = (leftOut==true);
  if (v_8) {
    v_9 = 2;
  } else {
    v_9 = 0;
  };
  v_7 = (rightOut==true);
  if (v_7) {
    v_10 = 1;
  } else {
    v_10 = v_9;
  };
  v_5 = (rightOut==true);
  v_3 = (leftOut==true);
  v_2 = (centreOut==true);
  v_4 = (v_2&&v_3);
  v_6 = (v_4&&v_5);
  if (v_6) {
    v_11 = 0;
  } else {
    v_11 = v_10;
  };
  v_1 = (centreOut==false);
  if (v_1) {
    v_12 = 3;
  } else {
    v_12 = v_11;
  };
  v = (blocked==true);
  if (v) {
    _out->wheelLeft = 0;
  } else {
    _out->wheelLeft = v_12;
  };;
}

