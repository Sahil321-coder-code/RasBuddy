---
Title: "RasBuddy"
Author: "Sahil321-Coder"
Description: "A AI Assistant made with Raspberry Pi"
Created_at: "29-05-2025"
---
# Total Time Spent = ~29 Hours

# May 29th: Choosing the Hardware, Software & Designing 3D Model


So, today I will be chosing the hardware for my project, and also I need to choose them by their quality, price & its working too! So, it's 9:00 AM here. I'm on my laptop and now I'm using the websites Ebhoot, RoboticsDNA, RoboSAP, and Silverline Electronics for the parts, as they are the vendors recommended by Hack Club. So now I am making a list of components that i will be using in the project by keeping in mind that they should be available on these websites so that I can start it Now I have all the Types of parts, and I will be searching for software needed for the project

So I have successfully chosen the hardware and there is also the list of Hardware and Software below.
So, the hardware I have chosen is 🛠️:
 1. Raspberry Pi 4 4GB
 2. SSD1306 OLED display (I2C)
 3. USB Microphone Raspberry Pi compatible Microphone (Refer to the video) 
 4. Speaker 3.5mm Jack
 5. MicroSD card 32GB

   ![Screenshot 2025-05-29 091201](https://github.com/user-attachments/assets/a8cdb03f-1d8e-487b-b8e6-5aa9c7ed2e48)

I have got the software and they are all free! So, that's great news, and now I will be configuring the software as per the project requirements, and setting them up!

Now after I have doen the setup and Configured the softwares as per the requirements now tomorrow I will be writing the python program.
So, the software I have chosen is 💻:

 1. Arduino IDE

![download](https://github.com/user-attachments/assets/ab0e670a-fe69-4f4a-a1f3-fd473b00838a)
 
 3. Python 3.7+

![image](https://github.com/user-attachments/assets/ad84a264-cf08-4589-9adb-76894905b943)


 4. PyCharm Community Edition

![image](https://github.com/user-attachments/assets/08a956b5-b86f-4704-9361-9171d5bfa715)

   
 6. Libraries: vosk, sounddevice, pyttsx3, argostranslate, requests, Pillow, Adafruit-SSD1306, etc.

![image](https://github.com/user-attachments/assets/a22aeefc-d90c-4331-8823-27c9c90ca5eb)


![image](https://github.com/user-attachments/assets/6b312600-d56f-4ce7-9ff7-576b62c82780)


The hardware and software I have chosen are completely free and are working perfect on Windows & Mac, so note the hardware and take it.Bye!!

**Total time spent: 6h**

# May 30th: Half Python Programming!

So, today we will be writing and installing the required softwares and apps, firts you are going to need Raspberry Pi Imager software and the details you are going to need for to put in the software are given 👇 below.
So, first we will be downloading the the Docker for the translation, follow the steps below for smooth results:

🔧 STEP 1: Install Docker
Go to this website: [Docker](https://www.docker.com/products/docker-desktop)

🧠 STEP 2: Run LibreTranslate with Hindi–English Models
Run this in your terminal or PowerShell:

```bash
docker run -p 5000:5000 libretranslate/libretranslate
```
LibreTranslate server will be available at:
```bash
http://localhost:5000
```
🧠 Step 3: Install the Argos Model (Hindi → English)(you will get a Argos file in the Libraries folder)
You have an .argosmodel file already downloaded. Let’s install it.
1.Install Argos Translate CLI (only needed once):
```bash
pip install argos-translate
```
2.pip install argos-translate
```bash
argos-translate-cli --install path\to\hi_en.argosmodel
```
✅ Step 3: Test Your Local LibreTranslate
Run this Python code to check if Hindi → English translation works:
```bash
import requests

response = requests.post("http://localhost:5000/translate", data={
    "q": "मुझे हिंदी आती है",
    "source": "hi",
    "target": "en",
    "format": "text"
})

print(response.json()["translatedText"])
```

Output should be: "I know Hindi"

✅ You’re Done


Next, install the Arduino IDE from the Arduino Website and set the Board to ESP32 Dev Module
Install the libraries given below:
1.Adafruit_SSD1306
2.Adafruit_GFX

✅ You’re Done.

**Total time spent: 7h**

# May 31st: Python Programming Completed!

So, I have yesterday made the Python Programming but half and now I am completing it and also adding advaced features like Music, Time, Wetaher, etc.To know more features stay  tuned for the final prototype, it will be made if my project gets approved! And also make sure you are well known to python programming, beacuse you need to have a proper knowledge of python for this project, to resolve error, & queries, etc. So, best of luck for your project.!This project will be a great step into my whole projects career 


![image](https://github.com/user-attachments/assets/461667cd-eb3d-4e78-9c2b-44ed97a6aac6)


*Below is the folder structure. Your folder structure for Pycharm should resemble this, and also unzip the VOSK model file as specified in the structure*

So, today is the last day, and  I have successfully completed the Python Programming. The file of Python Programming is given in the Important Files > Program files > ( Here you will get the file ) 

Your folder in PyCharm should look like this :
```bash
YourProject/
├── bot.py                      ← This Python script
├── vosk-model-small-en-us-0.15/
└── (Docker running LibreTranslate)
```

Also, install these libraries for the Python Code:
```bash
pip install vosk pyttsx3 sounddevice requests
```


**Total time spent: 11h**

# June 1st: Writing the README.md & Designing 3D Model!

So, now Today is the last day and I will be designing the 3D Model for my Project, Now I have to choose the software that I will be using for designing like Blender, KiCAD, FreeCAD, etc, It's gonna be hard for me today,the lights are gone and my laptop's charging is only 30% so, without wasting time  let's start searching!

Now I tried 5 softwares the KiCAD was not good fit for me, and also the AutoCAD but, the 2 softwares FreeCAD & Blender are the perfect fit fot me beacuse I have been using Blender for 2 years and FreeCAD is just a beginning for me , so I will just see the videos for converting a Blender file into a FreeCAD file, so I am using blender for making the 3d model and using FreeCAD as a CAD Software beacuse Hack Club told that you need to include your CAD file, though Blender is not a CAD Software I am using FreeCAD.


So, after an intense search for the software I have chosen 2 softwares for  my project that are Blender & FreeCAD

![images](https://github.com/user-attachments/assets/0ae76cf4-5967-4503-8770-ea9912f327a6) &  ![download](https://github.com/user-attachments/assets/ad5630df-0911-49ba-b514-d9307ad97a46)

So now I am designing the 3D Model here are it's pics!

![gandr-collage](https://github.com/user-attachments/assets/6c80d18c-58b8-4603-a61b-f11cbdb58ca9)


and these both softwares are  free of cost! so enjoy making your project!

Now I am staring writing the README.md for my project, the lats step towards the end of my project.

It's 5:00 PM here and I am starting to write the readme of my project and also making some corrections in the Python Program and downloading images of 3D Model made in Blender & FreeCAD.

It's 7:45 PM and I have sucessfully completed writing the README.md and now finally Debugging the code.

It's 9:30 PM and I have sucessfully completed Debugging the code and also writing the README.md.

**Total time spent: 4.5h**

# Voila Your Project is Ready and your new Friend Too!

