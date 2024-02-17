/* All Tests
 * See the b1 schematic for more details.
 */

#include <MCP23017.h>  // MCP23017 by Bertrand Lemasle
#include <SPI.h>

/* MCP23017 */
#define ISR_CP 0
#define ISR_PL 1
#define ISR_CE 2
#define ISR_Q7 8

#define SB_RCLK 3  // MCP23017
#define SB_TONE 2

#define MCP23017_I2C_ADDRESS 0x20
MCP23017 mcp23017 = MCP23017(MCP23017_I2C_ADDRESS);

/* Status block tests. */
byte tests[] = {
	0b00000000,  // Reset
	0b00000001,  // Green
	0b00000010,  // Yellow
	0b00000100,  // Red
	0b00001000,  // White
	0b00010000,  // Blue
	0b00100000,  // Red
	0b01000000,  // Yellow
	0b00000111,  // Multi
	0b01111000,  // Multi
	0b10000000,  // Buzzer
};

void setup()
{
	Serial.begin(9600);
	Serial.println("Initial State Register Test");

	SPI.begin();
	Wire.begin();

	mcp23017.init();

	mcp23017.pinMode(ISR_CP, OUTPUT);
	mcp23017.pinMode(ISR_PL, OUTPUT);
	mcp23017.pinMode(ISR_CE, OUTPUT);
	mcp23017.pinMode(ISR_Q7, INPUT );

	mcp23017.pinMode(SB_RCLK, OUTPUT);

	mcp23017.writeRegister(MCP23017Register::GPIO_A, 0x00);
	mcp23017.writeRegister(MCP23017Register::GPIO_B, 0x00);
}

/* ISR test. */
void test_isr()
{
	uint8_t data = 0;

	mcp23017.digitalWrite(ISR_CE, LOW);
	delayMicroseconds(100);

	mcp23017.digitalWrite(ISR_PL, LOW);
	delayMicroseconds(100);
	mcp23017.digitalWrite(ISR_PL, HIGH);

	mcp23017.digitalWrite(ISR_CP, LOW);
	delayMicroseconds(100);

	for (uint8_t i = 0; i < 8; i++)
	{
		data |= mcp23017.digitalRead(ISR_Q7) << i;
		mcp23017.digitalWrite(ISR_CP, HIGH);
		delayMicroseconds(100);
		mcp23017.digitalWrite(ISR_CP, LOW);
		delayMicroseconds(100);
	}
	mcp23017.digitalWrite(ISR_CE, HIGH);

	Serial.print("Value: ");
	Serial.println(data >> 1, BIN);

	if (data & 0x80 > 0)
		Serial.println("Reset is high.");
	else
		Serial.println("Reset is low.");
}

/* Status block test. */
void test_status_block()
{
	for (uint8_t i = 0; i < sizeof(tests); i++)
	{
		mcp23017.digitalWrite(SB_RCLK, LOW);
		SPI.transfer(tests[i]);
		mcp23017.digitalWrite(SB_RCLK, HIGH);
		delay(1000);
	}

	tone(SB_TONE, 513);
	delay(200);
	tone(SB_TONE, 1046);
	delay(300);

	noTone(SB_TONE);
	delay(1500);
}

void loop()
{
	Serial.println("\nStarting a test iteration.\n");

	Serial.println("--> ISR Test");
	test_isr();

	Serial.println("--> Status Block Test");
	test_status_block();

//	Serial.println("--> Scanner Test");
//	test_scanner();

	Serial.println("Test iteration complete.\n");
	delay(2000);
}
