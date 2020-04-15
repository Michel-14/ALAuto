# ALAuto
Updated and semi-rewritten version of [azurlane-auto](https://github.com/perryhuynh/azurlane-auto).  
Automates Combat, Commissions, Missions, Enhancement, Retiring, Skill Levelling, Dorm Refilling and Dorm Cleaning.

**This bot was made for EN server. However, it's now possible to use it on JP thanks to [@phantasmalmira](https://github.com/phantasmalmira) ([#59](https://github.com/Egoistically/ALAuto/pull/59)). Other servers won't work with current assets.**

## Requirements on Windows
* Python 3.7.X installed and added to PATH.
* Latest [ADB](https://developer.android.com/studio/releases/platform-tools) added to PATH.
* ADB debugging enabled emulator with **1920x1080 resolution** and **Android 5 or newer**.

Tested on Windows 10 with BlueStacks and Nox, [don't use Nox though](https://www.reddit.com/r/noxappplayer/comments/cz2133/segurazo_malware_with_nox_player/).

## Installation and Usage
1. Clone or download this repository.
2. Install the required packages via `pip3` with the command `pip3 install -r requirements.txt`.
3. Enable adb debugging on your emulator, on Nox you might also need to enable root.
4. Change config.ini's IP:PORT to 127.0.0.1 and your emulator's adb port, then change the rest to your likings. If you are using your own phone/device for the bot, enable debbuging on your device and change IP:PORT to your device's name (obtainable through this adb command `adb devices -l`).
5. Run `ALAuto` using the command `python ALAuto.py` from the bot main directory.

Check the [Wiki](https://github.com/Egoistically/ALAuto/wiki/Config.ini-and-Modules-explanation) for more information. It's my first time making one, don't mind me.  

## Relevant information
* CPU usage might spike a bit when searching for enemies and boss.
* If you'd like to disable `oil limit` or `retreat after` set them to `0`.
* If you wish to view a changelog, check the [commit history](https://github.com/Egoistically/ALAuto/commits/master).
* If you'd like to help us during events to release an update faster you can check [this guide](https://github.com/Egoistically/ALAuto/wiki/Creating-new-assets-for-bot).

This was made for my own usage, it is far from good and I'm very aware of it. I am posting this because it might be useful to someone, that's all.  
If you'd like to contribute in any way make sure to open a [pull request](https://github.com/Egoistically/ALAuto/pulls) or an [issue](https://github.com/Egoistically/ALAuto/issues). If you'd like to contact us you can do so through our [Discord](https://discord.gg/vCFxDen).

## Fork Features

* Ascreencap shared folder support for Memu and BlueStacks, other emulators and phones can use the old adb screencap
* Ascreencap is installed automatically when first starting AlAuto
* preview 720p screen resolution support, note that some assets are missing(replaced by 1080p ones for the time being), list below:

```
Missing assets:
maps/map_E-A1 - E-SP5
research/12h, 30m
```

There are 2 new entries in the config.ini:

**Emulator**: 
the name of the emulator, either `Memu` or `BlueStacks`
Leave this field empty for other emulators or phones, it will use the old adb screencap.

**SharedFolderpath**: 
the complete path of memu or bluestacks shared folder, by default:
BlueStacks = `C:\ProgramData\BlueStacks\Engine\UserData\SharedFolder\`
Memu = `C:\Users\yourUsername\Downloads\MEmu Download\`

