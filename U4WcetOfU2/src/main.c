#include "fblib/firebird.h"
#include "cor_c/cor.h"
#include "drivers.h"

//setting up timer and interrupts
unsigned long micros();

unsigned long timer0_micros=0;
unsigned long timer0_fract=0;

int main(int argc, char  *argv[]) {
  TCCR0A = 0;
  TCCR0B = (1 << CS00);    //version micro second
  // TCCR0B = (1 << CS00) | (1 << CS01) ; //version millisec
  TIMSK0 = (1 << TOIE0);


// Cor__acc_out out;
Cor__lw_out lwOut;
Cor__rw_out rwOut;


init_devices();

  while (1) {
      unsigned long a,b,c;

      int blocked, leftOut, rightOut, centreOut;
      int blocked2, leftOut2, rightOut2, centreOut2;

    //   a=micros();
    // _delay_ms (1000);
    // b=micros();
    // c=(b-a)/1000;
    // lcd_print(1, 1, c, 5);

      //calculating wcet for fwActuator
      a=micros();
      fwActuator(&lwOut,&rwOut);
      b=micros();
      c=(b-a);
      // lcd_print(2, 1, c, 5);

      a=micros();
      inputDriver(&blocked,&leftOut,&rightOut,&centreOut);
      b=micros();
      c=(b-a)/1000;
      // lcd_print(2, 1, c, 5);

      a=micros();
      inputDriver2(blocked,leftOut,rightOut,centreOut,&blocked2,&leftOut2,&rightOut2,&centreOut2);
      b=micros();
      c=(b-a);
      // lcd_print(2, 1, c, 5);


      a=micros();
      Cor__lw_step( blocked,  leftOut,  rightOut,  centreOut, &lwOut) ;
      b=micros();
      c=(b-a);
      lcd_print(2, 1, c, 5);

      a=micros();
      Cor__rw_step( blocked2,  leftOut2,  rightOut2,  centreOut2, &rwOut);
      b=micros();
      c=(b-a);
      // lcd_print(2, 1, c, 5);

  }

  return 0;
}


unsigned long micros()
{
    unsigned long m;
    cli();
    m = timer0_micros;
    sei();
    return m;
}

// version millisec

// ISR(TIMER0_OVF_vect)
// {
//     unsigned long m = timer0_micros;
//     unsigned long f = timer0_fract;
  
//     m += 1111;
//     f += 1111;
//     if (f >= 10000) {
//         f -= 10000;
//         m += 1;
//     }
//     timer0_fract = f;
//     timer0_micros = m;
// }

//version micro second
ISR(TIMER0_OVF_vect)
{
    unsigned long m = timer0_micros;
    unsigned long f = timer0_fract;
  
    m += 17;
    f += 3611;
    if (f >= 10000) {
        f -= 10000;
        m += 1;
    }
    timer0_fract = f;
    timer0_micros = m;
}