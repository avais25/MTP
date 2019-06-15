#include "giotto_input.c"

float s1;
float a=0;
float i1;
float i2;
float o1=0;
float t_o1=0;
float o2=0;
float t_o2=0;
float p1=0;
float p2=0;

void t1(){
f1(i1,&t_o1);
}

void t2(){
f2(i2,&t_o2);
}

void t1_update(){
o1=t_o1;
}

void t2_update(){
o2=t_o2;
}

void d1(){
h1(o2,&i1);
}

void d2(){
h2(&s1,&i2);
}

void d4(){
h4(o1,&a);
}
