import pygame
from sys import exit
import random as rnd


pieces = {
    0 :"Rock",
    1 :"Paper",
    2 :"Scissor",
}
cpu_choices = [0,1,2]
#mapes are bases on cpu choices list
map_cases = {
    0: ["D","L", "W"],
    1: ["W","D", "L"],
    2: ["L","W", "D"],
}

point = 0
round = 1



pygame.init()

#basic variables
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("ROCK-PAPER-SCISSOR")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)
font1 = pygame.font.Font(None, 40)

#surfaces
bg_surface = pygame.image.load('img/background.png')
title_surface = font.render('Rock Paper Scissor',True ,(50, 143, 250,255))
title_rect = title_surface.get_rect(center=(500/2, 35))

player_text = font1.render('PLAYER', True , (64,64,64))
cpu_text = font1.render("CPU", True,(64,64,64))
cpu_text_rect = cpu_text.get_rect(topright = (450,70))
#btns 
rock_btn = pygame.image.load('img/btn/rock_btn.png')
rock_btn_rect = rock_btn.get_rect(topleft=(50 , 380))
paper_btn = pygame.image.load('img/btn/paper_btn.png')
paper_btn_rect = paper_btn.get_rect(topleft=(200, 380))
scissor_btn = pygame.image.load('img/btn/scissors_btn.png')
scissor_btn_rect = scissor_btn.get_rect(topleft=(350, 380))


# pygame.display.set_icon(rock_btn)

rock = pygame.image.load('img/rock.png')
paper = pygame.image.load('img/paper.png')
scissor = pygame.image.load('img/scissor.png')
vs = pygame.image.load('img/vs.png')
wating = pygame.image.load('img/wait.png')

index = 0
def wait_ani():
    img_list = [rock , paper, scissor]
    current_img = img_list[int(index)]
    return current_img


def player_choose():
    if rock_btn_rect.collidepoint(event.pos):
        return 0
    if paper_btn_rect.collidepoint(event.pos):
        return 1
    if scissor_btn_rect.collidepoint(event.pos):
        return 2
    else:
        return "none"

def matchCase(uAns, cpuAns):
    index_cpu = cpu_choices.index(cpuAns)
    mapped_result = map_cases[uAns]
    result = mapped_result[index_cpu]
    return result

# def getpoint(a):
    # global point
    # if a == "D":
    #     point += 0
    # elif a == "W":
    #     point += 5
    # elif a == "L":
    #     point -= 5
    
player_choosed =False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONUP:
            choice = player_choose()
            if not choice == 'none':
                player_choosed = True
                choice_png = pieces[choice] + ".png"
                cpu_choice = rnd.choice(cpu_choices)
                cpu_choice_png = pieces[cpu_choice] + ".png"
                choice_img = pygame.image.load('img/'+choice_png)
                cpu_choice_img = pygame.image.load('img/'+cpu_choice_png)
            else:
                player_choosed =False
    
    
    screen.blit(bg_surface,(0,0))
    screen.blit(title_surface,title_rect)
    screen.blit(rock_btn,rock_btn_rect)
    screen.blit(paper_btn,paper_btn_rect)
    screen.blit(scissor_btn,scissor_btn_rect)
    screen.blit(player_text, (50,70))
    screen.blit(cpu_text, cpu_text_rect)

    if player_choosed == True:
        screen.blit(choice_img, (50,150))
        screen.blit(cpu_choice_img, (300,150))
        screen.blit(vs , (225,200))
        result = matchCase(choice,cpu_choice)
        # getpoint(result)
        if result == "D":
            screen.blit((font.render("DRAW", True , (11, 227, 216))) , (200 ,100))
        elif result == "W":
            screen.blit((font.render(" WIN", True , (11, 227, 216))) , (200 ,100))
        elif result == "L":
            screen.blit((font.render("LOSE", True , (11, 227, 216))) , (200 ,100))
    if player_choosed == False:
        img = wait_ani()
        index = index +0.07
        if index > 3:
            index = 0
        screen.blit(img , (300,150)) 
        screen.blit(wating , (50,150)) 
    # point_surface= font1.render(f"POINT = {point}", True , 'green')
    # screen.blit(point_surface, (0,0))
    pygame.display.update()
    clock.tick(60)