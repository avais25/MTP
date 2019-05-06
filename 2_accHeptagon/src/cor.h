/* --- Generated the 7/10/2018 at 5:56 --- */
/* --- heptagon compiler, version 1.05.00 (compiled sat. oct. 6 4:33:59 CET 2018) --- */
/* --- Command line: /home/avais/.opam/system/bin/heptc -target c -s acc-hepts cor.ept --- */

#ifndef COR_H
#define COR_H

#include "cor_types.h"
typedef struct Cor__acc_out {
  int stop;
  int wlf;
} Cor__acc_out;

void Cor__acc_step(int blocked, Cor__acc_out* _out);

#endif // COR_H
