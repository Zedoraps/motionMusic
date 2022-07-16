from datetime import datetime
from gpiozero import MotionSensor


class Motion:

    def __init__(self):
        self.motion = False
        self.sens = MotionSensor(4)

        self.sens.when_motion = self.on_motion
        self.sens.when_no_motion = self.on_no_motion

    def on_motion(self):
        self.motion = True
        print(f'{datetime.now().strftime("%H:%M:%S")}: Motion Detected')

    def on_no_motion(self):
        self.motion = False
        print(f'{datetime.now().strftime("%H:%M:%S")}: Motion Ended')
