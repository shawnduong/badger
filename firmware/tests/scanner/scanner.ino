/* Scanner
 * See b1/Scanner schematic for more details.
 */

/* Comment this out to use the normal library. */
//#define USE_FORK

#include <SPI.h>

#ifdef USE_FORK
	#include "mfrc522_mcp23017/include.h"
	#include <MCP23017.h>  // MCP23017 by Bertrand Lemasle

	#define MCP23017_I2C_ADDRESS 0x20
	MCP23017 mcp23017 = MCP23017(MCP23017_I2C_ADDRESS);

	#define SS   4  // MCP23017
	#define RST  5  // MCP23017
	MFRC522 mfrc522(&mcp23017, SS, RST);
#else
	#include <MFRC522.h>

	#define SS  15
	#define RST  2
	MFRC522 mfrc522(15,2);
#endif

void setup()
{
	Serial.begin(9600);

	SPI.begin();

	#ifdef USE_FORK
		Wire.begin();
		mcp23017.init();
		mcp23017.writeRegister(MCP23017Register::GPIO_A, 0x00);
		mcp23017.writeRegister(MCP23017Register::GPIO_B, 0x00);
	#endif

	mfrc522.PCD_Init();
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
