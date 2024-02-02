/* Initial State Register
 * See b1/Initial State Register schematic for more details.
 *
 * Block <-> ESP8266
 * VCC   <-> 3V3
 * PL    <-> D1
 * CP    <-> D5 (SCLK)
 * ~CE   <-> D8 (CS)
 * Q7    <-> D6 (MISO)
 */

#define PL 5
#define CP 14
#define Q7 12
#define CE 15

void setup()
{
	Serial.begin(9600);

	pinMode(PL, OUTPUT);
	pinMode(CP, OUTPUT);
	pinMode(Q7, INPUT );
	pinMode(CE, OUTPUT);
}

void loop()
{
	uint8_t data = 0;

	digitalWrite(PL, LOW);
	digitalWrite(PL, HIGH);

	digitalWrite(CE, LOW);
	digitalWrite(CP, LOW);

	/* Manual shift in. */
	for (uint8_t i = 0; i < 8; i++)
	{
		data |= digitalRead(Q7) << i;
		digitalWrite(CP, HIGH);
		digitalWrite(CP, LOW);
	}
	digitalWrite(CE, HIGH);

	Serial.print("Value: ");
	Serial.println(data >> 1, BIN);

	if (data & 0x80 > 0)
		Serial.println("Reset is high.");
	else
		Serial.println("Reset is low.");

	Serial.println("");

	delay(1000);
}
