/* E-Paper
 * See b1/E-Paper schematic for more details.
 * Uses the MCP23017's GPB2 as BUSY, GPB3 as ~CS, GPB4 as DC, and GPB5 as ~RST.
 */

//#include <GxEPD.h>
//#include <GxGDEM029T94/GxGDEM029T94.h>
//#include <GxIO/GxIO_SPI/GxIO_SPI.h>
//#include <GxIO/GxIO.h>

#include <MCP23017.h>  // MCP23017 by Bertrand Lemasle

#define EPA_BUS  10
#define EPA_CS   11
#define EPA_DC   12
#define EPA_RST  13

#define MCP23017_I2C_ADDRESS 0x20
MCP23017 mcp23017 = MCP23017(MCP23017_I2C_ADDRESS);

GxIO_Class io(mcp23017, SPI, EPA_CS, EPA_DC, EPA_RST);
GxEPD_Class display(io, EPA_RST, EPA_BUSY);

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
