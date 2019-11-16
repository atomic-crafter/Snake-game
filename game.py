import pygame
import random
import math
from tkinter import * 
from pygame.locals import *

pygame.init()
#Define tkinter
x = 220
y = 220
x2=x
x3=x
x4=x
x5=x
x6=x
x7=x
x8=x
x9=x
x10=x
x11=x
x12=x
x13=x
x14=x
x15=x
x16=x
x17=x
x18=x
x19=x
x20=x
y2=y
y3=y
y4=y
y5=y
y6=y
y7=y
y8=y
y9=y
y10=y
y11=y
y12=y
y13=y
y14=y
y15=y
y16=y
y17=y
y18=y
y19=y
y20=y
window= Tk()
#Define functions

def len():
    global x,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,y,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20
    x20=x19
    x19=x18
    x18=x17
    x17=x16
    x16=x15
    x15=x14
    x14=x13
    x13=x12
    x12=x11
    x11=x10
    x10=x9
    x9=x8
    x8=x7
    x7=x6
    x6=x5
    x5=x4
    x4=x3
    x3=x2
    x2=x
    y20=y19
    y19=y18
    y18=y17
    y17=y16
    y16=y15
    y15=y14
    y14=y13
    y13=y11
    y12=y11
    y11=y10
    y10=y9
    y9=y8
    y8=y7
    y7=y6
    y6=y5
    y5=y4
    y4=y3
    y3=y2
    y2=y
def restrart():
    global window
    window.quit()
    main()
def game_quit():
    global window
    pygame.quit()
    window.quit()
def game_over():
    global window,score
    print("krvarrr")
    run=False
    #tkinter window settings

    window.title("You lose")
    window.geometry("200x70")
    window.configure(background = "white")
    Label(window, text= "You lose", fg = "black" , bg = "white", font="comicsamsms 15 italic").grid(row = 0 , column = 1, sticky = W)
    #Label(window, text= (str(score)+"points"), fg = "black" , bg = "white", font="comicsamsms 15 bold").grid(row = 0 , column = 2, sticky = W)
    Button(window, text = "Try again", width = 6, command = restrart) .grid(row = 2, column = 2, sticky = W)
    Button(window, text = "Quit", width = 6, command = game_quit) .grid(row = 2, column = 1, sticky = W)
    window.mainloop()
def roundup(x):
        if x%20==0:
            return x
        else:
            return x-(x%20)
#main function

def main():
    #pos variables
    global x,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,y,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20
    
    xRandom = random.randint(65,390)
    yRandom = random.randint(65,390)
    xRandom = roundup(xRandom)
    yRandom = roundup(yRandom)
    x=roundup(x)
    y=roundup(y)

    #other variables

    score = 0
    i=0
    uptime = 1+(score/10)
    win = pygame.display.set_mode((500,500))
    text = ("Score:"+str(score))
    width = 20
    height = 20
    speed =20
    rows = 60
    lp = None
    run = True
    r = 255
    g = 0
    b = 0
    yiv =int(380/width)
    myfont = pygame.font.SysFont('Comic Sans MS', 16)
    Tyfont = pygame.font.SysFont('Comic Sans MS', 50)
    #pygame setup

    
    pygame.display.set_caption("Cool game")
    
    #main loop

    while run:
        #Clear window
        
        i+=1
        if i == 2:
            win.fill((0,0,0))
            i=0
        #variable setups

        rows = 60
        xRandom = roundup(xRandom)
        yRandom = roundup(yRandom)

        #ScoreBoard

        score_text = myfont.render("Score: ", True, (255,255,255))
        win.blit(score_text, (10, 10))
        final_text = myfont.render(str(score), True, (255,255,255))
        win.blit(final_text, (60, 10))
        Title_text = Tyfont.render("Snake Game", True, (0,255,0))
        win.blit(Title_text, (120, 1))
        #pygame setup

        pygame.draw.rect(win,(255,0,255),(xRandom,yRandom, width,height))
        pygame.time.delay(100)
        
        
        #lenght control

        if score<=4:
            len()
            pygame.draw.rect(win,(r,g,b),(x,y,width,height))
            pygame.draw.rect(win,(r,g,b),(x2,y2,width,height))
            pygame.draw.rect(win,(r,g,b),(x3,y3,width,height))
            pygame.draw.rect(win,(r,g,b),(x4,y4,width,height))
        elif score==5:
            len()
            pygame.draw.rect(win,(r,g,b),(x,y,width,height))
            pygame.draw.rect(win,(r,g,b),(x2,y2,width,height))
            pygame.draw.rect(win,(r,g,b),(x3,y3,width,height))
            pygame.draw.rect(win,(r,g,b),(x4,y4,width,height))
            pygame.draw.rect(win,(r,g,b),(x5,y5,width,height))
        elif score==6:
            len()
            pygame.draw.rect(win,(r,g,b),(x,y,width,height))
            pygame.draw.rect(win,(r,g,b),(x2,y2,width,height))
            pygame.draw.rect(win,(r,g,b),(x3,y3,width,height))
            pygame.draw.rect(win,(r,g,b),(x4,y4,width,height))
            pygame.draw.rect(win,(r,g,b),(x5,y5,width,height))
            pygame.draw.rect(win,(r,g,b),(x6,y6,width,height))
        elif score==7:
            len()
            pygame.draw.rect(win,(r,g,b),(x,y,width,height))
            pygame.draw.rect(win,(r,g,b),(x2,y2,width,height))
            pygame.draw.rect(win,(r,g,b),(x3,y3,width,height))
            pygame.draw.rect(win,(r,g,b),(x4,y4,width,height))
            pygame.draw.rect(win,(r,g,b),(x5,y5,width,height))
            pygame.draw.rect(win,(r,g,b),(x6,y6,width,height))
            pygame.draw.rect(win,(r,g,b),(x5,y5,width,height))
            pygame.draw.rect(win,(r,g,b),(x6,y6,width,height))
            pygame.draw.rect(win,(r,g,b),(x7,y7,width,height))
        elif score==8:
            len()
            pygame.draw.rect(win,(r,g,b),(x,y,width,height))
            pygame.draw.rect(win,(r,g,b),(x2,y2,width,height))
            pygame.draw.rect(win,(r,g,b),(x3,y3,width,height))
            pygame.draw.rect(win,(r,g,b),(x4,y4,width,height))
            pygame.draw.rect(win,(r,g,b),(x5,y5,width,height))
            pygame.draw.rect(win,(r,g,b),(x6,y6,width,height))
            pygame.draw.rect(win,(r,g,b),(x7,y7,width,height))
            pygame.draw.rect(win,(r,g,b),(x8,y8,width,height))
        elif score==9:
            len()
            pygame.draw.rect(win,(r,g,b),(x,y,width,height))
            pygame.draw.rect(win,(r,g,b),(x2,y2,width,height))
            pygame.draw.rect(win,(r,g,b),(x3,y3,width,height))
            pygame.draw.rect(win,(r,g,b),(x4,y4,width,height))
            pygame.draw.rect(win,(r,g,b),(x5,y5,width,height))
            pygame.draw.rect(win,(r,g,b),(x6,y6,width,height))
            pygame.draw.rect(win,(r,g,b),(x7,y7,width,height))
            pygame.draw.rect(win,(r,g,b),(x8,y8,width,height))
            pygame.draw.rect(win,(r,g,b),(x9,y9,width,height))
        elif score==10:
            len()
            pygame.draw.rect(win,(r,g,b),(x,y,width,height))
            pygame.draw.rect(win,(r,g,b),(x2,y2,width,height))
            pygame.draw.rect(win,(r,g,b),(x3,y3,width,height))
            pygame.draw.rect(win,(r,g,b),(x4,y4,width,height))
            pygame.draw.rect(win,(r,g,b),(x5,y5,width,height))
            pygame.draw.rect(win,(r,g,b),(x6,y6,width,height))
            pygame.draw.rect(win,(r,g,b),(x7,y7,width,height))
            pygame.draw.rect(win,(r,g,b),(x8,y8,width,height))
            pygame.draw.rect(win,(r,g,b),(x9,y9,width,height))
            pygame.draw.rect(win,(r,g,b),(x10,y10,width,height))
        elif score==11:
            len()
            pygame.draw.rect(win,(r,g,b),(x,y,width,height))
            pygame.draw.rect(win,(r,g,b),(x2,y2,width,height))
            pygame.draw.rect(win,(r,g,b),(x3,y3,width,height))
            pygame.draw.rect(win,(r,g,b),(x4,y4,width,height))
            pygame.draw.rect(win,(r,g,b),(x5,y5,width,height))
            pygame.draw.rect(win,(r,g,b),(x6,y6,width,height))
            pygame.draw.rect(win,(r,g,b),(x7,y7,width,height))
            pygame.draw.rect(win,(r,g,b),(x8,y8,width,height))
            pygame.draw.rect(win,(r,g,b),(x9,y9,width,height))
            pygame.draw.rect(win,(r,g,b),(x10,y10,width,height))
            pygame.draw.rect(win,(r,g,b),(x11,y11,width,height))
        elif score==12:
            len()
            pygame.draw.rect(win,(r,g,b),(x,y,width,height))
            pygame.draw.rect(win,(r,g,b),(x2,y2,width,height))
            pygame.draw.rect(win,(r,g,b),(x3,y3,width,height))
            pygame.draw.rect(win,(r,g,b),(x4,y4,width,height))
            pygame.draw.rect(win,(r,g,b),(x5,y5,width,height))
            pygame.draw.rect(win,(r,g,b),(x6,y6,width,height))
            pygame.draw.rect(win,(r,g,b),(x7,y7,width,height))
            pygame.draw.rect(win,(r,g,b),(x8,y8,width,height))
            pygame.draw.rect(win,(r,g,b),(x9,y9,width,height))
            pygame.draw.rect(win,(r,g,b),(x10,y10,width,height))
            pygame.draw.rect(win,(r,g,b),(x11,y11,width,height))
            pygame.draw.rect(win,(r,g,b),(x12,y12,width,height))
        elif score==13:
            len()
            pygame.draw.rect(win,(r,g,b),(x,y,width,height))
            pygame.draw.rect(win,(r,g,b),(x2,y2,width,height))
            pygame.draw.rect(win,(r,g,b),(x3,y3,width,height))
            pygame.draw.rect(win,(r,g,b),(x4,y4,width,height))
            pygame.draw.rect(win,(r,g,b),(x5,y5,width,height))
            pygame.draw.rect(win,(r,g,b),(x6,y6,width,height))
            pygame.draw.rect(win,(r,g,b),(x7,y7,width,height))
            pygame.draw.rect(win,(r,g,b),(x8,y8,width,height))
            pygame.draw.rect(win,(r,g,b),(x9,y9,width,height))
            pygame.draw.rect(win,(r,g,b),(x10,y10,width,height))
            pygame.draw.rect(win,(r,g,b),(x11,y11,width,height))
            pygame.draw.rect(win,(r,g,b),(x12,y12,width,height))
            pygame.draw.rect(win,(r,g,b),(x13,y13,width,height))
        elif score==14:
            len()
            pygame.draw.rect(win,(r,g,b),(x,y,width,height))
            pygame.draw.rect(win,(r,g,b),(x2,y2,width,height))
            pygame.draw.rect(win,(r,g,b),(x3,y3,width,height))
            pygame.draw.rect(win,(r,g,b),(x4,y4,width,height))
            pygame.draw.rect(win,(r,g,b),(x5,y5,width,height))
            pygame.draw.rect(win,(r,g,b),(x6,y6,width,height))
            pygame.draw.rect(win,(r,g,b),(x7,y7,width,height))
            pygame.draw.rect(win,(r,g,b),(x8,y8,width,height))
            pygame.draw.rect(win,(r,g,b),(x9,y9,width,height))
            pygame.draw.rect(win,(r,g,b),(x10,y10,width,height))
            pygame.draw.rect(win,(r,g,b),(x11,y11,width,height))
            pygame.draw.rect(win,(r,g,b),(x12,y12,width,height))
            pygame.draw.rect(win,(r,g,b),(x13,y13,width,height))
            pygame.draw.rect(win,(r,g,b),(x14,y14,width,height))
        elif score==15:
            len()
            pygame.draw.rect(win,(r,g,b),(x,y,width,height))
            pygame.draw.rect(win,(r,g,b),(x2,y2,width,height))
            pygame.draw.rect(win,(r,g,b),(x3,y3,width,height))
            pygame.draw.rect(win,(r,g,b),(x4,y4,width,height))
            pygame.draw.rect(win,(r,g,b),(x5,y5,width,height))
            pygame.draw.rect(win,(r,g,b),(x6,y6,width,height))
            pygame.draw.rect(win,(r,g,b),(x7,y7,width,height))
            pygame.draw.rect(win,(r,g,b),(x8,y8,width,height))
            pygame.draw.rect(win,(r,g,b),(x9,y9,width,height))
            pygame.draw.rect(win,(r,g,b),(x10,y10,width,height))
            pygame.draw.rect(win,(r,g,b),(x11,y11,width,height))
            pygame.draw.rect(win,(r,g,b),(x12,y12,width,height))
            pygame.draw.rect(win,(r,g,b),(x13,y13,width,height))
            pygame.draw.rect(win,(r,g,b),(x14,y14,width,height))
            pygame.draw.rect(win,(r,g,b),(x15,y15,width,height))
        elif score==16:
            len()
            pygame.draw.rect(win,(r,g,b),(x,y,width,height))
            pygame.draw.rect(win,(r,g,b),(x2,y2,width,height))
            pygame.draw.rect(win,(r,g,b),(x3,y3,width,height))
            pygame.draw.rect(win,(r,g,b),(x4,y4,width,height))
            pygame.draw.rect(win,(r,g,b),(x5,y5,width,height))
            pygame.draw.rect(win,(r,g,b),(x6,y6,width,height))
            pygame.draw.rect(win,(r,g,b),(x7,y7,width,height))
            pygame.draw.rect(win,(r,g,b),(x8,y8,width,height))
            pygame.draw.rect(win,(r,g,b),(x9,y9,width,height))
            pygame.draw.rect(win,(r,g,b),(x10,y10,width,height))
            pygame.draw.rect(win,(r,g,b),(x11,y11,width,height))
            pygame.draw.rect(win,(r,g,b),(x12,y12,width,height))
            pygame.draw.rect(win,(r,g,b),(x13,y13,width,height))
            pygame.draw.rect(win,(r,g,b),(x14,y14,width,height))
            pygame.draw.rect(win,(r,g,b),(x15,y15,width,height))
            pygame.draw.rect(win,(r,g,b),(x16,y16,width,height))
        elif score==17:
            len()
            pygame.draw.rect(win,(r,g,b),(x,y,width,height))
            pygame.draw.rect(win,(r,g,b),(x2,y2,width,height))
            pygame.draw.rect(win,(r,g,b),(x3,y3,width,height))
            pygame.draw.rect(win,(r,g,b),(x4,y4,width,height))
            pygame.draw.rect(win,(r,g,b),(x5,y5,width,height))
            pygame.draw.rect(win,(r,g,b),(x6,y6,width,height))
            pygame.draw.rect(win,(r,g,b),(x7,y7,width,height))
            pygame.draw.rect(win,(r,g,b),(x8,y8,width,height))
            pygame.draw.rect(win,(r,g,b),(x9,y9,width,height))
            pygame.draw.rect(win,(r,g,b),(x10,y10,width,height))
            pygame.draw.rect(win,(r,g,b),(x11,y11,width,height))
            pygame.draw.rect(win,(r,g,b),(x12,y12,width,height))
            pygame.draw.rect(win,(r,g,b),(x13,y13,width,height))
            pygame.draw.rect(win,(r,g,b),(x14,y14,width,height))
            pygame.draw.rect(win,(r,g,b),(x15,y15,width,height))
            pygame.draw.rect(win,(r,g,b),(x16,y16,width,height))
            pygame.draw.rect(win,(r,g,b),(x17,y17,width,height))
        elif score==18:
            len()
            pygame.draw.rect(win,(r,g,b),(x,y,width,height))
            pygame.draw.rect(win,(r,g,b),(x2,y2,width,height))
            pygame.draw.rect(win,(r,g,b),(x3,y3,width,height))
            pygame.draw.rect(win,(r,g,b),(x4,y4,width,height))
            pygame.draw.rect(win,(r,g,b),(x5,y5,width,height))
            pygame.draw.rect(win,(r,g,b),(x6,y6,width,height))
            pygame.draw.rect(win,(r,g,b),(x7,y7,width,height))
            pygame.draw.rect(win,(r,g,b),(x8,y8,width,height))
            pygame.draw.rect(win,(r,g,b),(x9,y9,width,height))
            pygame.draw.rect(win,(r,g,b),(x10,y10,width,height))
            pygame.draw.rect(win,(r,g,b),(x11,y11,width,height))
            pygame.draw.rect(win,(r,g,b),(x12,y12,width,height))
            pygame.draw.rect(win,(r,g,b),(x13,y13,width,height))
            pygame.draw.rect(win,(r,g,b),(x14,y14,width,height))
            pygame.draw.rect(win,(r,g,b),(x15,y15,width,height))
            pygame.draw.rect(win,(r,g,b),(x16,y16,width,height))
            pygame.draw.rect(win,(r,g,b),(x17,y17,width,height))
            pygame.draw.rect(win,(r,g,b),(x18,y18,width,height))
        elif score==19:
            len()
            pygame.draw.rect(win,(r,g,b),(x,y,width,height))
            pygame.draw.rect(win,(r,g,b),(x2,y2,width,height))
            pygame.draw.rect(win,(r,g,b),(x3,y3,width,height))
            pygame.draw.rect(win,(r,g,b),(x4,y4,width,height))
            pygame.draw.rect(win,(r,g,b),(x5,y5,width,height))
            pygame.draw.rect(win,(r,g,b),(x6,y6,width,height))
            pygame.draw.rect(win,(r,g,b),(x7,y7,width,height))
            pygame.draw.rect(win,(r,g,b),(x8,y8,width,height))
            pygame.draw.rect(win,(r,g,b),(x9,y9,width,height))
            pygame.draw.rect(win,(r,g,b),(x10,y10,width,height))
            pygame.draw.rect(win,(r,g,b),(x11,y11,width,height))
            pygame.draw.rect(win,(r,g,b),(x12,y12,width,height))
            pygame.draw.rect(win,(r,g,b),(x13,y13,width,height))
            pygame.draw.rect(win,(r,g,b),(x14,y14,width,height))
            pygame.draw.rect(win,(r,g,b),(x15,y15,width,height))
            pygame.draw.rect(win,(r,g,b),(x16,y16,width,height))
            pygame.draw.rect(win,(r,g,b),(x17,y17,width,height))
            pygame.draw.rect(win,(r,g,b),(x18,y18,width,height))
            pygame.draw.rect(win,(r,g,b),(x19,y19,width,height))
        elif score>=20:
            len()
            pygame.draw.rect(win,(r,g,b),(x,y,width,height))
            pygame.draw.rect(win,(r,g,b),(x2,y2,width,height))
            pygame.draw.rect(win,(r,g,b),(x3,y3,width,height))
            pygame.draw.rect(win,(r,g,b),(x4,y4,width,height))
            pygame.draw.rect(win,(r,g,b),(x5,y5,width,height))
            pygame.draw.rect(win,(r,g,b),(x6,y6,width,height))
            pygame.draw.rect(win,(r,g,b),(x7,y7,width,height))
            pygame.draw.rect(win,(r,g,b),(x8,y8,width,height))
            pygame.draw.rect(win,(r,g,b),(x9,y9,width,height))
            pygame.draw.rect(win,(r,g,b),(x10,y10,width,height))
            pygame.draw.rect(win,(r,g,b),(x11,y11,width,height))
            pygame.draw.rect(win,(r,g,b),(x12,y12,width,height))
            pygame.draw.rect(win,(r,g,b),(x13,y13,width,height))
            pygame.draw.rect(win,(r,g,b),(x14,y14,width,height))
            pygame.draw.rect(win,(r,g,b),(x15,y15,width,height))
            pygame.draw.rect(win,(r,g,b),(x16,y16,width,height))
            pygame.draw.rect(win,(r,g,b),(x17,y17,width,height))
            pygame.draw.rect(win,(r,g,b),(x18,y18,width,height))
            pygame.draw.rect(win,(r,g,b),(x19,y19,width,height))
            pygame.draw.rect(win,(r,g,b),(x20,y20,width,height))
        for j in range(yiv):
            pygame.draw.line(win, (255,255,255),(rows,64), (rows,440))
            pygame.draw.line(win, (255,255,255),(64,rows), (440,rows))
            rows+=width
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                window.quit()
        #Keybord Controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x>62:
            x-=speed
            lp = "L"
        elif keys[pygame.K_RIGHT] and x<500-width-64:
            x+=speed
            lp = "R"
        elif keys[pygame.K_UP] and y>64:
            y-=speed
            lp = "U"
        elif keys[pygame.K_DOWN] and y < 430:
            y+=speed
            lp = "D"
        else:
            if lp=="L" and x>62:
                x-=speed
            elif lp=="R" and x<500-width-64:
                x+=speed
            elif lp == "U" and y>64:
                y-=speed
            elif lp == "D" and y < 430:
                y+=speed
        
        #Get Score
        
        if x == xRandom and y == yRandom:
            xRandom = random.randint(65,390)
            yRandom = random.randint(65,390)
            xRandom = roundup(xRandom)
            yRandom = roundup(yRandom)
            score+=1
            print(score)
            pygame.draw.rect(win,(90,20,10),(xRandom,yRandom, width,height))
        '''
        print("x:"+str(x))
        print("y:"+str(y))
        print("xrandom:"+str(xRandom))
        print("yrandom:"+str(yRandom))
        '''
        
        #Draw Border
        
        pygame.draw.rect(win,(255,255,255),(60,60,380,380), 4)
        
        #Change color
        
        if keys[pygame.K_g]:
            r = 0
            g = 255
            b = 0
        if keys[pygame.K_b]:
            r = 0
            g = 0
            b = 255 
        if keys[pygame.K_r]:
            r = 255
            g = 0
            b = 0   
        
        #Edge Translations
        
        if x==420:
            x=60
        elif x==60:
            x=420
        if y==420:
            y=60
        elif y==60:
            y=420
        
        #Check for Game Over
        
        if x==x2 and y==y2 and score>0:
            game_over()
        if x==x3 and y==y3 and score>0:
            game_over()
        if x==x4 and y==y4 and score>0:
            game_over()
        if x==x5 and y==y5 and score>4:
            game_over()
        if x==x6 and y==y6 and score>5:
            game_over()
        if x==x7 and y==y7 and score>6:
            game_over()
        if x==x8 and y==y8 and score>7:
            game_over()
        if x==x9 and y==y9 and score>8:
            game_over()
        if x==x10 and y==y10 and score>9:
            game_over()
        if x==x11 and y==y11 and score>10:
            game_over()
        if x==x12 and y==y12 and score>11:
            game_over()
        if x==x13 and y==y13 and score>12:
            game_over()
        if x==x14 and y==y14 and score>13:
            game_over()
        if x==x15 and y==y15 and score>14:
            game_over()
        if x==x16 and y==y16 and score>15:
            game_over()
        if x==x17 and y==y17 and score>16:
            game_over()
        if x==x18 and y==y18 and score>17:
            game_over()
        if x==x19 and y==y19 and score>18:
            game_over()
        if x==x20 and y==y20 and score>19:
            game_over()
        pygame.display.update()
#Run Program  

main()
pygame.quit()