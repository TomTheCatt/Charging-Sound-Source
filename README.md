# Charging Sound Source
The source code to the original program pre-packaged can be found [here](https://github.com/TomTheCatt/Charging-Sound). It is recommended that you download and install the packaged version as python 3 is not needed. If a bug or issue has been discovered, please post it in the previously mentioned link.

## **IMPORTANT NOTE**
A device running Windows 7 or higher is required. Extract all files from `.zip` file when downloaded. At times, a sound may not be played at all, which is due to Charging_Sound sleeping, thus conserving processing.

### Install
Download the program as a `.zip` folder and extract the contents. Find `install.pyw` and double-click it(or run as administrator to avoid prompts). Accept all prompts until none are asked. Find Windows Task Scheduler or press the windows button and "R"(win+R) and enter `taskschd.msc` to reach the Task Scheduler. Find a task labeled `Charging_Sound`. If it's status is "Queued" or similar, click "Run" on the right side of the window. You may test to see if Charging_Sound works by plugging in a charger and taking it out.

### Changing Sounds
Download your desired sound file. Copy and paste the file(or a preferred method) into the same file with `main.pyw`. If you intend to replace the sound played when charging, delete `charging_sound.wav` and rename your file `charging_sound.wav`. If you intend to replace the sound played when **not** charging, delete `not_charging_sound.wav` and rename your file `not_charging_sound.wav`

### Uninstall
Find `uninstall.pyw` and double-click it. Accept all prompts untill none are asked. You may access Windows Task Scheduler and double-check that the task named `Charging_Sound` is no longer present. You may now delete*all* contents related to `Charging_Sound`.

## Bugs
If the program is not working, check the directory in Windows Task Scheduler. Leave `/c python` in when replacing the paths.
