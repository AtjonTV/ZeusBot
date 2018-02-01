# ZeusBot
ZeusBot is a bot that can play the moblie game vHackXT, the bot is written in Python 2.7, and can run on nearly any system that hase Python 2.7 and the requirements installed.

[Here](https://steemit.com/atvgstudios/@atjontv/zeusbot-vhackxt) is a Steemit Post about ZeusBot

**[Disclaimer: ZeusBot is based on [OlympicCode](https://olympiccode.net/)'s project "[vHackXTBot-Python](https://github.com/OlympicCode/vHackXTBot-Python)".]**

[![Discord](https://img.shields.io/badge/Chat-%20on%20Discord-738bd7.svg?style=flat-square)](https://discord.gg/EZNjh7t) 
[![pipeline status](https://gitlab.atvg-studios.at/root/ZeusBot/badges/dev-2.x/pipeline.svg)](https://gitlab.atvg-studios.at/root/ZeusBot/commits/dev-2.x)
[![coverage report](https://gitlab.atvg-studios.at/root/ZeusBot/badges/dev-2.x/coverage.svg)](https://gitlab.atvg-studios.at/root/ZeusBot/commits/dev-2.x)

Minimal Configuration required  
  
- CPU i3, i5, ARM64, 4 thread Minimum or (4 core for amd).  
- Ram 128MB.  
- OS: Windows 7, Win10,  Linux ALL version, Android 4.4 or Higher.  
- Network speed: ADSL Minimal (100ko/s for download).

System test Results

| Hardware      | Software      | Bots   | CPU Usage  | RAM  Usage | Reccomented?
| ------------- |:-------------:|:------:|:-----:|:-----:|:-----:|
| Raspberry Pi 3 Model B | Raspbian 9.3 (Python 2.7.13) | 5 | 5% | ~80MB | Yes (Cheap)[30$]
| HP ProBook 470 G3 | ElementaryOS 0.4.1 (Python 2.7.15)| 1 | 0.01% | ~16MB | No (Pricie)[1500$]
| Google Cloud Micro-Instance | Ubuntu 16.04 (Python 2.7.13) | 2 | 0.05% | - | No (Pricie)[40$/Month]


Hostings

| Hoster | Price ($ and €)| Duration | Max Bots per Customer| Used Bots
| --------|:---------:|:--------:|:-------:|:-------:|
|ATVG-Studios Private Hosting| 60 | one year | 1 | 1/10
|ATVG-Studios| 5 | one month | 10 | 4/200
|BeeIT| 5 | one month | 10 | 0/200
|XerxezZ| 10 | one month | 20 | 0/400

How to get a host?  
The only way is to contact AtjonTV @ ATVG-Studios to get him make a connection to one of the listed Hosts, he will take in your money, give it to the host and manage your bot on thair system.

AtjonTV's Mail:
<admin.atjontv@atvg-studios.at>


Possible Payment methods:  
* Credit Card
* PayPal
* PaySafeCard
* Skrill

Function
- Update your Account Firewall / IPSP / CPU / Ram ect...
- Remove Spyware if detecting in the account
- Attack the with botnet
- Attack for console Target and detect for FBI
- Help for tournament to get first place
- Run in Multi-Processing for more stability and fast (Linux) / Windows is scalable
- Two attack modes, Patator or Secure
- it's the number 1 bot for vHackXT
- detected if you are blocked on the api vHackXT and waiting (~5 Minutes)
- Auto update Botnet 
- Chat resolve cluster name (execute : python chat.py in linux and just run chat.exe for windows)  
(Windows no support all charset in the chat :( ) 
  
Edit line 3 and 4 in config.py
Enter your login details  
> user = ""
> password = ""  

Linux Exclusive Database and multiprocessing **(file database is database.txt in your directory)**

External dependencies you'll need include:
- requests
- Pillow

 
 
To install the bot on Linux:  

### You can find installation scripts at [ZeusBot-Install](http://gitlab.atvg-studios.at/root/ZeusBot-Installer)  

### Installing on Android  
#### (I serve no help for android.)

Install Pillow on Android 6.x    
>$ pkg install python python-dev libjpeg-turbo-dev ndk-sysroot clang  
>$ python -m pip install wheel  
>$ LDFLAGS="-L/system/lib/" CFLAGS="-I/data/data/com.termux/files/usr/include/"  python -m pip install pillow    
>$ python -m pip install request   
>$ python -m pip install futures   

start for Android 6.x  
>$ python main.py  

Install Pillow on Android 7.x  
>$ pkg install python python-dev libjpeg-turbo-dev ndk-sysroot clang  
>$ python2 -m pip install wheel  
>$ LDFLAGS="-L/system/lib/" CFLAGS="-I/data/data/com.termux/files/usr/include/"  python2 -m pip install pillow    
>$ python2 -m pip install request  
>$ python2 -m pip install futures  

start for 7.x  
>$ python2 main.py 

**New Mode Available !**  
"**Potator**" or "**Secure**" on line 39 in main.py (edit line)

**Potator**    
```   
Potator mode It will not examine firewall or stealth mode it will attack anything
that can with any criteria perfect for tournaments
```

**Secure**  
```
Protects against attack back or you tell yourself  
the least to secure it verifying that you are
```

Result:  
![](http://www.cuby-hebergs.com/dl/vhack.png)

