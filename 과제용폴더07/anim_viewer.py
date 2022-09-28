from pico2d import *
open_canvas()
character = load_image('spritesheet.png')

# x 165 y 293
frame = 0
frame_select=2
# frame 순서(2~6)
def frame_clip(frame_n,num):
    clear_canvas()
    character.clip_draw(frame_n*165,293*num,165,293,x,150)
    update_canvas()

for x in range(0,800+1,5):
    frame_clip(frame,frame_select)
    if frame == 11:
        frame_select+=1
        frame=0
        if frame_select==7:
            frame_select=2
    else:
        frame = (frame+1)%12
    delay(0.05)
    get_events()


close_canvas()