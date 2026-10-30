import pygame
import math
import random

pygame.init()

WIDTH = 1200
HEIGHT = 800
SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
sky_color = (176,210,237)#night = 12,9,10
running = True
time = 0 #360 = 1 day#

cloud_x = 148
cloud_y = 99
cloud_color = (255,255,255)
sun_radius = 80
moon_radius = 55
sun_color = (255,249,78)
moon_color = (245,242,225)

while running:
    time += 1
    cloud_x += 3
    if(cloud_x >= WIDTH + 40):
        cloud_x = -97
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        
    
    temp = 180 - min((time+90) % 360,360-((time+90)%360)) #the difference from moon
    sky_color = (int(math.cos(temp/180*math.pi) * (82)+94),int((math.cos(temp/180*math.pi) *  (100.5))+109.5),int((math.cos(temp/180*math.pi) *  (113.5))+123.5))
    screen.fill(sky_color)
    pygame.draw.circle(screen,sun_color,(int(600-510*math.cos(time/180*math.pi)),int(600-510*math.sin(time/180*math.pi))),sun_radius)#sun
    #moon
    moon_x,moon_y = int(600+510*math.cos(time/180*math.pi)),int(600+510*math.sin(time/180*math.pi))
    pygame.draw.circle(screen,moon_color,(moon_x,moon_y),moon_radius)
    pygame.draw.circle(screen,(222,222,198),(moon_x+20,moon_y+12),21)
    pygame.draw.circle(screen,(222,222,198),(moon_x-25,moon_y-3),15)
    pygame.draw.circle(screen,(222,222,198),(moon_x+14,moon_y-22),16)
    pygame.draw.circle(screen,(222,222,198),(moon_x-3,moon_y+34),10)

    pygame.draw.rect(screen, (155,118,83),(0,600,1200,200))#land
    pygame.draw.rect(screen, (43,45,66),(500,200,200,400))#building
    #clock
    pygame.draw.circle(screen, (192,192,192),(600,300),75)
    pygame.draw.rect(screen, (0,0,0),(597,225,6,12))
    pygame.draw.rect(screen, (0,0,0),(597,363,6,12))
    pygame.draw.rect(screen, (0,0,0),(525,297,12,6))
    pygame.draw.rect(screen, (0,0,0),(663,297,12,6))
    pygame.draw.line(screen, (0,0,0),(600,300),(600+70*math.sin(24*time/180*math.pi),300-70*math.cos(24*time/180*math.pi)),2)
    pygame.draw.line(screen, (0,0,0),(600,300),(600-50*math.sin(2*time/180*math.pi),300+50*math.cos(2*time/180*math.pi)),5)
    pygame.draw.circle(screen, (184,115,51),(600,300),4)
    #windows
    coordinate_list = [(520,400,70,80),(520,505,70,80),(610,400,70,80),(610,505,70,80)]
    if(time % 360 <= 180):
        for i in range(4):
            pygame.draw.rect(screen,(sky_color[0]*3//5+8,sky_color[1]*3//5+10,sky_color[2]*3//5+14),coordinate_list[i])

    else:
        for i in range(4):
            pygame.draw.rect(screen,(sky_color[0]*3//20+217,sky_color[1]*3//20+187,sky_color[2]*3//20+111),coordinate_list[i])
       

    #cloud
    pygame.draw.circle(screen,cloud_color,(cloud_x,cloud_y),40)
    pygame.draw.circle(screen,cloud_color,(cloud_x+34,cloud_y-32),40)
    pygame.draw.circle(screen,cloud_color,(cloud_x+57,cloud_y-17),40)

    #shadowing
    shadowing_color = (79,76,70)
    if(time%360 >= 15 and time%360 <= 165):
        pygame.draw.polygon(screen,shadowing_color,[(500,600),(700,600),(700+150*math.tan((90-time)/180*math.pi),750),(500+150*math.tan((90-time)/180*math.pi),750)])
    

    pygame.display.flip()
    clock.tick(30)
    

pygame.quit()
