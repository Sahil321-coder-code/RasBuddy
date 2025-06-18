#include <WiFi.h>
#include <HTTPClient.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET    -1
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

// Replace with your Wi-Fi credentials
const char* ssid = "YOUR_WIFI_SSID";
const char* password = "YOUR_WIFI_PASSWORD";

// Replace with the IP address of your PC running the Flask server
const char* serverName = "http://192.168.1.100:5000/translate";

void setup() {
  Serial.begin(115200);

  // OLED setup
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println("SSD1306 allocation failed");
    for (;;);
  }
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 0);
  display.println("Connecting WiFi...");
  display.display();

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  display.clearDisplay();
  display.setCursor(0, 0);
  display.println("WiFi Connected!");
  display.display();
  delay(1000);
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;

    http.begin(serverName);
    http.addHeader("Content-Type", "application/octet-stream");

    // Simulated audio payload - just sending dummy data
    uint8_t dummyAudio[100] = {0};

    int httpResponseCode = http.POST(dummyAudio, sizeof(dummyAudio));

    if (httpResponseCode > 0) {
      String response = http.getString();
      Serial.println(response);

      // Extract message (basic)
      int index = response.indexOf(":");
      int end = response.indexOf("}");
      String translated = response.substring(index + 2, end - 1);

      display.clearDisplay();
      display.setCursor(0, 0);
      display.setTextWrap(true);
      display.println("Translated:");
      display.println(translated);
      display.display();
    } else {
      Serial.print("Error code: ");
      Serial.println(httpResponseCode);
    }

    http.end();
  } else {
    Serial.println("WiFi Disconnected");
  }

  delay(10000);  // Wait 10 seconds before next request
}
