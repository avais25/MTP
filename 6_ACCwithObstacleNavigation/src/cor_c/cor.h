/* --- Generated the 10/10/2018 at 9:50 --- */
/* --- heptagon compiler, version 1.05.00 (compiled sat. oct. 6 4:33:59 CET 2018) --- */
/* --- Command line: /home/avais/.opam/system/bin/heptc -target c cor.ept --- */

#ifndef COR_H
#define COR_H

#include "cor_types.h"
typedef struct Cor__frontDistanceToSpeed_out {
  int speed;
} Cor__frontDistanceToSpeed_out;

void Cor__frontDistanceToSpeed_step(int frontDistance,
                                    Cor__frontDistanceToSpeed_out* _out);

typedef struct Cor__acc_out {
  int wheelLeft;
  int wheelRight;
} Cor__acc_out;

void Cor__acc_step(int frontDistance, int leftDiistance, int leftOut,
                   int rightOut, int centreOut, Cor__acc_out* _out);

#endif // COR_H
