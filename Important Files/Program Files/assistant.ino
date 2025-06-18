#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

void setup() {
  Serial.begin(115200);
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.setCursor(0,10);
  display.println("ESP32 READY");
  display.display();
}

void loop() {
  if (Serial.available()) {
    display.clearDisplay();
    String msg = Serial.readStringUntil('\n');
    display.setCursor(0,0);
    display.println("Bot says:");
    display.setCursor(0,10);
    display.println(msg);
    display.display();
  }
}
