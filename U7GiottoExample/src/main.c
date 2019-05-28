// #define F_CPU 14745600
#include "fblib/firebird.h"



volatile unsigned int schedule = 0;

int main(int argc, char *argv[])
{

    init_devices();

    TCCR4A = (1 << WGM42); //CTC Mode

    TCCR4B = (1 << CS00) | (1 << CS01); //prescaling 64
    TIMSK4 = (1 << OCIE4A);
    OCR4A = 230;
    schedule=6;

    while (1)
    {
        switch (schedule)
        {
        case 0: //cpu idel case
            break;

        case 1: //read 1
            schedule = 0;
            break;

        case 2: //task 1
            schedule = 0;
            break;

        case 3: //task 3
            schedule = 0;
            break;

        case 4: //driver 1
            schedule = 0;
            break;

        case 5: //driver 3
            schedule = 0;
            break;

        case 6: //driver 4
            schedule = 0;
            break;

        default:
            schedule = 0;
            break;
        }
    }
    return 0;
}

ISR(TIMER4_COMPA_vect)
{
    switch (OCR4A)
    {
    case 230: //scheduling r1
        OCR4A = 288;
        schedule = 1;
        break;
    case 288: //scheduling d1
        OCR4A = 345;
        schedule = 4;
        break;
    case 345: //scheduling t1
        OCR4A = 403;
        schedule = 2;
        break;
    case 403: //scheduling d3
        OCR4A = 633;
        schedule = 5;
        break;
    case 633: //scheduling t3
        OCR4A = 864;
        schedule = 3;
        break;
    case 864: //scheduling d1
        OCR4A = 921;
        schedule = 4;
        break;
    case 921: //scheduling t1
        OCR4A = 1152;
        schedule = 2;
        break;
    case 1152: //scheduling r1
        OCR4A = 1382;
        schedule = 1;
        break;
    case 1382: //scheduling d4
        OCR4A = 1612;
        schedule = 6;
        break;
    case 1612: //scheduling d3
        OCR4A = 1843;
        schedule = 5;
        break;
    case 1843: //scheduling t3
        OCR4A = 2073;
        schedule = 3;
        break;
    case 2073: //scheduling r1
        OCR4A = 2188;
        schedule = 1;
        break;
    case 2188: //scheduling d3
        OCR4A = 2361;
        schedule = 5;
        break;
    case 2361: //scheduling t3
        OCR4A = 2764;
        schedule = 3;
        break;
    case 2764: //scheduling d4 ,new iteration
        TCNT4=0;
        OCR4A = 230;
        schedule = 6;
        break;

    default:
        break;
    }
}

