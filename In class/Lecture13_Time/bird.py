from pico2d import*
import random
import game_framework

#Bird fly Speed
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 30.0           #Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

#Bird Action Speed
TIME_PER_ACTION = 0.7
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class Bird:
    def __init__(self):
        self.x = random.randint(100, 1500)
        self.y = random.randint(400, 500)
        self.dir = 1
        self.frame = 0
        self.frame_x = 0
        self.frame_y = 0

        self.image = load_image('bird_animation.png')
    def update(self):
        if self.x < 50:
            self.dir = 1
        elif self.x > 1550:
            self.dir = -1

        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14

        if 0 <= self.frame < 5:
            self.frame_x = 0
            self.frame_y = 2
        elif 5 <= self.frame < 10:
            self.frame_x = 5
            self.frame_y = 1
        elif 10 <= self.frame:
            self.frame_x = 10
            self.frame_y = 0

    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw((int(self.frame)-self.frame_x) * 183, 168 * self.frame_y, 183, 168,
                                           0, '', self.x, self.y, 30, 30)
        else:
            self.image.clip_composite_draw((int(self.frame)-self.frame_x) * 183, 168 * self.frame_y, 183, 168,
                                           3.141592, 'v', self.x, self.y, 30, 30)
