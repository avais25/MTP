/* --- Generated the 10/10/2018 at 8:18 --- */
/* --- heptagon compiler, version 1.05.00 (compiled sat. oct. 6 4:33:59 CET 2018) --- */
/* --- Command line: /home/avais/.opam/system/bin/heptc -target c cor.ept --- */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "cor.h"

void Cor__distanceToSpeed_step(int distance, Cor__distanceToSpeed_out* _out) {
  
  int v_2;
  int v_1;
  int v;
  v_1 = (distance==1);
  if (v_1) {
    v_2 = 2;
  } else {
    v_2 = 0;
  };
  v = (distance==2);
  if (v) {
    _out->speed = 3;
  } else {
    _out->speed = v_2;
  };;
}

void Cor__acc_step(int distance, int leftOut, int rightOut, int centreOut,
                   Cor__acc_out* _out) {
  Cor__distanceToSpeed_out Cor__distanceToSpeed_out_st;
  
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
  int v;
  v_22 = (rightOut==true);
  if (v_22) {
    v_23 = 2;
  } else {
    v_23 = 0;
  };
  v_21 = (leftOut==true);
  if (v_21) {
    v_24 = 1;
  } else {
    v_24 = v_23;
  };
  v_19 = (rightOut==true);
  v_17 = (leftOut==true);
  v_16 = (centreOut==true);
  v_18 = (v_16&&v_17);
  v_20 = (v_18&&v_19);
  if (v_20) {
    v_25 = 0;
  } else {
    v_25 = v_24;
  };
  Cor__distanceToSpeed_step(distance, &Cor__distanceToSpeed_out_st);
  v_15 = Cor__distanceToSpeed_out_st.speed;
  v_14 = (centreOut==false);
  if (v_14) {
    _out->wheelRight = v_15;
  } else {
    _out->wheelRight = v_25;
  };
  v_10 = (rightOut==true);
  if (v_10) {
    v_11 = 1;
  } else {
    v_11 = 0;
  };
  v_9 = (leftOut==true);
  if (v_9) {
    v_12 = 2;
  } else {
    v_12 = v_11;
  };
  v_7 = (rightOut==true);
  v_5 = (leftOut==true);
  v_4 = (centreOut==true);
  v_6 = (v_4&&v_5);
  v_8 = (v_6&&v_7);
  if (v_8) {
    v_13 = 0;
  } else {
    v_13 = v_12;
  };
  Cor__distanceToSpeed_step(distance, &Cor__distanceToSpeed_out_st);
  v_3 = Cor__distanceToSpeed_out_st.speed;
  v = (centreOut==false);
  if (v) {
    _out->wheelLeft = v_3;
  } else {
    _out->wheelLeft = v_13;
  };;
}

