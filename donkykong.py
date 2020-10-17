import pygame, sys
import time
import random
from pygame.locals import *

pygame.init()

pygame.time.set_timer(USEREVENT+1,2000)
display_width = 800
display_height = 300
display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('layout')

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
purple = (255,0,255)
coin = (100,100,0)

clock = pygame.time.Clock()
block_size = 10
FPS = 30

levels = []
ladders = []
pygame.mixer.music.load('music.mp3')
class layout():

    def level(self):
       
        bricks=pygame.image.load(filename5)

        bricktop=pygame.transform.scale(bricks,(display_width,block_size))
        display.blit(bricktop,(0,0))
        display.blit(bricktop,(0,display_height-block_size))
        brickleft=pygame.transform.scale(bricks,(block_size,display_height))
        display.blit(brickleft,(0,0))
        display.blit(brickleft,(display_width-block_size,0))
        for i in [1,2,3,4,5]:
            brick.append(pygame.transform.scale(bricks,(levels[2*(i-1)+1],block_size)))
            display.blit(brick[i-1],(levels[2*(i-1)],block_size+(i)*3*block_size+(i-1)*2*block_size))
           
    def ladder(self):
        ladder=pygame.image.load(filename3)
        for i in [1,2,3,4,5]:
            ladder3=pygame.transform.scale(ladder,(2*block_size,5*block_size))
            display.blit(ladder3,(ladders[i-1],block_size+(i)*3*block_size+(i-1)*2*block_size))
            #pygame.draw.rect(display, red, [ladders[i-1],block_size+(i)*3*block_size+(i-1)*2*block_size,block_size,5*block_size])

        ladder1=pygame.transform.scale(ladder,(2*block_size,6*block_size))
        display.blit(ladder1,(710,14*10))
        ladder2=pygame.transform.scale(ladder,(2*block_size,2*block_size))
        display.blit(ladder2,(710,22*10))
    def coins(self):
        coin1=pygame.image.load(filename2)
        coin=pygame.transform.scale(coin1,(2*block_size,2*block_size))
        if collect1 == 0:
            display.blit(coin,(750,270))
        if collect2 == 0:
            display.blit(coin,(390,270))
            #display.blit(display, coin, [390,280,block_size,block_size])
        if collect3 == 0:
            display.blit(coin,(220,220))
        if collect4 == 0:
            #pygame.draw.rect(display, coin, [770,230,block_size,block_size])
            display.blit(coin,(770,220))
        if collect5 == 0:
            display.blit(coin,(400,170))
            #pygame.draw.rect(display, coin, [400,180,block_size,block_size])
        if collect6 == 0:
            display.blit(coin,(50,170))
            #pygame.draw.rect(display, coin, [50,180,block_size,block_size])
        if collect7 == 0:
            display.blit(coin,(320,120))
            #pygame.draw.rect(display, coin, [320,130,block_size,block_size])
        if collect8 == 0:
            display.blit(coin,(720,120))
            #pygame.draw.rect(display, coin, [720,130,block_size,block_size])
        if collect9 == 0:
            display.blit(coin,(470,70))
            #pygame.draw.rect(display, coin, [470,80,block_size,block_size])
        if collect10 == 0:
            display.blit(coin,(90,70))
            #pygame.draw.rect(display, coin, [90,80,block_size,block_size])
        if collect11 == 0:
            display.blit(coin,(600,20))
            #pygame.draw.rect(display, coin, [600,30,block_size,block_size])
       
class person():
    
    def donkey(self):
        global donk_x,donk_y,donk_x_change
        if donk_x <= 260:
            donk_x_change = 5
        if donk_x >= 700:
            donk_x_change = -5
        donk_x += donk_x_change
        pic=pygame.image.load(filename0)
        pic1=pygame.transform.scale(pic,(15,15))
        display.blit(pic1,(donk_x,donk_y))
        #pygame.draw.rect(display, green, [donk_x,donk_y,block_size,block_size])
class balls():

    def creation(self):
        fireballs.append([donk_x,donk_y,-donk_x_change/5])
    def floorandladder(self):
        global lead_x,lead_y,h
        ball=pygame.image.load(filename4)
        ball2=pygame.transform.scale(ball,(15,15))
        for fireball in fireballs:
            fireball[0]=fireball[0]+fireball[2]*5
            if fireball[0]>=770:
                fireball[0] = 770
                fireball[2] = 0 - fireball[2]
            if fireball[0]<=10:
                fireball[0] = 10
                fireball[2] = 0 - fireball[2]
            ###########################################################
            if fireball[1] == 25 and  fireball[0] < 260:
                fireball[1] = 75
            if fireball[1] == 75 and fireball[0] > 490:
                fireball[1] = 125
            if fireball[1] == 125 and fireball[0] < 290:
                fireball[1] = 175

            if fireball[1] == 175 and fireball[0] > 420:
                fireball[1] = 225
            if fireball[1] == 225 and fireball[0] < 200:
                fireball[1] = 275

            n = random.randrange(0,5)

            if fireball[0] == 640 and fireball[1] == 225 and n == 1:
                fireball[1] = 275
            if fireball[0] == 710 and fireball[1] == 125 and n == 2:
                fireball[1] = 225
            if fireball[0] == 150 and fireball[1] == 75 and n == 3:
                fireball[1] = 175

            if fireball[0] == 400 and fireball[1] == 25 and n== 4:
                fireball[1] = 75
            if fireball[0] == 370 and fireball[1] == 175 and n == 0:
                fireball[1] = 225
            if fireball[0] == 30 and fireball[1] == 275:
                fireballs.remove(fireball)
                print lead_x
                print lead_y
                print h
            if (fireball[0] <= lead_x <= fireball[0]+5 or fireball[0]-5 <= lead_x <= fireball[0] ) and lead_y == fireball[1]- 5:
                h = h-1
                lead_x = 20
                lead_y = 270
                gameover = True 
            
            ###########################################################
            display.blit(ball2,(fireball[0],fireball[1]))
            #pygame.draw.rect(display, red, [fireball[0],fireball[1],10,10])
class player():
    def get_position(self):
        return [lead_x,lead_y]
    def move_right(self):
        global lead_x_change
        lead_x_change = 10
    def move_left(self):
        global lead_x_change
        lead_x_change = -10
    def up(self):
        global lead_x,lead_y
        if lead_x == 640 and lead_y == 270:
            lead_y = 220
        if lead_x == 360 and lead_y == 220:
            lead_y = 170
        if lead_x == 150 and lead_y == 170:
            lead_y = 70
        if lead_x == 400 and lead_y == 70:
            lead_y = 20
    def down(self):
        global lead_x,lead_y
        if lead_x == 640 and lead_y == 220:
            lead_y = 270
        if lead_x == 360 and lead_y == 170:
            lead_y = 220
        if lead_x == 150 and lead_y == 70:
            lead_y = 170
        if lead_x == 400 and lead_y == 20:
            lead_y = 70
        if lead_x == 710 and lead_y == 120:
            lead_y = 220
class checks():
    def check(self):
        global lead_x, lead_y
        if lead_y == 20 and  lead_x < 260:
            lead_y = 70
        if lead_y == 70 and lead_x > 480:
            lead_y = 120
        if lead_y == 120 and lead_x < 290:
            lead_y = 170
       
        if lead_y == 170 and lead_x > 400:
            lead_y = 220
        if lead_y == 220 and lead_x < 200:
            lead_y = 270
    def border(self):
        global lead_x,lead_y
        if lead_x < 10:
            lead_x = 10
        if lead_y >= 270:
            lead_y = 270
        if lead_x >= 770:
            lead_x = 770
C=checks()
M=player()
P=person()
L=layout()
B=balls()
levels=[260,540,0,490,300,500,0,410,210,590]
ladders=[400,150,150,360,640]
lead_x_change = 0
filename1 = 'person.png'
filename2 = 'coin.png'
filename3 = 'ladder.png'
filename4 = 'ball.png'
filename0 = 'ape.png'
filename5 = 'brick.jpg'
filename8 = 'queen.png'
fireballs = []
brick = []
collect1 = 0
collect2 = 0
collect3 = 0
collect4 = 0
collect5 = 0
collect6 = 0
collect7 = 0
collect8 = 0
collect9 = 0
collect10 = 0
collect11 = 0
h = 3
donk_x = 700 
donk_y = 25
donk_x_change = -5
lead_x = 20
lead_y = 270
lead_x_change =0
lead_y_change =0
def mainloop():
    pygame.mixer.music.play(-1,0.0)
    global collect1,collect2,collect3
   
 
    global collect4
    global collect5
    global collect6
    global collect7
    global collect8
    global collect9
    global collect10
    global collect11
    global h,donk_x,donk_y,donk_x_change,lead_x,lead_y,lead_x_change,lead_y_change
    gameover = False
    gameexit = False
    lead_x = 20
    lead_y = 270
    lead_x_change =0
    lead_y_change =0    
    c = 0   
    donk_x_change = -5
    q = 1
    k1=k2=k3=k4=k5=k6=k7=k8=k9=k10=k11= 0
    score = 0
    while not gameexit and h > 0:
        
        C.check()
        
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT+1:
                B.creation()
            if event.type == pygame.QUIT:
                gameexit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    M.move_right()
                            
                if event.key == pygame.K_LEFT:
                        
                    M.move_left()
                if event.key == pygame.K_SPACE and c!=1:
                    c = 1
                    lead_y_change = -6
                    
                
                if event.key == pygame.K_UP:
                    M.up()
                if event.key == pygame.K_DOWN:
                    M.down()
                
                
                    
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    lead_x_change = 0
                
        if c == 1: 
            lead_y_change += 1
            if lead_y_change == 6:
                c = 0
                lead_y_change = 0
    
                
        lead_x += lead_x_change
        lead_y += lead_y_change
        C.border()
        
        ################# coin collection ######################
        if lead_x == 750 and lead_y == 270 and k1==0:
            collect1 = 1
            score += 25
            k1 = 1
        if lead_x == 390 and lead_y == 270 and k2==0:
            collect2 = 1
            score += 25
            k2 = 1
        if lead_x == 220 and lead_y == 220 and k3==0:
            collect3 = 1
            score += 25
            k3 = 1
        if lead_x == 770 and lead_y == 220 and k4==0:
            collect4 = 1
            score += 25
            k4 = 1
            
        if lead_x == 400 and lead_y == 170 and k5==0:
            collect5 = 1
            score += 25
            k5 = 1
        if lead_x == 50 and lead_y == 170 and k6==0:
            collect6 = 1
            score += 25
            k6 = 1
        if lead_x == 320 and lead_y == 120 and k7==0:
            collect7 = 1
            score += 25
            k7 = 1
        if lead_x == 720 and lead_y == 120 and k8==0:
            collect8 = 1
            score += 25
            k8 = 1
        if lead_x == 470 and lead_y == 70 and k9==0:
            collect9 = 1
            score += 25
            k9 = 1
        if lead_x == 90 and lead_y == 70 and k10==0:
            collect10 = 1
            score += 25
            k10 = 1
        if lead_x == 600 and lead_y == 20 and k11==0:
            collect11 = 1
            score += 25
            k11 = 1
        ##########################################################
        display.fill(white)
        L.level()
        L.ladder()
         ################################### coins ##############################
        L.coins()
        P.donkey()
        ##############################################################################
        img=pygame.image.load(filename1)
        img2=pygame.transform.scale(img,(20,20))
        display.blit(img2,(lead_x,lead_y))
        queen=pygame.image.load(filename8)
        queen2=pygame.transform.scale(queen,(20,20))
        display.blit(queen2,(770,20))
        #pygame.draw.rect(display, purple, [77*10,20,block_size,block_size])
        if lead_x == 770 and lead_y == 20:
            h = 0
            q = 2
        
        ################################### fireballs ##########################
        
        B.floorandladder()

        font = pygame.font.SysFont(None, 20)
        screen_text = font.render("LIFE:"+str(h),True , red)
        display.blit(screen_text, [130,10]) 
        pygame.display.update()   
        
       
        font = pygame.font.SysFont(None, 20)
        screen_text = font.render("SCORE:"+str(score),True , red)
        display.blit(screen_text, [40,10]) 
        pygame.display.update()
        clock.tick(FPS)
    while  (h == 0 and q == 1) :
        global fireballs
        display.fill(green)
        font = pygame.font.SysFont(None, 20)
        screen_text = font.render("SCORE:"+str(score),True , red)
        display.blit(screen_text, [400, 100])
        screen_text = font.render("Game Over  q:quit p:playagain ",True , red)
        display.blit(screen_text, [400, 150])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    q = 0
                if event.key == pygame.K_w:
                    collect1 = 0
                    collect2 = 0
                    collect3 = 0
                    collect4 = 0
                    collect5 = 0
                    collect6 = 0
                    collect7 = 0
                    collect8 = 0
                    collect9 = 0
                    collect10 = 0
                    collect11 = 0
                    print 'hi'
                    h = 3
                    fireballs = []
                    mainloop()
    while  (h == 0 and q == 2) :
        global fireballs
        display.fill(green)
        font = pygame.font.SysFont(None, 20)
        screen_text = font.render("SCORE:"+str(score),True , red)
        display.blit(screen_text, [400, 100])
        screen_text = font.render("YOU WON: CONGO!!  q:quit p:playagain ",True , red)
        display.blit(screen_text, [400, 150])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    q = 0
                if event.key == pygame.K_p:
                    collect1 = 0
                    collect2 = 0
                    collect3 = 0
                    collect4 = 0
                    collect5 = 0
                    collect6 = 0
                    collect7 = 0
                    collect8 = 0
                    collect9 = 0
                    collect10 = 0
                    collect11 = 0
                    print 'hi'
                    h = 3
                    fireballs = []
                    mainloop()
                
    pygame.mixer.music.stop()   
    pygame.quit()
    quit()
mainloop()

            
                        
                        
