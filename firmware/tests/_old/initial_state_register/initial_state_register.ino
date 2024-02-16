/* Initial State Register
 * See b1/Initial State Register schematic for more details.
 *
 * Block <-> Arduino Uno
 * VCC   <-> 3V3
 * CP    <-> D13 (SCLK)
 * Q7    <-> D12 (MISO)
 * ~CE   <-> D10 (CS)
 * PL    <-> D5
 */

#define SCLK 13  // D13 | Pin 19: PB5
#define MISO 12  // D12 | Pin 18: PB4

#define CS0  10  // D10 | Pin 16: PB2
#define PL    5  // D5  | Pin 11: PD5

void setup()
{
	Serial.begin(9600);

	pinMode(SCLK, OUTPUT);
	pinMode(MISO, INPUT );
	pinMode(CS0 , OUTPUT);
	pinMode(PL  , OUTPUT);
}

void loop()
{
	uint8_t data = 0;

	digitalWrite(CS0, LOW);
	delay(1000);

	digitalWrite(PL, LOW);
	digitalWrite(PL, HIGH);

	digitalWrite(SCLK, LOW);

	/* Manual shift in. */
	for (uint8_t i = 0; i < 8; i++)
	{
		data |= digitalRead(MISO) << i;
		digitalWrite(SCLK, HIGH);
		digitalWrite(SCLK, LOW);
	}
	digitalWrite(CS0, HIGH);

	Serial.print("Value: ");
	Serial.println(data >> 1, BIN);

	if (data & 0x80 > 0)
		Serial.println("Reset is high.");
	else
		Serial.println("Reset is low.");

	Serial.println("");

	delay(1000);
}
