/* LoRa
 * See b1/LoRa schematic for more details.
 *
 * Block <-> ESP8266
 * VCC   <-> 3V3
 * RST   <-> D0
 * DIO0  <-> D1
 * SCK   <-> D5 (SCLK)
 * MISO  <-> D6 (MISO)
 * MOSI  <-> D7 (MOSI)
 * NSS   <-> D8 (CS)
 */

#include <LoRa.h>
#include <SPI.h>

#define DIO0 5
#define SS   15
#define RST  16

//#define MODE_TX  // comment this line out if you want to rx.

void setup()
{
	Serial.begin(9600);
	LoRa.setPins(SS, RST, DIO0);
	LoRa.begin(433e6);
	LoRa.setSpreadingFactor(8);
	LoRa.setSyncWord(0x13);
}

void loop()
{
#ifdef MODE_TX
	Serial.print("Sending packet... ");
	LoRa.beginPacket();
	LoRa.println(F("Hello world!"));
	LoRa.endPacket();
	Serial.println("done.");
	delay(5000);

#else
	if (LoRa.parsePacket())
	{
		Serial.print("Received packet '");
		while (LoRa.available())  Serial.print((char)LoRa.read());
		Serial.print("' with RSSI ");
		Serial.println(LoRa.packetRssi());
	}
#endif
}
