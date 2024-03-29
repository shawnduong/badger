/* Status Block
 * See b1/Status Block schematic for more details.
 * Uses the MCP23017's GPA2 as RCLK.
 */

#include <MCP23017.h>  // MCP23017 by Bertrand Lemasle
#include <SPI.h>

#define SB_RCLK  3  // MCP23017
#define SB_TONE  2

#define MCP23017_I2C_ADDRESS 0x20
MCP23017 mcp23017 = MCP23017(MCP23017_I2C_ADDRESS);

/* Status block tests. */
byte tests[] = {
	0b00000000,  // Reset
	0b00000010,  // Green
	0b00000100,  // Yellow
	0b00001000,  // Red
	0b00010000,  // White
	0b00100000,  // Blue
	0b01000000,  // Red
	0b10000000,  // Yellow
	0b00001110,  // Multi
	0b11110000,  // Multi
	0b00000001,  // Buzzer
};

void setup()
{
	Serial.begin(9600);
	Serial.println("Status Block Test");

	SPI.begin();

	Wire.begin();
	mcp23017.init();

	mcp23017.pinMode(SB_RCLK, OUTPUT);

	mcp23017.writeRegister(MCP23017Register::GPIO_A, 0x00);
	mcp23017.writeRegister(MCP23017Register::GPIO_B, 0x00);
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

	Serial.println("Done.");
}

void loop()
{
	Serial.println("\nStarting a test iteration.\n");
	test_status_block();
	Serial.println("Test iteration complete.\n");
	delay(2000);
}
