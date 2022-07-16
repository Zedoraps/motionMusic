from datetime import datetime
from signal import pause

from gpiozero import MotionSensor


class Motion:

    def __init__(self):
        self.sens = MotionSensor(4)

        self.sens.when_motion = self.on_motion
        self.sens.when_no_motion = self.on_no_motion

    def write(self, status):
        with open('status.txt', 'w') as f:
            f.writelines(f"{datetime.now()}: {status}\n")

    def on_motion(self):
        self.write(True)
        print(f'{datetime.now().strftime("%H:%M:%S")}: Motion Detected')

    def on_no_motion(self):
        self.write(False)
        print(f'{datetime.now().strftime("%H:%M:%S")}: Motion Ended')


