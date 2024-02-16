/* MCP23017 Test
 * See b1/Wi-Fi and MCU page for details.
 */

#include <MCP23017.h>  // MCP23017 by Bertrand Lemasle

#define MCP23017_I2C_ADDRESS 0x20
MCP23017 mcp23017 = MCP23017(MCP23017_I2C_ADDRESS);

void setup()
{
	Serial.begin(9600);
	Serial.println("MCP23017 Test");

	Wire.begin();
	mcp23017.init();

	/* GPA0 = 0, GPA1 = 1, ... GPB7 = 15 */
	mcp23017.pinMode(0, OUTPUT);
	mcp23017.pinMode(1, INPUT );
	mcp23017.pinMode(8, OUTPUT);
	mcp23017.pinMode(9, INPUT );

	mcp23017.writeRegister(MCP23017Register::GPIO_A, 0x00);
	mcp23017.writeRegister(MCP23017Register::GPIO_B, 0x00);
}

void loop()
{
	uint8_t buffer;

	Serial.println("\nStarting a test iteration.\n");

	Serial.print("Reading GPA1... ");
	buffer = mcp23017.digitalRead(1);
	Serial.println(buffer);
	Serial.println("Writing to GPA0.");
	mcp23017.digitalWrite(0, buffer);

	delay(2000);

	Serial.print("Reading GPB1... ");
	buffer = mcp23017.digitalRead(9);
	Serial.println(buffer);
	Serial.println("Writing to GPB0.");
	mcp23017.digitalWrite(8, buffer);

	delay(2000);

	Serial.println("Clearing.");
	mcp23017.digitalWrite(0, 0);
	mcp23017.digitalWrite(8, 0);

	Serial.println("Test iteration complete.\n");

	delay(2000);
}
