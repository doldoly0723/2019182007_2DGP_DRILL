import game_framework
from pico2d import *
import play_state
import title_state

# fill here
# running = True
image = None
logo_time = 0.0

def enter():
    global image
    image = load_image('tuk_credit.png')
    # fill here
    pass

def exit():
    global image
    del image
    # fill here
    pass

def update():
    # logo time을 계산하고, 그 결과에 따라 1초가 넘으면 running = False
    global logo_time
    delay(0.01)
    logo_time += 0.01
    if logo_time >= 0.5:
        logo_time = 0
        game_framework.change_state(title_state)
    # fill here
    pass

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()
    # fill here
    pass

def handle_events():
    events = get_events()





