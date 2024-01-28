/* Connections Test
 * Check to see if all the modules are connected correctly. If they are, then
 * the hardware is ready for firmware development.
 */

#include <SPI.h>
#include "sr74hc165.h"
#include "sr74hc595.h"

/* Auxiliary shift register used for handling CS and other misc. outputs. Wire
 * it by SPI conventions.
 *
 * QA = CE for ID selector DIP switches (74HC165, aka PISO SR)
 * QB = PL for ID selector DIP switches (74HC165, aka PISO SR)
 */
Sr74hc595 auxSr(13, 15, 14, 0b11111111);

/* Unit ID shift register (input) used for discovering the ID of a Badger unit
 * upon first start.
 */
Sr74hc165 idSr(&auxSr, 14, 12, 0, 1);

void setup()
{
	Serial.begin(9600);
	Serial.println("Initialized.");
	Serial.println("-----------------");
	Serial.print("Unit ID: ");
	Serial.println(idSr.sr_read(), BIN);
}

void loop()
{
	delay(1000);
}
