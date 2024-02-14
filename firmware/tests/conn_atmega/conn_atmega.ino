/* ATmega328-P Connection Test
 * See b1 schematic for more details.
 */

#include <MFRC522.h> // MFRC522 by GithubCommunity (Miguel Balboa)
#include <SPI.h>

#define SCLK 13  // D13 | Pin 19: PB5
#define MISO 12  // D12 | Pin 18: PB4
#define MOSI 11  // D11 | Pin 17: PB3

/* ISR */
#define CS0  10  // D10 | Pin 16: PB2
#define PL    5  // D5  | Pin 11: PD5

/* Status Block */
#define CS1   9  // D9  | Pin 15: PB1
#define TONE  2  // D2  | Pin  4: PD2

/* Scanner */
#define CS2   8  // D8  | Pin 14: PB0
#define RST   4  // D4  | Pin  6: PD4

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

///* Scanner object. */
MFRC522 mfrc522(CS2, RST);

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

	mfrc522.PCD_Init();
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
		SPI.beginTransaction(SPISettings(4000000, LSBFIRST, SPI_MODE0));
		digitalWrite(CS1, LOW);
		SPI.transfer(tests[i]);
		digitalWrite(CS1, HIGH);
		SPI.endTransaction();
		delay(1000);
	}

	tone(TONE, 513);
	delay(200);
	tone(TONE, 1046);
	delay(300);

	noTone(TONE);
	delay(1500);
}

/* Scanner test. */
void test_scanner()
{
	Serial.println("Please scan a card.");
	while (!(mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial()))
		delay(100);

	mfrc522.PICC_DumpToSerial(&(mfrc522.uid));
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

	Serial.println("==============");
	Serial.println("Starting scanner test.");
	test_scanner();
	delay(1000);
}
