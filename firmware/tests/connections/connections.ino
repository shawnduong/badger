/* Connections Test
 * Check to see if all the modules are connected correctly. If they are, then
 * the hardware is ready for firmware development.
 */

#include <SPI.h>
#include "sr74hc595.h"

/* Auxiliary shift register used for handling CS and other misc. outputs. Wire
 * it by SPI conventions.
 *
 * QA = CS for ID selector DIP switches (74HC165, aka PISO SR)
 * QB = PL for ID selector DIP switches (74HC165, aka PISO SR)
 */
Sr74hc595 auxSr(13, 15, 14, 0b11111111);

void setup()
{
	Serial.begin(9600);
	Serial.println("Initialized.");
}

void loop()
{
	auxSr.sr_write_bit(5, 0);
	auxSr.sr_write_bit(3, 0);
	auxSr.sr_write_bit(2, 0);
	Serial.println(auxSr.get_state(), BIN);
	delay(1000);

	auxSr.sr_write_bit(5, 1);
	auxSr.sr_write_bit(3, 1);
	auxSr.sr_write_bit(2, 1);
	Serial.println(auxSr.get_state(), BIN);
	delay(1000);
}
