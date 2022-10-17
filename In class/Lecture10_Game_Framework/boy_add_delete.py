import game_framework
from pico2d import *
import play_state
import title_state

# fill here
# running = True
image = None


def enter():
    global image
    image = load_image('add_delete_boy.png')
    # fill here
    pass

def exit():
    global image
    del image
    # fill here
    pass

def update():
    play_state.update()
    pass

def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(400, 300)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:    #이전 상태인 play_state로 복귀
                    game_framework.pop_state()
                case pico2d.SDLK_j:
                    if len(play_state.team) > 1:
                        del play_state.team[len(play_state.team)-1]
                    game_framework.pop_state()
                    #game_framework.change_state(play_state)
                case pico2d.SDLK_k:
                    play_state.team += [play_state.Boy()]
                    game_framework.pop_state()
                    #game_framework.change_state(play_state)








