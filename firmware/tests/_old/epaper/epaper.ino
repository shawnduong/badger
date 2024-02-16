/* E-Paper Block
 * See b1/E-Paper schematic for more details.
 *
 * Block <-> ESP8266
 * VCC   <-> 3V3
 * RST   <-> D1
 * BUSY  <-> D2
 * DC    <-> D3
 * SCK   <-> D5 (SCLK)
 * DIN   <-> D7 (MOSI)
 * CS    <-> D8 (CS)
 */

#include <GxEPD.h>
#include <GxGDEM029T94/GxGDEM029T94.h>
#include <GxIO/GxIO_SPI/GxIO_SPI.h>
#include <GxIO/GxIO.h>

#define CS   15
#define DC   0
#define RST  5
#define BUSY 4

GxIO_Class io(SPI, CS, DC, RST);
GxEPD_Class display(io, RST, BUSY);

uint64_t i = 0;

void setup()
{
	display.init();
	display.fillScreen(GxEPD_WHITE);

	display.setRotation(0);
	display.setTextColor(GxEPD_BLACK);
}

void test()
{
	display.setCursor(0, i);
	display.print("foobar!");
	i += 1;
}

void loop()
{
	display.drawPaged(test);
	delay(5000);
}
