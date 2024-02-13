/* ATmega328-P Connection Test
 * See b1 schematic for more details.
 */

#define SCLK 13  // D13 | Pin 19: PB5
#define MISO 12  // D12 | Pin 18: PB4
#define MOSI 11  // D11 | Pin 17: PB3

/* ISR */
#define CS0  10  // D10 | Pin 16: PB2
#define PL    5  // D5  | Pin 11: PD5

/* Status Block */
#define CS1   9  // D9  | Pin 15: PB1
#define TONE 14  // A0  | Pin 23: PC0

/* Status block tests. */
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

	pinMode(SCLK, OUTPUT);
	pinMode(MISO, INPUT );
	pinMode(MOSI, OUTPUT);

	pinMode(CS0 , OUTPUT);
	pinMode(PL  , OUTPUT);

	pinMode(CS1 , OUTPUT);
	pinMode(TONE, OUTPUT);

	digitalWrite(CS0, HIGH);
	digitalWrite(CS1, HIGH);
}

/* ISR test. */
void test_isr()
{
	uint8_t data = 0;

	/* Discard the first value as a workaround for a bug.
	   See https://github.com/shawnduong/badger/issues/1 */
	for (uint8_t i = 0; i < 2; i++)
	{
		digitalWrite(CS0, LOW);
		delay(1000);

		digitalWrite(PL, LOW);
		digitalWrite(PL, HIGH);

		digitalWrite(SCLK, LOW);

		/* Manual shift in. */
		for (uint8_t i = 0; i < 8; i++)
		{
			data |= digitalRead(MISO) << i;
			digitalWrite(SCLK, HIGH);
			digitalWrite(SCLK, LOW);
		}
		digitalWrite(CS0, HIGH);
	}

	Serial.print("Value: ");
	Serial.println(data >> 1, BIN);

	if (data & 0x80 > 0)
		Serial.println("Reset is high.");
	else
		Serial.println("Reset is low.");

	Serial.println("");
}

/* Status block test. */
void test_status_block()
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

void loop()
{
	Serial.println("==============");
	Serial.println("Starting ISR test.");
	test_isr();
	delay(1000);

	Serial.println("==============");
	Serial.println("Starting status block test.");
	test_status_block();
	delay(1000);
}
