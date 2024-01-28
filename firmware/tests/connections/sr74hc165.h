#pragma once

enum _SR_74HC165_PINOUT
{
	_SR_74HC165_PL = 0,
	_SR_74HC165_CP = 14,
	_SR_74HC165_Q7 = 12,
	_SR_74HC165_CE = 15
};

void sr_74hc165_init()
{
	pinMode(_SR_74HC165_PL, OUTPUT);
	pinMode(_SR_74HC165_CP, OUTPUT);
	pinMode(_SR_74HC165_Q7, INPUT);
	pinMode(_SR_74HC165_CE, OUTPUT);
}

char sr_74hc165_read()
{
	digitalWrite(_SR_74HC165_PL, LOW);
	delayMicroseconds(10);
	digitalWrite(_SR_74HC165_PL, HIGH);
	delayMicroseconds(10);

	digitalWrite(_SR_74HC165_CP, HIGH);
	delayMicroseconds(10);
	digitalWrite(_SR_74HC165_CE, LOW);
	char data = shiftIn(_SR_74HC165_Q7, _SR_74HC165_CP, LSBFIRST);
	digitalWrite(_SR_74HC165_CE, HIGH);

	return data;
}
