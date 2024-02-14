/* Scanner
 * See b1/Scanner schematic for more details.
 *
 * Block <-> Arduino Uno
 * VCC   <-> 3V3
 * SCK   <-> D13 (SCLK)
 * MISO  <-> D12 (MISO)
 * MOSI  <-> D11 (MOSI)
 * SDA   <-> D8
 * RST   <-> D4
 */

#include <MFRC522.h> // MFRC522 by GithubCommunity (Miguel Balboa)
#include <SPI.h>

#define SCLK 13  // D13 | Pin 19: PB5
#define MISO 12  // D12 | Pin 18: PB4
#define MOSI 11  // D11 | Pin 17: PB3

#define CS2   8  // D8  | Pin 14: PB0
#define RST   4  // D4  | Pin  6: PD4

MFRC522 mfrc522(CS2, RST);

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
