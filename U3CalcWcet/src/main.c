// #define F_CPU 14745600
#include "fblib/firebird.h"

unsigned long millis();
unsigned long micros();

unsigned long timer0_millis=0;
unsigned int timer0_fract=0;
unsigned int timer0_overflow_count=0;

int main(int argc, char  *argv[]) {


  init_devices();
  TCCR0A = 0;
  
  // TCCR0B = (1 << CS00);    //version micro second
  TCCR0B = (1 << CS00) | (1 << CS01) ; //version millisec
  TIMSK0 = (1 << TOIE0);

// //lcd print wcet
//  int i=11111;
  while (1) {
    unsigned long a,b,c;
   

    //delay testing
    a=micros();
    _delay_ms (10);
    b=micros();
    c=(b-a);
    lcd_print(1, 1, c, 5);

    // //lcd print wcet
    // a=millis();
    // lcd_print(2, 1, i, 5);
    // b=millis();
    // c=(b-a)/1000;
    // lcd_print(1, 1, c, 5);
    // i++;
  }
  return 0;
}


// version millisec

ISR(TIMER0_OVF_vect)
{
    unsigned long m = timer0_millis;
    unsigned int f = timer0_fract;
  
    m += 1;
    f += 1111;
    if (f >= 10000) {
        f -= 10000;
        m += 1;
    }
    timer0_fract = f;
    timer0_millis = m;
    timer0_overflow_count++;
    // TCNT0=0;
}

// //version micro second
// ISR(TIMER0_OVF_vect)
// {
//     unsigned long m = timer0_millis;
//     unsigned long f = timer0_fract;
//     // long a=0;
//     // _delay_us(17);
  
//     m += 17;
//     f += 3611;
//     if (f >= 10000) {
//         f -= 10000;
//         m += 1;
//     }
//     timer0_fract = f;
//     timer0_millis = m;


    
//     a = TCNT0;

//     // lcd_print(1, 1, a, 5);
//     TCNT0=0;
// }

// //version micro second -- stopped counter
// ISR(TIMER0_OVF_vect)
// {
//     TCCR0B=0;
//     cli();
//     unsigned long m = timer0_millis;
//     unsigned long f = timer0_fract;
  
//     m += 17;
//     f += 3611;
//     if (f >= 10000) {
//         f -= 10000;
//         m += 1;
//     }
//     timer0_fract = f;
//     timer0_millis = m;
//     TCCR0B = (1 << CS00) ;
//     sei();
// }

    
unsigned long millis()
{
    unsigned long m;
    cli();
    m = timer0_millis;
    sei();
    return m;
}

unsigned long micros()
{
    unsigned long m;
    unsigned char cnt;
    cli();
    cnt= TCNT0;
    m = (cnt + (timer0_overflow_count * 256))*4.34;
    sei();
    return m;
}
