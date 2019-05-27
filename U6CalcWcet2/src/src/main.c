// #define F_CPU 14745600
#include "fblib/firebird.h"

unsigned long millis();
unsigned long micros();

volatile unsigned long timer0_millis=0;
volatile uint32_t timer0_fract=0;
volatile unsigned long timer0_overflow_count=0;

int main(int argc, char  *argv[]) {


  init_devices();

  // TCCR0A = (1 << WGM01);
  TCCR0A = 0;

  TCCR0B = (1 << CS00) | (1 << CS01) ; //prescaling 64
  // TIMSK0 = (1 << OCIE0A);

  // OCR0A = 251;


   TIMSK0 = (1 << TOIE0);
  // int i=100;

  while (1) {
    unsigned long a,b,c;


    a=millis();
    _delay_ms (1000);
    b=millis();
    c=(b-a);
    lcd_print(1, 1, c, 5);
    // lcd_print(2, 1, sizeof(int), 5);

  }
  return 0;
}

ISR(TIMER0_COMPA_vect)
{
    unsigned long m = timer0_millis;
    uint32_t f = timer0_fract;

    m += 1;

    timer0_fract = f;
    timer0_millis = m;
    timer0_overflow_count++;
    if(timer0_overflow_count%5==0)
    TCNT0+=2;
    
}

ISR(TIMER0_OVF_vect)
{
    TCNT0+=4;
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
    m = (cnt + (timer0_overflow_count * 256))*64/14745600;
    sei();
    return m;
}