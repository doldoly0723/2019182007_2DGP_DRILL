from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

def handle_events():
    global running
    global dir_x
    global dir_y
    # 키에 따른 frame 변화
    global frame
    global frame_y
    # 테두리 경계
    global x
    global y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                frame_y=1
                dir_x += 1
            elif event.key == SDLK_LEFT:
                frame_y = 0
                dir_x -= 1
            elif event.key == SDLK_UP:
                if frame_y == 2:
                    frame_y = 0
                elif frame_y == 3:
                    frame_y = 1
                dir_y += 1
            elif event.key == SDLK_DOWN:
                if frame_y == 2:
                    frame_y = 0
                elif frame_y == 3:
                    frame_y = 1
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
                frame_y = 3
            elif event.key == SDLK_LEFT:
                dir_x += 1
                frame_y = 2
            elif event.key == SDLK_UP:
                if frame_y == 0:
                    frame_y = 2
                elif frame_y == 1:
                    frame_y = 3
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                if frame_y == 0:
                    frame_y = 2
                elif frame_y == 1:
                    frame_y = 3
                dir_y += 1

open_canvas()
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
y = 90
# 행 프레임
frame = 0
# 열 프레임
frame_y = 3
dir_x = 0
dir_y = 0

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, frame_y * 100, 100, 100, x, y)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8

    if x >750:
        x=745
    elif x < 50:
        x = 55
    elif y > 550:
        y=545
    elif y <50:
        y = 55
    x += dir_x*5
    y += dir_y*5
    delay(0.01)

close_canvas()

