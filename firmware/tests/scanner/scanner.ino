/* Scanner
 * See b1/Scanner schematic for more details.
 */

//#include "mfrc522_mcp23017/include.h"
#include <MFRC522.h>
#include <MCP23017.h>  // MCP23017 by Bertrand Lemasle
#include <SPI.h>

#define SS  3  // MCP23017
#define RST 4  // MCP23017

#define MCP23017_I2C_ADDRESS 0x20
MCP23017 mcp23017 = MCP23017(MCP23017_I2C_ADDRESS);

//MFRC522 mfrc522(&mcp23017, SS, RST);
MFRC522 mfrc522(15,2);

void setup()
{
	Serial.begin(9600);

	Wire.begin();
	SPI.begin();

	/* Using pin 0 for the ISR's CE and 2 for SB's CE. Set high so they don't
	   disturb this test. */
	mcp23017.pinMode(0, OUTPUT);
	mcp23017.pinMode(2, OUTPUT);
	mcp23017.digitalWrite(0, HIGH);
	mcp23017.digitalWrite(2, HIGH);

	mcp23017.init();
	mfrc522.PCD_Init();

	mcp23017.writeRegister(MCP23017Register::GPIO_A, 0x00);
	mcp23017.writeRegister(MCP23017Register::GPIO_B, 0x00);
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
	Serial.println("\nStarting a test iteration.\n");
	test_scanner();
	Serial.println("Test iteration complete.\n");
	delay(2000);
}
