from pico2d import *
import math

open_canvas()
character = load_image('character.png')
grass = load_image('grass.png')

while(True):
    rect=0
    cir=0
    x=400
    y=90
    seta_x=0
    seta_y=180

    while(cir<1):
        while(seta_x<360):
            xpos = 400 + math.sin(seta_x/360*2*math.pi)*100
            ypos = 190 + math.cos(seta_y/360*2*math.pi)*100
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(xpos,ypos)
            seta_x+=2
            seta_y+=2
            delay(0.01)
        cir+=1
    while(rect<1):
        while x<780:
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            x=x+2
            delay(0.01)
        while y<560:
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            y=y+2
            delay(0.01)
        while x>20:
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            x=x-2
            delay(0.01)
        while y>90:
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            y=y-2
            delay(0.01)
        while x<400:
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            x=x+2
            delay(0.01)
        cir=0
        rect+=1




close_canvas()
