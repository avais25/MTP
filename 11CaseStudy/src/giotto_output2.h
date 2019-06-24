#include "giotto_input.h"

float bl;
float le;
float ri;
float cn;
float act=0;
float bli;
float lei;
float rii;
float cni;
float lw=0;
float rw=0;

void t1(){
f1(bli,lei,rii,cni,&lw,&rw);
}

void input_t1(){
h1(&bl,&le,&ri,&cn,&bli,&lei,&rii,&cni);
}

void actuation(){
h4(lw,rw,&act);
}
