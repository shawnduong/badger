/* BID Register
 * See b1/BID Register schematic for more details.
 * Uses the MCP23017's GPA0 as ~CE and GPA1 as ~PL. GPB0 is used to read in the
 * bits from the ISR.
 */

#include <MCP23017.h>  // MCP23017 by Bertrand Lemasle

#define BID_CP  0  // MCP23017
#define BID_PL  1  // MCP23017
#define BID_CE  2  // MCP23017
#define BID_Q7  8  // MCP23017

#define MCP23017_I2C_ADDRESS 0x20
MCP23017 mcp23017 = MCP23017(MCP23017_I2C_ADDRESS);

void setup()
{
	Serial.begin(9600);
	Serial.println("BID Register Test");

	Wire.begin();
	mcp23017.init();

	mcp23017.pinMode(BID_CP, OUTPUT);
	mcp23017.pinMode(BID_PL, OUTPUT);
	mcp23017.pinMode(BID_CE, OUTPUT);
	mcp23017.pinMode(BID_Q7, INPUT );

	mcp23017.writeRegister(MCP23017Register::GPIO_A, 0x00);
	mcp23017.writeRegister(MCP23017Register::GPIO_B, 0x00);
}

/* BID Register test. */
void test_bid_register()
{
	uint8_t data = 0;

	mcp23017.digitalWrite(BID_CE, LOW);
	delayMicroseconds(100);

	mcp23017.digitalWrite(BID_PL, LOW);
	delayMicroseconds(100);
	mcp23017.digitalWrite(BID_PL, HIGH);

	mcp23017.digitalWrite(BID_CP, LOW);
	delayMicroseconds(100);

	for (uint8_t i = 0; i < 8; i++)
	{
		data |= mcp23017.digitalRead(BID_Q7) << i;
		mcp23017.digitalWrite(BID_CP, HIGH);
		delayMicroseconds(100);
		mcp23017.digitalWrite(BID_CP, LOW);
		delayMicroseconds(100);
	}
	mcp23017.digitalWrite(BID_CE, HIGH);

	Serial.print("Value: ");
	Serial.println(data >> 1, BIN);

	if ((data & 0x80) > 0)
		Serial.println("Reset is high.");
	else
		Serial.println("Reset is low.");
}

void loop()
{
	Serial.println("\nStarting a test iteration.\n");
	test_bid_register();
	Serial.println("Test iteration complete.\n");
	delay(2000);
}
