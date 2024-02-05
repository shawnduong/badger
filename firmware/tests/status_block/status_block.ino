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

#define SER   13
#define RCLK  15
#define SRCLK 14

#define BUZZ  5

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
	0b00000001,  // Buzzer
};

void setup()
{
	Serial.begin(9600);

	pinMode(SER  , OUTPUT);
	pinMode(RCLK , OUTPUT);
	pinMode(SRCLK, OUTPUT);
	pinMode(BUZZ , OUTPUT);
}

void loop()
{
	for (uint8_t i = 0; i < sizeof(tests); i++)
	{
		digitalWrite(RCLK, LOW);
		shiftOut(SER, SRCLK, LSBFIRST, tests[i]);
		digitalWrite(RCLK, HIGH);
		delay(2500);
	}

	tone(BUZZ, 513);
	delay(200);
	tone(BUZZ, 1046);
	delay(300);

	noTone(BUZZ);
	delay(1000);
}
