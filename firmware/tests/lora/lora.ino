/* LoRa
 * See b1/LoRa schematic for more details.
 * Uses the MCP23017's GPA6 as NSS, GPA7 as RESET, and GPB1 as DIO0.
 */

#include "lora_mcp23017/include.h"
#include <MCP23017.h>  // MCP23017 by Bertrand Lemasle

#define TEST_TX
#define TEST_RX

#define LORA_NSS   6  // MCP23017
#define LORA_RST   7  // MCP23017
#define LORA_DIO0  9  // MCP23017

#define MCP23017_I2C_ADDRESS 0x20
MCP23017 mcp23017 = MCP23017(MCP23017_I2C_ADDRESS);

void setup()
{
	Serial.begin(9600);
	Serial.println("LoRa Test");

	Wire.begin();
	mcp23017.init();

	mcp23017.writeRegister(MCP23017Register::GPIO_A, 0x00);
	mcp23017.writeRegister(MCP23017Register::GPIO_B, 0x00);

	LoRa.setPins(&mcp23017, LORA_NSS, LORA_RST, LORA_DIO0);
	LoRa.begin(433e6);
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
	#ifdef TEST_TX
		test_lora_tx();
	#endif
	#ifdef TEST_RX
		test_lora_rx();
	#endif
	Serial.println("Test iteration complete.\n");
}
