// #define F_CPU 14745600
#include "fblib/firebird.h"

unsigned long micros();

unsigned long timer0_micros=0;
unsigned long timer0_fract=0;

int main(int argc, char  *argv[]) {


  init_devices();
  // TCCR0A = 0;
  
  // TCCR0B = (1 << CS00);    //version micro second
  TCCR0B = (1 << CS00) | (1 << CS01) ; //version millisec
  TIMSK0 = (1 << TOIE0);

 int i=11111;
  while (1) {
    unsigned long a,b,c;
   

    //delay testing
    a=micros();
    _delay_ms (1000);
    b=micros();
    c=(b-a)/1000;
    lcd_print(1, 1, c, 5);

    // //lcd print wcet
    // a=micros();
    // lcd_print(2, 1, i, 5);
    // b=micros();
    // c=(b-a)/1000;
    // lcd_print(1, 1, c, 5);
    // i++;
  }
  return 0;
}


// version millisec

ISR(TIMER0_OVF_vect)
{
    unsigned long m = timer0_micros;
    unsigned long f = timer0_fract;
  
    m += 1111;
    f += 1111;
    if (f >= 10000) {
        f -= 10000;
        m += 1;
    }
    timer0_fract = f;
    timer0_micros = m;
}

// //version micro second
// ISR(TIMER0_OVF_vect)
// {
//     unsigned long m = timer0_micros;
//     unsigned long f = timer0_fract;
  
//     m += 17;
//     f += 3611;
//     if (f >= 10000) {
//         f -= 10000;
//         m += 1;
//     }
//     timer0_fract = f;
//     timer0_micros = m;
// }

// //version micro second -- stopped counter
// ISR(TIMER0_OVF_vect)
// {
//     TCCR0B=0;
//     cli();
//     unsigned long m = timer0_micros;
//     unsigned long f = timer0_fract;
  
//     m += 17;
//     f += 3611;
//     if (f >= 10000) {
//         f -= 10000;
//         m += 1;
//     }
//     timer0_fract = f;
//     timer0_micros = m;
//     TCCR0B = (1 << CS00) ;
//     sei();
// }

    
unsigned long micros()
{
    unsigned long m;
    cli();
    m = timer0_micros;
    sei();
    return m;
}

