/* Sanity Check
 * Just making sure the microcontroller is alive.
 */

uint8_t i = 0;

void setup()
{
	Serial.begin(9600);
	Serial.println("Booted.");
}

void loop()
{
	Serial.print("\nIteration #");
	Serial.println(i);
	i++;

	delay(1000);
}
