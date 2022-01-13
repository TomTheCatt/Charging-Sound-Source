import psutil, time, os
from playsound import playsound
from xml.etree import ElementTree
from pathlib import Path

main_name = Path(__file__).stem
main_ext = ".exe"
main_direc = os.getcwd()

#print(main_direc, main_name, main_ext)

def detect_battery():
    is_powered = psutil.sensors_battery().power_plugged
    #Checks if power is on. If it is, it will play a sound("charging_sound.wav")
    global first_time
    global powered_currently
    if powered_currently != is_powered:
        try:
            del first_time
            powered_currently = is_powered
            return
        except:
            #Corrects powered_currently to the value of is_powered
            powered_currently = is_powered
            playsound(f"{os.getcwd()}\\charging_sound.wav") if is_powered == True else playsound(f"{os.getcwd()}\\not_charging_sound.wav")

def start():
    global first_time
    global powered_currently
    first_time, powered_currently = None, False
    #Loops infinately
    while True:
        det = 0
        #Loops for about two minutes.
        for i in range(240):
            detect_battery()
            time.sleep(0.5)
        #Rests for one minute before repeating
        time.sleep(60)

if __name__ == "__main__":
    start()
