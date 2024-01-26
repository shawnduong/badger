#ifndef SR_74HC165_H
#define SR_74HC165_H

enum SR_74HC165_PINOUT
{
	SR_74HC165_PL = 0,
	SR_74HC165_CP = 14,
	SR_74HC165_Q7 = 12,
	SR_74HC165_CE = 15
};

void sr_74hc165_init()
{
	pinMode(SR_74HC165_PL, OUTPUT);
	pinMode(SR_74HC165_CP, OUTPUT);
	pinMode(SR_74HC165_Q7, INPUT);
	pinMode(SR_74HC165_CE, OUTPUT);
}

char sr_74hc165_read()
{
	digitalWrite(SR_74HC165_PL, LOW);
	delayMicroseconds(10);
	digitalWrite(SR_74HC165_PL, HIGH);
	delayMicroseconds(10);

	digitalWrite(SR_74HC165_CP, HIGH);
	delayMicroseconds(10);
	digitalWrite(SR_74HC165_CE, LOW);
	char data = shiftIn(SR_74HC165_Q7, SR_74HC165_CP, LSBFIRST);
	digitalWrite(SR_74HC165_CE, HIGH);

	return data;
}

#endif
