# Charging Sound Source
The source code to the original program pre-packaged can be found here. It is recommended that you download and install the packaged version found [here](https://github.com/TomTheCatt/Charging-Sound). If a bug or issue has been discovered, please post it in the previously mentioned link.

## Install
# Step 1
Download through Github and run `install.pyw` in the file's directory. Accept all permissions asked until none are asked.

## Changing Sounds
### Step 1
Find and download the sound you desire. Change the file's extension to `.wav`.

### Step 2
Bring the file into the program's directory(with `install.pyw`, `main.pyw`, and `uninstall.pyw`).

If you want to replace the charging sound, delete `charging_sound.wav` and rename your new file(and it's extension) `charging_sound.wav`.

If you want to replace the disconnection sound, delete `not_charging_sound.wav` and rename your new file(and it's extension) `not_charging_sound.wav`.

Both files must remain in the same directory as `main.pyw`(along with `install.pyw` and `uninstall.pyw`), otherwise an error will be given. If you want no sound to be played, you can uninstall the program, or set one sound file to silence and the other to the desired sound.

## Uninstall
### Step 1
Run `uninstall.pyw` in the file's directory. Accept all permissions until none are asked.
