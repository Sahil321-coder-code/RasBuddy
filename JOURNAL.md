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

   ![Screenshot 2025-05-29 090920](https://github.com/user-attachments/assets/dbe9520b-719e-4b50-9476-25c67784cc9e)
   ![Screenshot 2025-05-29 091201](https://github.com/user-attachments/assets/a8cdb03f-1d8e-487b-b8e6-5aa9c7ed2e48)

I have got the software and they are all free! So, that's great news, and now I will be configuring the software as per the project requirements, and setting them up!

Now after I have doen the setup and Configured the softwares as per the requirements now tomorrow I will be writing the python program.
So, the software I have chosen is 💻:

 1. Raspberry Pi Imager.

![Screenshot 2025-06-17 150841](https://github.com/user-attachments/assets/e17b36ac-713b-42e5-993c-ee5e96134bf1)

 
 3. Python 3.7+

![image](https://github.com/user-attachments/assets/ad84a264-cf08-4589-9adb-76894905b943)


 4. PyCharm Community Edition

![image](https://github.com/user-attachments/assets/08a956b5-b86f-4704-9361-9171d5bfa715)

   
 6. Libraries: vosk, sounddevice, pyttsx3, argostranslate, requests, Pillow, Adafruit-SSD1306, etc.
     (Refer to instructions.txt )

![image](https://github.com/user-attachments/assets/a22aeefc-d90c-4331-8823-27c9c90ca5eb)


![image](https://github.com/user-attachments/assets/6b312600-d56f-4ce7-9ff7-576b62c82780)


The hardware and software I have chosen are completely free and are working perfect on Windows & Mac, so note the hardware and take it.Bye!!

**Total time spent: 6h**

# May 30th: Half Python Programming!

So, today we will be writing and installing the required softwares and apps, firts you are going to need Raspberry Pi Imager software and the details you are going to need for to put in the software are given 👇 below.


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
 
Congratulations you have successfully set up the Pi Imager

![Screenshot 2025-06-17 150354](https://github.com/user-attachments/assets/6aeba2e9-5a0e-46f0-8670-768fa0f5f025)

![Screenshot 2025-06-17 150451](https://github.com/user-attachments/assets/89f4b6ba-354f-4cad-b8ee-2bc7c8a94c0e)



If you are not getting the instructions, how to do it ,then click [here](https://drive.google.com/file/d/1qQF-NHXBG2cuox9VjBYXK5pml_ZQaf1B/view?usp=sharing)

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

![Screenshot 2025-06-17 150608](https://github.com/user-attachments/assets/d54fe157-622f-4631-80f3-224a463da592)


![Screenshot 2025-06-17 150550](https://github.com/user-attachments/assets/3d250fce-8e8d-4a2c-8722-e570d7c0cf84)


**Total time spent: 7h**

# May 31st: Python Programming Completed!

So, I have yesterday made the Python Programming but half and now I am completing it and also adding advaced features like Music, Time, Wetaher, etc.To know more features stay  tuned for the final prototype, it will be made if my project gets approved! And also make sure you are well known to python programming, beacuse you need to have a proper knowledge of python for this project, to resolve error, & queries, etc. So, best of luck for your project.!This project will be a great step into my whole projects career 


![image](https://github.com/user-attachments/assets/461667cd-eb3d-4e78-9c2b-44ed97a6aac6)


*Below is the folder structure. Your folder structure for Raspberry Pi Imager should resemble this, and also unzip the VOSK model file as specified in the structure*

So, today is the last day, and  I have successfully completed the Python Programming. The file of Python Programming is given in the Important Files > Program files > ( Here you will get the file ) 

Your folder in Raspberry Pi should look like this :
```bash
raspi-assistant/
├── assistant.py            # Final Python code
├── vosk-model/             # Extracted vosk model folder (e.g. vosk-model-small-en-us-0.15)
├── music/
│   └── song1.mp3           # Your music file
└── translate_model.argosmodel  # Optional: Argos Hindi-English model if offline

```
The code file is given in "assistant.py" in the important files, and also name the song you want as song1.mp3. The folder structure is given 

**Total time spent: 11h**

# June 1st: Writing the README.md & Designing 3D Model!

So, now Today is the last day and I will be designing the 3D Model for my Project, Now I have to choose the software that I will be using for designing like Blender, KiCAD, FreeCAD, etc, It's gonna be hard for me today,the lights are gone and my laptop's charging is only 30% so, without wasting time  let's start searching!

Now I tried 5 softwares the KiCAD was not good fit for me, and also the AutoCAD but, the 2 softwares FreeCAD & Blender are the perfect fit fot me beacuse I have been using Blender for 2 years and FreeCAD is just a beginning for me , so I will just see the videos for converting a Blender file into a FreeCAD file, so I am using blender for making the 3d model and using FreeCAD as a CAD Software beacuse Hack Club told that you need to include your CAD file, though Blender is not a CAD Software I am using FreeCAD.


So, after an intense search for the software I have chosen 2 softwares for  my project that are Blender & FreeCAD

![images](https://github.com/user-attachments/assets/0ae76cf4-5967-4503-8770-ea9912f327a6) &  ![download](https://github.com/user-attachments/assets/ad5630df-0911-49ba-b514-d9307ad97a46)

So now I am designing the 3D Model here are it's pics!

![Web_Photo_Editor](https://github.com/user-attachments/assets/675ffecb-1269-4aae-b113-db4bb5b49e6a)

and these both softwares are  free of cost! so enjoy making your project!

Now I am staring writing the README.md for my project, the lats step towards the end of my project.

It's 5:00 PM here and I am starting to write the readme of my project and also making some corrections in the Python Program and downloading images of 3D Model made in Blender & FreeCAD.

It's 7:45 PM and I have sucessfully completed writing the README.md and now finally Debugging the code.

It's 9:30 PM and I have sucessfully completed Debugging the code and also writing the README.md.

**Total time spent: 4.5h**

# Voila Your Project is Ready and your new Friend Too!

