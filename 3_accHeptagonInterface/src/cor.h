/* --- Generated the 6/10/2018 at 9:40 --- */
/* --- heptagon compiler, version 1.05.00 (compiled sat. oct. 6 4:33:59 CET 2018) --- */
/* --- Command line: /home/avais/.opam/system/bin/heptc -target c -s acc -hepts cor.ept --- */

#ifndef COR_H
#define COR_H

#include "cor_types.h"
#include "fblib.h"
typedef struct Cor__acc_mem {
  Fblib__blocked_mem blocked;
  Fblib__blocked_mem blocked_1;
} Cor__acc_mem;

typedef struct Cor__acc_out {
  int stop;
  int wlf;
} Cor__acc_out;

void Cor__acc_reset(Cor__acc_mem* self);

void Cor__acc_step(Cor__acc_out* _out, Cor__acc_mem* self);

#endif // COR_H
