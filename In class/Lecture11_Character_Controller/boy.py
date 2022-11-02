from pico2d import *

#2 이벤트 정의
#RD, LD, RU, LU = 0, 1, 2, 3
RD, LD, RU, LU, TIMER, A = range(0,6)

#키입력 확인을 단순화 시켜서 이벤트로 해석
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN, SDLK_a): A
}


#1 상태 정의

class AUTO_RUN:
    def enter(self, event):    # 상태에 들어갈 때 행하는 액션
        print('ENTER AUTO_RUN')

    def exit(self):     # 상태를 나올 때 행하는 액션, 고개 들기
        print("EXIT AUTO_RUN")
        self.dir = 0

    def do(self):       # 상태에 있을 때 지속적으로 행하는 행위, 숨쉬기
        self.frame = (self.frame + 1) % 8
        if self.face_dir == 1:
            self.x += 1
        else:
            self.x -= 1

        if self.x > 800:
            self.face_dir = -1
        elif self.x < 0:
            self.face_dir = 1

    def draw(self):
        if self.face_dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y+50, 300,300)
        elif self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y+50,300,300)

class IDLE:
    def enter(self, event):    # 상태에 들어갈 때 행하는 액션
        print('ENTER IDLE')
        self.dir = 0
        self.timer = 1000

    def exit(self):     # 상태를 나올 때 행하는 액션, 고개 들기
        print("EXIT IDLE")

    def do(self):       # 상태에 있을 때 지속적으로 행하는 행위, 숨쉬기
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer == 0:
            self.add_event(TIMER) # 좀 더 객체지향적인 방법

    def draw(self):
            if self.face_dir == 1:
                self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
            else:
                self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)


class RUN:
    @staticmethod
    def enter(self, event):
        print("ENTER RUN")
        # 방향을 결정해야 하는데, 뭘 근거로? 어떤 키가 눌렸기 때문에?
        # 키 이벤트 정보가 필요
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

    @staticmethod
    def exit(self):
        print("EXIT RUN")
        self.face_dir = self.dir

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        # x 좌표를 변경, 달리기
        self.x += self.dir
        self.x = clamp(0, self.x, 800)

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)

class SLEEP:
    def enter(self, event):    # 상태에 들어갈 때 행하는 액션
        print('ENTER SLEEP')

    def exit(self):     # 상태를 나올 때 행하는 액션, 고개 들기
        print("EXIT SLEEP")

    def do(self):       # 상태에 있을 때 지속적으로 행하는 행위, 숨쉬기
        self.frame = (self.frame + 1) % 8

    def draw(self):
            if self.face_dir == -1:
                self.image.clip_composite_draw(self.frame * 100, 200, 100, 100,
                                               -3.141592 / 2, '', self.x + 25, self.y - 25, 100, 100)
            else: # 오른쪽 눕기
                self.image.clip_composite_draw(self.frame * 100, 300, 100, 100,
                                               -3.141592 / 2, '', self.x - 25, self.y - 25, 100, 100)



#3 상태 변환 기술
next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, A: AUTO_RUN},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, A: AUTO_RUN},
    SLEEP: {RD: RUN, LD: RUN, RU: RUN, LU: RUN, TIMER: SLEEP},
    AUTO_RUN: {RD: RUN, LD:RUN, RU: AUTO_RUN, LU:AUTO_RUN, A: IDLE}
}






class Boy:

    def add_event(self, event):
        self.q.insert(0, event)

    def handle_event(self, event):
        if(event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)


        # if event.type == SDL_KEYDOWN:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             boy.dir -= 1
        #         case pico2d.SDLK_RIGHT:
        #             boy.dir += 1
        # elif event.type == SDL_KEYUP:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             boy.dir += 1
        #             boy.face_dir = -1
        #         case pico2d.SDLK_RIGHT:
        #             boy.dir -= 1
        #             boy.face_dir = 1

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.q = [] #이벤트 큐 초기화
        self.cur_state = IDLE
        self.cur_state.enter(self, None) #초기 상태의 entry 액션 수행

    def update(self):
        self.cur_state.do(self) # 현재 상태의 do 액션 수행..

        #이벤트를 확인해서, 이벤트가 있으면 이벤트 변환 처리
        if self.q:  #큐에 이벤트가 있으면, 이벤트가 발생했으면
            event = self.q.pop()
            self.cur_state.exit(self) #현재 상태를 나가야 되고
            self.cur_state = next_state[self.cur_state][event] # 다음 상태를 구한다
            self.cur_state.enter(self, event) # 다음 상태의 entry action 수행



        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)

    def draw(self):
        self.cur_state.draw(self)

        # if self.dir == -1:
        #     self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        # elif self.dir == 1:
        #     self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        # else:
        #     if self.face_dir == 1:
        #         self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        #     else:
        #         self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
