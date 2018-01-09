# ZeusBot
ZeusBot is written in Python 2.7   

[![Discord](https://img.shields.io/badge/Chat-%20on%20Discord-738bd7.svg?style=flat-square)](https://discord.gg/EZNjh7t) 
[![issues](https://img.shields.io/github/issues/OlympicCode/vHackAPI-Python.svg?style=flat-square&raw=true)](http://gitlab.atvg-studios.at/root/ZeusBot/issue)
[![buildstatus](http://gitlab.atvg-studios.at/root/ZeusBot/badges/dev-2.x/build.svg)](http://gitlab.atvg-studios.at/root/ZeusBot/commits/dev-2.x)


[![DiscordBig](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRqIgbcCpiwO-V04gZWfGRZl-qrmIbgKXZtHCDjhV9nF_l3tD0g9w)](https://discord.gg/EZNjh7t)

[Official Database OlympicCode ](https://vhack.olympiccode.ga/)  
thanks to [@checkium](https://github.com/checkium)!

Minimal Configuration required  
  
- CPU i3, i5, ARM64, 4 thread Minimum or (4 core for amd).  
- Ram 128Mo.  
- OS: Windows 7, Win10,  Linux ALL version, Android 4.4 or Higher.  
- Network speed: ADSL Minimal (100ko/s for download).


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

