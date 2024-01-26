/* Connect Test
 * Check to see if all the modules are connected correctly. If they are, then
 * the hardware is ready for firmware development.
 */

#include <SPI.h>
#include "sr_74hc165.h"

char srData;

void setup()
{
	Serial.begin(9600);
	sr_74hc165_init();

	Serial.println("Initialized.");
}

void loop()
{
	srData = sr_74hc165_read();

	Serial.println("Shift Register 74HC165 Test");
	Serial.print("Pin data: ");
	Serial.println(srData, BIN);

	delay(1000);
}
