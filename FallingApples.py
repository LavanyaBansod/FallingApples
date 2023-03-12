import pygame
from pygame import mixer
import math
import random
#import time


#..initialize a pygame
pygame.init()


#..create a screen[(x.y)axis]
screen=pygame.display.set_mode((800,600))


#Background
background = pygame.image.load('play_garden.png')
introbackground = pygame.image.load("background_png.png")
help_background = pygame.image.load("game_help.png")
ending_background = pygame.image.load("bluenight.png")


#Clock
#clock = pygame.time.Clock()


#end images
awesome = pygame.image.load('awesome.png')
go_for_it = pygame.image.load('go_for_it.png')
kidding_me = pygame.image.load('kiddingme.png')
not_bad = pygame.image.load('notbad.png')
not_satisfied = pygame.image.load('notsatisfied.png')
wooo = pygame.image.load('wooo.png')


#Background music
mixer.music.load('River Flow In You.mp3')
mixer.music.play(-1)


#..title and icon
pygame.display.set_caption("Newton's Apple...")
icon = pygame.image.load('Applee.png')
pygame.display.set_icon(icon)


#...basket

# Image
basketImg = pygame.image.load('basket.png')

#position
basketX = 370
basketY = 500
basketX_change = 0


#...apple
appleImg = []
appleX = []
appleY = []
appleX_change = []
appleY_change = []
num_of_apples = 3


for i in range(num_of_apples):
    # Image
    appleImg.append(pygame.image.load('Applee.png'))
    
    # position
    appleX.append(random.randint(-25,730))
    appleY.append(random.randint(0,15))
    
    #speed
    appleX_change.append(0)
    appleY_change.append(1)
    


score_value = 0
dodge_value = 0

# Dodge font position
DtxtX = 600  
DtxtY = 10

# score font position
StxtX = 10
StxtY = 10

# Font types

# Score, dodge
font = pygame.font.Font('freesansbold.ttf',32)

# game over text
over_font = pygame.font.SysFont('chiller',60)

# comments on final page
face_font = pygame.font.SysFont('chiller',64)

# intro text
start_font = pygame.font.SysFont('comicsansms',70)

# Buttons in intro 
small_font = pygame.font.SysFont('comicsansms',40)

# Buttons in intro
large_font = pygame.font.SysFont('comicsansms',50)
large_fonts = pygame.font.SysFont('comicsansms',60)



def show_score(x,y,score_value):          # (x,y)
    score = font.render("Score: "+str(score_value),True, (255,255,255))
    screen.blit(score, (x,y))

    
def dodge(x,y,value):
    Dscore = font.render("Dodge: "+str(value),True, (255,255,255))
    screen.blit(Dscore, (x,y))    


def basket(x,y):
    # Basket image, position
    screen.blit(basketImg, (x,y))


def got_apple(appleX, appleY, basketX, basketY):
    # Checks if basket touches the apple
    distance = math.sqrt((math.pow(appleX - basketX,2)) +
                         (math.pow(appleY-basketY,2)))
    if distance < 43:
        return True
    else:
        return False


def apple(x,y,i):
    # Apple image, position
    screen.blit(appleImg[i], (x,y))


def game_start_text():
    # Game intro text
    
    # Change colour continuously of the text
    bg = (random.randint(0,100), random.randint(0,100) ,random.randint(0,100))
    start_text = start_font.render("""..Falling Apples..""",True,bg)
    
    # display '..Falling Apples..' on intro screen(image,position)
    screen.blit(start_text,(140,150))


def game_over_text(score_value):
    
    over_text = over_font.render("""Your score: """+ str(score_value),True,
                                 (100,100,100))

    # Display score font on end screen
    screen.blit(over_text,(275,320))


def overImg(Img):
    
    # Display emojies and comments on final page
    
    # Display different emojies on different intervals of score
    if Img >= 30 and Img < 40:
        
        # (image, (position))
        screen.blit(wooo, (275,100))
        
        # comment font style
        face_text = face_font.render("""Wooooo!!! """,True,(245,222,179))
        
        # comment ,(position)
        screen.blit(face_text,(275,400))
        return

        
    elif Img >= 10 and Img < 20:
        screen.blit(go_for_it, (275,100))
        face_text = face_font.render("""Go For It!!!! """,True,(245,222,179))
        screen.blit(face_text,(275,400))
        return

        
    elif Img <= 20 and Img < 30 :
        screen.blit(kidding_me, (275,100))
        face_text = face_font.render("""Lucky... """,True,(245,222,179))
        screen.blit(face_text,(275,400))
        return

        
    elif Img >= 5 and Img < 10:
        screen.blit(not_bad, (275,100))
        face_text = face_font.render("""Not Bad## """,True,(245,222,179))
        screen.blit(face_text,(275,400))
        return

        
    elif Img < 5:
        screen.blit(not_satisfied, (275,100))
        face_text = face_font.render("""Difficult??""",True,(245,222,179))
        screen.blit(face_text,(275,400))
        return

        
    elif Img > 40:
        screen.blit(awesome, (275,100))
        face_text = face_font.render("""AWESOME!!! """,True,(245,222,179))
        screen.blit(face_text,(275,400))
        return


def game_intro():

    # starting game intro
    intro = True

    while intro:

        # setting intro background
        screen.blit(introbackground,(0,0))
        
        # Display game name
        game_start_text()


        for event in pygame.event.get():
            # End the game/ get out of the game
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        # get position of mouse
        mouse = pygame.mouse.get_pos()
        
        # checks if mouse key is pressed
        click = pygame.mouse.get_pressed()


        # mouse[0] -> Checks if mouse cursor is in
                        # the specified area along x- axis
        # mouse[1] -> Checks if mouse cursor is in
                        # the specified area along y-axis


        # if cursor is in specifed area font size increases
        
        # Go button
        if 190 > mouse[0] > 90 and 500 > mouse[1] > 450:
            Go_text = large_font.render("""..GO..""",True,(0,255,0))
            screen.blit(Go_text,(100+5,450+5))
            # click[0] -> Checks if the mouse key is pressed
            if click[0] == 1:
                # game_loop() -> game starts
                game_loop()
                
        else:
            # display text when cursor is not in specified area
            Go_text = small_font.render("""..GO..""",True,(0,200,0))
            screen.blit(Go_text,(100,450))


        # Quit Button
        if 660 > mouse[0] > 550 and 500 > mouse[1] > 450:
            Quit_text = large_font.render(""".Quit.""",True,(255,0,0))
            screen.blit(Quit_text,(550+5,450+5))
            if click[0] == 1:
                # End game when 'Quit' button is pressed
                pygame.quit()
                quit()
                
        else:
            Quit_text = small_font.render(""".Quit.""",True,(200,0,0))
            screen.blit(Quit_text,(550,450))
            

        # Help Button
        if 470 > mouse[0] > 320 and 550 > mouse[1] > 500:
            help_text = large_font.render("""..Help..""",True,(132,132,132))
            screen.blit(help_text,(320+5,500+5))
            if click[0] == 1:
                # Display help image, (position)
                screen.blit(help_background, (0,0))
                

        else:
            help_text = small_font.render("""..Help..""",True,(75,75,75))
            screen.blit(help_text,(320,500))


        # updates all the changes done
        pygame.display.update()



    # (position of basket, score value, dodge value, movement of basket)
    #...when game starts
def game_loop(basketX = 370,score_value = 0,dodge_value = 0,basketX_change = 0):    
    
    #game loop
    running = True
    while running:

        # Display Background image when game is running
        screen.blit(background,(0,0))


        # Quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                break


            # checks if any key is pressed
            if event.type == pygame.KEYDOWN:
                # speed
                
                # checks if left arrow is pressed
                if event.key == pygame.K_LEFT:
                    # Move basket along negative x-axis (left)
                    basketX_change = -2
                    
                # Checks if right arrow is pressed
                if event.key == pygame.K_RIGHT:
                    # Move basket along positive x-axis (right)
                    basketX_change = 2

                    
            # Checks if the key is not pressed
            if event.type == pygame.KEYUP:
                # Checks if left arrow or right arrow key is not pressed
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    # When the keys are not pressed their position is not changed
                    basketX_change = 0

                
        ###...checking for boundaries
        # changing the position of basket
        basketX += basketX_change


        # if the basket is at left end (0 pixel) basket cannot move further
        if basketX <= 0:
            basketX = 0
            
        # if the basket is at right end (736 pixel) basket will remain
        #at same position
        if basketX >= 736:
            basketX = 736


        for i in range(num_of_apples):
            # change the position of the apple
            appleY[i] += appleY_change[i]
            # if apple crosses 590 pixels it will again come to 0-15 pixels
            if appleY[i] > 590:
                
                # any random position from 0-15 pixels(y-axis)
                appleY[i] = random.randint(0,15)
                appleY[i] += appleY_change[i]
                
                # any random position from -25 to 730 pixels(x-axis)
                appleX[i] = random.randint(-25,730)
                
                # increment in dodge value whenever the apple is catched
                dodge_value += 1
                
                # When dodge value is 50 game ends
                if dodge_value > 49:
                    running = False

            # position of apple(x,y) and basket(x,y)
            catch = got_apple(appleX[i],appleY[i],basketX,basketY)
            
            if catch:
                
                # make swoosh sound whenever the apple is catched
                catch_sound = mixer.Sound("swoosh .wav")
                catch_sound.play()
                
                # when apple is catched it again starts from top
                appleY[i] = random.randint(0,15)
                appleX[i] = random.randint(-25,730)
                
                # increase score whenever the apple is catched
                score_value += 1

            # display apple image
            apple(appleX[i], appleY[i], i)
            
        # display dodge value
        dodge(DtxtX, DtxtY, dodge_value)
        
        # display score
        show_score(StxtX, StxtY, score_value)
        
        # display basket image
        basket(basketX,basketY)
        
        # update the changes done
        pygame.display.update()
        

    while not running:
        # display backgroung image
        screen.blit(ending_background,(0,0))
        
        # display 'Game Over' text
        game_over_text(score_value)
        
        # display faces and comments
        overImg(score_value)
        
        # display score(x, y, score)
        show_score(StxtX, StxtY, score_value)
        
        # display dodge value (x, y, dodge value)
        dodge(DtxtX, DtxtY, dodge_value)
        x = 250
        y = 475
        
        # get mouse position
        mouse = pygame.mouse.get_pos()
        
        # checks if mouse click is pressed
        click = pygame.mouse.get_pressed()
        

        # quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # MENU BUTTON
        # display text when cursor is in specified area
        if 550 > mouse[0] > 250 and 550 > mouse[1] > 450:
            again_text_2 = large_fonts.render("Main Menu!!",True,(255,240,245))
            screen.blit(again_text_2,(x-5,y-5))
            
            if click[0] == 1:
                game_intro()

        # display text when cursor is not in specified area
        else:
            again_text_1 = large_font.render("Main Menu!!",True,(230,230,250))
            screen.blit(again_text_1,(x,y))

            
        pygame.display.update()
        
# calls intro function
game_intro()
# calls game loop
game_loop()
