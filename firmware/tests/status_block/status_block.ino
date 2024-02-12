/* Status Block
 * See b1/Status Block schematic for more details.
 *
 * Block <-> ESP8266
 * VCC   <-> 3V3
 * SER   <-> D7 (MOSI)
 * RCLK  <-> D8 (CS)
 * SRCLK <-> D5 (SCLK)
 * BUZZ  <-> D1
 */

#define SCLK 13  // D13 | Pin 19: PB5
#define MOSI 11  // D11 | Pin 17: PB3
#define CS1   9  // D9  | Pin 15: PB1

#define TONE 14  // A0  | Pin 23: PC0

byte tests[] = {
	0b00000000,  // Reset
	0b10000000,  // Green
	0b01000000,  // Blue
	0b00100000,  // Red
	0b00010000,  // White
	0b00001000,  // Red
	0b10000100,  // (Blink) Green
	0b01000100,  // (Blink) Blue
	0b00100100,  // (Blink) Red
	0b00010010,  // (Blink) White
	0b00001010,  // (Blink) Red
	0b10010100,  // (Blink) Green, White
	0b10010110,  // (Blink) Green, (Blink) White
	0b10010111,  // Green, Red, Buzzer
};

/* On the Uno, some SRs (especially clones) are too slow, so we need to slow
   down the rate at which data is shifted out. */
void _shiftOut(uint8_t outPin, uint8_t clkPin, uint8_t order, byte data)
{
	for (uint8_t i = 0; i < 8; i++)
	{
		delayMicroseconds(250);
		digitalWrite(clkPin, LOW);
		delayMicroseconds(250);
		digitalWrite(outPin, (data >> i) & 1);
		delayMicroseconds(250);
		digitalWrite(clkPin, HIGH);
	}
}

void setup()
{
	Serial.begin(9600);

	pinMode(MOSI, OUTPUT);
	pinMode(CS1 , OUTPUT);
	pinMode(SCLK, OUTPUT);
	pinMode(TONE, OUTPUT);

	digitalWrite(CS1, HIGH);
}

void loop()
{
	for (uint8_t i = 0; i < sizeof(tests); i++)
	{
		digitalWrite(CS1, LOW);
		_shiftOut(MOSI, SCLK, LSBFIRST, tests[i]);
		digitalWrite(CS1, HIGH);
		delay(2000);
	}

	tone(TONE, 513);
	delay(200);
	tone(TONE, 1046);
	delay(300);

	noTone(TONE);
	delay(1500);
}
