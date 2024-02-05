/* Scanner
 * See b1/Scanner schematic for more details.
 *
 * Block <-> ESP8266
 * VCC   <-> 3V3
 * RST   <-> D1
 * SCK   <-> D5 (SCLK)
 * MISO  <-> D6 (MISO)
 * MOSI  <-> D7 (MOSI)
 * SDA   <-> D8 (CS)
 */

#include <MFRC522.h> // MFRC522 by GithubCommunity (Miguel Balboa)
#include <SPI.h>

#define RST  5
#define SCK  14
#define MISO 12
#define MOSI 13
#define SDA  15

MFRC522 mfrc522(SDA, RST);

void setup()
{
	Serial.begin(9600);
	SPI.begin();
	mfrc522.PCD_Init();
}

void loop()
{
	while (!(mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial()))
		delay(100);

	mfrc522.PICC_DumpToSerial(&(mfrc522.uid));
}
