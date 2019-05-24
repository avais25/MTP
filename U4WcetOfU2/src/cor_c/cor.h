/* --- Generated the 12/5/2019 at 2:40 --- */
/* --- heptagon compiler, version 1.05.00 (compiled sat. oct. 6 4:33:59 CET 2018) --- */
/* --- Command line: /home/avais/.opam/system/bin/heptc -target c cor.ept --- */

#ifndef COR_H
#define COR_H

#include "cor_types.h"
typedef struct Cor__lw_out {
  int wheelLeft;
} Cor__lw_out;

void Cor__lw_step(int blocked, int leftOut, int rightOut, int centreOut,
                  Cor__lw_out* _out);

typedef struct Cor__rw_out {
  int wheelRight;
} Cor__rw_out;

void Cor__rw_step(int blocked, int leftOut, int rightOut, int centreOut,
                  Cor__rw_out* _out);

#endif // COR_H
