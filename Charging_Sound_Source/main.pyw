import psutil, time, os
from playsound import playsound
from xml.etree import ElementTree

main_direc = __file__
main_name = os.path.basename(main_direc)

def loop():
    while True:
        try:
            powered, filepath = psutil.sensors_battery().power_plugged, f"{os.getcwd()}\\text.txt"
            print(os.getcwd())
            #Opens file -- cannot use "with" as it is incompatable with other "with" functions.
            with open(filepath, "r") as file:
                file = file.readline()
            if "False" in str(file) and powered == True:
                with open(filepath, "w") as file_x:
                    file_x.write("True")
                    playsound(f"{os.getcwd()}\\charging_sound.wav")
            elif "True" in str(file) and powered == False:
                with open(filepath, "w") as file_x:
                    file_x.write("False")
                    playsound(f"{os.getcwd()}\\not_charging_sound.wav")
            #time.sleep(0.00001)
        except Exception as ex:
            break

if __name__ == "__main__":
    loop()
