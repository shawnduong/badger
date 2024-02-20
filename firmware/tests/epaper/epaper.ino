/* E-Paper
 * See b1/E-Paper schematic for more details.
 * Uses the MCP23017's GPB2 as BUSY, GPB3 as ~CS, GPB4 as DC, and GPB5 as ~RST.
 */

#include "gxepd_mcp23017/include.h"
#include "mcp23017_modded/MCP23017.cpp"

#define EPA_BUS  10  // MCP23017
#define EPA_CS   11  // MCP23017
#define EPA_DC   12  // MCP23017
#define EPA_RST  13  // MCP23017

#define MCP23017_I2C_ADDRESS 0x20
MCP23017 mcp23017 = MCP23017(MCP23017_I2C_ADDRESS);

GxIO_Class io(&mcp23017, SPI, EPA_CS, EPA_DC, EPA_RST);
GxEPD_Class display(&mcp23017, io, EPA_RST, EPA_BUS);

uint8_t epaperDisplayRow = 0;

void setup()
{
	Serial.begin(9600);
	Serial.println("E-Paper Test");

	SPI.begin();

	Wire.begin();
	mcp23017.init();

	mcp23017.writeRegister(MCP23017Register::GPIO_A, 0x00);
	mcp23017.writeRegister(MCP23017Register::GPIO_B, 0x00);

	display.init();
	display.fillScreen(GxEPD_WHITE);
	display.setRotation(0);
	display.setTextColor(GxEPD_BLACK);
}

/* E-paper test. */
void _test_epaper()
{
	display.setCursor(0, epaperDisplayRow);
	display.print("foobar!");
	epaperDisplayRow++;
}
void test_epaper()
{
	display.drawPaged(_test_epaper);
}

void loop()
{
	Serial.println("\nStarting a test iteration.\n");
	test_epaper();
	Serial.println("Test iteration complete.\n");
	delay(2000);
}
