---
Title: "RasBuddy"
Author: "Sahil321-Coder"
Description: "A AI Assistant made with Raspberry Pi"
Created_at: "29-05-2025"
---

# May 29th: Choosing the Hardware, Software & Designing 3D Model!

So, the hardware I have chosen is 🛠️:
 1. Raspberry Pi 4 4GB
 2. SSD1306 OLED display (I2C)
 3. USB Microphone ( Storin Mini Speech Microphone with USB Connector Stand for PC Laptop Desktop ) 
 4. Speaker 3.5mm Jack
 5. MicroSD card 32GB
    
So, the software I have chosen is 💻:

 1. Raspberry Pi Imager
 2. Python 3.7+
 3. Libraries: vosk, sounddevice, pyttsx3, argostranslate, requests, Pillow, Adafruit-SSD1306, etc.
     (Refer to instructions.txt )

   ![Screenshot 2025-05-29 090920](https://github.com/user-attachments/assets/dbe9520b-719e-4b50-9476-25c67784cc9e)
   ![Screenshot 2025-05-29 091201](https://github.com/user-attachments/assets/a8cdb03f-1d8e-487b-b8e6-5aa9c7ed2e48)



**Total time spent: 3h**

# May 30th: Half Python Programming!

After Downloading Raspberry Pi Imager.
You will get three options on starting Pi Imager:
 1.It will be Choose Device, select Raspberry Pi 4
 2. Next option will be Choose OS, select Raspberry Pi OS (64-bit)
 3. The last option will be Choose Storage. For that, you need to insert the SD Card you brought, and you will see one option when you put the SD card, select it, then continue
   you will get the option to customize, so click edit settings. Next, put these things in their place:
   
 Set hostname : raspi-assistant
 
 Enable SSH: Yes
 
 Set username and password (e.g., pi/raspberry)
 
 Configure Wi-Fi 
 
 Set locale, timezone (e.g., Asia/Kolkata for India) 
 
 Click Save.
 
 Then click Yes, then Yes again.
 
Congratulations You have successfully Setup the Pi Imager

First, enable I2C by going to Interface Options > I2C > Enable in Raspberry Pi Imager.
Next: Install the required libraries ( Copy the text below and paste it in the Raspberry Pi Imager Terminal )

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-pil i2c-tools espeak portaudio19-dev -y

pip3 install vosk pyttsx3 sounddevice pygame argostranslate requests adafruit-circuitpython-ssd1306
```

Next, download and install the libraries:(The files that we will be downloading in the code are given in Important Files > Libraries > ( there will be a Google Drive link, click on it)( You will see two files, download them and upload them into your RasBuddy code.) After uploading the two files, run this code in the terminal of Raspberry Pi Imager:

Install Vosk Model & Argos Model:
```bash
# Vosk small model (offline speech recognition)
wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
unzip vosk-model-small-en-us-0.15.zip

# Argos Hindi to English translation model
wget https://www.argosopentech.com/argospm/index/translate-hi_en.argosmodel
argos-translate --install translate-hi_en.argosmodel
06
```
**Total time spent: 3.6h**

# May 31st: Python Programming Completed and the Project also Completed!





