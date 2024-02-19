/* Wi-Fi
 * This just tests the ESP8266's Wi-Fi capabilities by doing an HTTPS POST.
 */

#include <ESP8266HTTPClient.h>
#include <ESP8266WiFi.h>
#include <WiFiClient.h>

#define SSID "your-ssid"
#define PASS "your-pass"
#define ENDPOINT "https://your.endpoint.here"

void wifi_setup()
{
	Serial.print("Connecting to ");
	Serial.print(SSID);

	WiFi.mode(WIFI_STA);
	WiFi.begin(SSID, PASS);

	while (WiFi.status() != WL_CONNECTED)
	{
		delay(500);
		Serial.print(".");
	}

	Serial.println(" done.");
//	WiFi.forceSleepBegin();
}

void setup()
{
	Serial.begin(9600);
	Serial.println("Wi-Fi Test");

	wifi_setup();
}

void test_http()
{
//	WiFi.forceSleepWake();

	WiFiClientSecure client;

	/* Don't do this in production. */
	client.connect(ENDPOINT, 443);
	client.setInsecure();

	HTTPClient http;
	http.begin(client, ENDPOINT);
	http.addHeader("Content-Type", "application/json");
	Serial.print("Response code: ");
	Serial.println(http.POST("{'test': 123}"));
	Serial.print("Response data: ");
	Serial.println(http.getString());
	http.end();

//	WiFi.forceSleepBegin();
}

void loop()
{
	Serial.println("\nStarting a test iteration.\n");
	test_http();
	Serial.println("Test iteration complete.\n");
	delay(5000);
}
