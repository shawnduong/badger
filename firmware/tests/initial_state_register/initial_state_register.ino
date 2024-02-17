/* Initial State Register
 * See b1/Initial State Register schematic for more details.
 * Uses the MCP23017's GPA0 as ~CE and GPA1 as ~PL. GPB0 is used to read in the
 * bits from the ISR.
 */

#include <MCP23017.h>  // MCP23017 by Bertrand Lemasle

/* MCP23017 */
#define ISR_CP 0
#define ISR_PL 1
#define ISR_CE 2
#define ISR_Q7 8

#define MCP23017_I2C_ADDRESS 0x20
MCP23017 mcp23017 = MCP23017(MCP23017_I2C_ADDRESS);

void setup()
{
	Serial.begin(9600);
	Serial.println("Initial State Register Test");

	Wire.begin();
	mcp23017.init();

	mcp23017.pinMode(ISR_CP, OUTPUT);
	mcp23017.pinMode(ISR_PL, OUTPUT);
	mcp23017.pinMode(ISR_CE, OUTPUT);
	mcp23017.pinMode(ISR_Q7, INPUT );

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

void loop()
{
	Serial.println("\nStarting a test iteration.\n");
	test_isr();
	Serial.println("Test iteration complete.\n");
	delay(2000);
}
