// #define F_CPU 14745600
#include "fblib/firebird.h"

unsigned long millis();
unsigned long micros();

unsigned long timer0_millis=0;
unsigned int timer0_fract=0;
unsigned long timer0_overflow_count=0;

int main(int argc, char  *argv[]) {


  init_devices();

  TCCR0A = (1 << WGM01);

  TCCR0B = (1 << CS00) | (1 << CS01) ; //prescaling 64

  OCR0A = 252;

  TIMSK0 = (1 << OCIE0A);
int i=100;

  while (1) {
    unsigned long a,b,c;
    a=millis();
    // while (i--)
    // {
    //  _delay_ms (10);
    // }
    _delay_ms (2000);
    
    b=millis();
    c=(b-a);
    lcd_print(1, 1, c, 5);

  }
  return 0;
}

ISR(TIMER0_COMPA_vect)
{
  // TCNT0=0;
    unsigned long m = timer0_millis;
    unsigned int f = timer0_fract;

    m += 1;
    f += 9375;
    if (f >= 100000) {
        f -= 100000;
        m += 1;
    }
    timer0_fract = f;
    timer0_millis = m;
    timer0_overflow_count++;
}

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
    m = (cnt + (timer0_overflow_count * 252))*4.34;
    sei();
    return m;
}