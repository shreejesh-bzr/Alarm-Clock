import datetime
import time
from playsound import playsound

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("⏰ Alarm ringing!")
            playsound("alarm.wav")
            break
        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)
