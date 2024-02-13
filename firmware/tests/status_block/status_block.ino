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
	0b01000000,  // Yellow
	0b00100000,  // Red
	0b00010000,  // White
	0b00001000,  // Blue
	0b00000100,  // Red
	0b00000010,  // Yellow
	0b11100000,  // Multi
	0b00011110,  // Multi
	0b00000001,  // Buzzer
};

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
		shiftOut(MOSI, SCLK, LSBFIRST, tests[i]);
		digitalWrite(CS1, HIGH);
		delay(1000);
	}

	tone(TONE, 513);
	delay(200);
	tone(TONE, 1046);
	delay(300);

	noTone(TONE);
	delay(1500);
}
