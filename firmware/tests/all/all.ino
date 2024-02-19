/* All Tests
 * See the b1 schematic for more details.
 */

#include "lora_mcp23017/include.h"
#include "mfrc522_mcp23017/include.h"
#include <MCP23017.h>  // MCP23017 by Bertrand Lemasle
#include <SPI.h>

#define BID_CP  0  // MCP23017
#define BID_PL  1  // MCP23017
#define BID_CE  2  // MCP23017
#define BID_Q7  8  // MCP23017

#define SB_RCLK  3  // MCP23017
#define SB_TONE  2

#define RFID_SS   4  // MCP23017
#define RFID_RST  5  // MCP23017

#define LORA_NSS   6  // MCP23017
#define LORA_RST   7  // MCP23017
#define LORA_DIO0  9  // MCP23017

#define MCP23017_I2C_ADDRESS 0x20
MCP23017 mcp23017 = MCP23017(MCP23017_I2C_ADDRESS);

MFRC522 mfrc522(&mcp23017, RFID_SS, RFID_RST);

/* Status block tests. */
byte tests[] = {
	0b00000000,  // Reset
	0b00000001,  // Green
	0b00000010,  // Yellow
	0b00000100,  // Red
	0b00001000,  // White
	0b00010000,  // Blue
	0b00100000,  // Red
	0b01000000,  // Yellow
	0b00000111,  // Multi
	0b01111000,  // Multi
	0b10000000,  // Buzzer
};

void setup()
{
	Serial.begin(9600);
	Serial.println("Initial State Register Test");

	SPI.begin();
	Wire.begin();

	mcp23017.init();
	mfrc522.PCD_Init();

	mcp23017.pinMode(BID_CP, OUTPUT);
	mcp23017.pinMode(BID_PL, OUTPUT);
	mcp23017.pinMode(BID_CE, OUTPUT);
	mcp23017.pinMode(BID_Q7, INPUT );

	mcp23017.pinMode(SB_RCLK, OUTPUT);

	mcp23017.writeRegister(MCP23017Register::GPIO_A, 0x00);
	mcp23017.writeRegister(MCP23017Register::GPIO_B, 0x00);

	/* Default CE line values. */
	mcp23017.digitalWrite(BID_CE  , HIGH);
	mcp23017.digitalWrite(SB_RCLK , HIGH);
	mcp23017.digitalWrite(RFID_SS , HIGH);
	mcp23017.digitalWrite(LORA_NSS, HIGH);

	LoRa.setPins(&mcp23017, LORA_NSS, LORA_RST, LORA_DIO0);
	LoRa.begin(433e6);
}

/* BID Register test. */
void test_bid_register()
{
	uint8_t data = 0;

	mcp23017.digitalWrite(BID_CE, LOW);
	delayMicroseconds(100);

	mcp23017.digitalWrite(BID_PL, LOW);
	delayMicroseconds(100);
	mcp23017.digitalWrite(BID_PL, HIGH);

	mcp23017.digitalWrite(BID_CP, LOW);
	delayMicroseconds(100);

	for (uint8_t i = 0; i < 8; i++)
	{
		data |= mcp23017.digitalRead(BID_Q7) << i;
		mcp23017.digitalWrite(BID_CP, HIGH);
		delayMicroseconds(100);
		mcp23017.digitalWrite(BID_CP, LOW);
		delayMicroseconds(100);
	}
	mcp23017.digitalWrite(BID_CE, HIGH);

	Serial.print("Value: ");
	Serial.println(data >> 1, BIN);

	if (data & 0x80 > 0)
		Serial.println("Reset is high.");
	else
		Serial.println("Reset is low.");
}

/* Status block test. */
void test_status_block()
{
	for (uint8_t i = 0; i < sizeof(tests); i++)
	{
		mcp23017.digitalWrite(SB_RCLK, LOW);
		SPI.transfer(tests[i]);
		mcp23017.digitalWrite(SB_RCLK, HIGH);
		delay(1000);
	}

	tone(SB_TONE, 513);
	delay(200);
	tone(SB_TONE, 1046);
	delay(300);

	noTone(SB_TONE);

	Serial.println("Done.");
}

/* Scanner test. */
void test_scanner()
{
	Serial.println("Please scan a card.");
	while (!(mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial()))
		delay(100);

	mfrc522.PICC_DumpToSerial(&(mfrc522.uid));
}

/* LoRa Tx test. */
void test_lora_tx()
{
	Serial.print("Sending packet... ");
	LoRa.beginPacket();
	LoRa.print(F("Hello world!"));
	LoRa.endPacket();
	Serial.println("done.");
}

/* LoRa Rx test. */
void test_lora_rx()
{
	Serial.print("Waiting to receive packet... ");
	while (!LoRa.parsePacket())  delay(1);
	Serial.println("done.");

	Serial.print("Received packet '");
	while (LoRa.available())  Serial.print((char)LoRa.read());
	Serial.print("' with RSSI ");
	Serial.println(LoRa.packetRssi());
}

void loop()
{
	Serial.println("\nStarting a test iteration.\n");

	Serial.println("--> BID Register Test");
	test_bid_register();

	Serial.println("--> Status Block Test");
	test_status_block();

	Serial.println("--> Scanner Test");
	test_scanner();

	Serial.println("--> LoRa Tx Test");
	test_lora_tx();

	Serial.println("--> LoRa Rx Test");
	test_lora_rx();

	Serial.println("Test iteration complete.\n");
	delay(2000);
}
