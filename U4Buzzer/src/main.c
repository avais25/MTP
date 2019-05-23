#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#include "fblib/firebird.h"
unsigned long timer0_micros=0;
unsigned long timer0_fract=0;
unsigned long micros()
{
    unsigned long m;
    cli();
    m = timer0_micros;
    sei();
    return m;
}




//Main Function
int main(void)
{
	init_devices();
  TCCR0B = (1 << CS00);
  TIMSK0 = (1 << TOIE0);

	while(1)
	{
    unsigned long a,b,c;

    
		buzzer_on();
		_delay_ms(1000);		//delay
		buzzer_off();
    a=micros();
		_delay_ms(1000);		//delay
    b=micros();
    c=(b-a)/1000;
    lcd_print(1, 1, c, 5);
	}
}

ISR(TIMER0_OVF_vect)
{
    unsigned long m = timer0_micros;
    unsigned long f = timer0_fract;
  
    m += 17;
    f += 3612;
    if (f >= 10000) {
        f -= 10000;
        m += 1;
    }
    timer0_fract = f;
    timer0_micros = m;
}

    
