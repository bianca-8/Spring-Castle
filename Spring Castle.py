#Name: Bianca Bian
#Date: March 9, 2023
#Course Code: ICS3U1-04
#Description: This program draws a castle in spring

import pygame
import random
import math
pygame.init()
SIZE = (1000,700) 
screen = pygame.display.set_mode(SIZE)


#Colors
RED = (250,103,100)
ORANGE = (250,180,100)
BLUE = (187,223,237)
SKY_BLUE = (157,218,242)
RAINBOW_BLUE = (179,218,245)
YELLOW = (255,228,1)
BRIGHT_YELLOW = (255,255,0)
RAINBOW_YELLOW = (247,243,119)
GREEN = (0,108,0)
RAINBOW_GREEN = (170,247,119)
GRASS_GREEN = (102, 242, 90)
TREE_GREEN1 = (39,135,22)
TREE_GREEN2 = (45,156,26)
VIOLET = (213,179,245)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREY = (235,235,235)
BROWN = (152,110,84)
DOOR_BROWN = (93,41,6)
TREE_BROWN = (61,39,24)

#Coordinates of the top right corner of the box behind the towers
x = 325 
y = 300

#Random:
#Random bird xy coordinates
birdX1 = random.randint(0,1000)
birdY1 = random.randint(0,100)
birdX2 = birdX1 + random.randint(10,20)
birdY2 = birdY1 + random.randint(10,20)
birdX3 = birdX1 + random.randint(-10,30)
birdY3 = birdY1 + random.randint(-10,30)
birdX4 = birdX2 + random.randint(30,40)
birdY4 = birdY1 + random.randint(30,40)

#Random colours
redRandom = random.randint(0,255)
greenRandom = random.randint(0,255)
blueRandom = random.randint(0,255)

#Flower random colour combinations
flowerRandom1 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
flowerRandom2 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
flowerRandom3 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))


#Background:
#Sky background
pygame.draw.rect(screen,SKY_BLUE,(0,0,1000,450)) 
#Sun
pygame.draw.circle(screen,YELLOW,(0,0),70)

#rainbow
pygame.draw.ellipse(screen,RED,(x-250,y-250,800,800))
pygame.draw.ellipse(screen,ORANGE,(x-235,y-230,765,780))
pygame.draw.ellipse(screen,RAINBOW_YELLOW,(x-213,y-210,730,760))
pygame.draw.ellipse(screen,RAINBOW_GREEN,(x-193,y-190,700,740))
pygame.draw.ellipse(screen,RAINBOW_BLUE,(x-173,y-170,670,720))
pygame.draw.ellipse(screen,VIOLET,(x-153,y-150,640,700))
pygame.draw.ellipse(screen,SKY_BLUE,(x-133,y-130,610,680))

#grass background
pygame.draw.rect(screen,GRASS_GREEN,(0,350,1000,350)) 

#Draw clouds
def drawCloud(x,y):
  pygame.draw.ellipse(screen,GREY,(x+10,y,70,70)) #left circle
  pygame.draw.ellipse(screen,GREY,(x+60,y-10,70,80)) #middle circle
  pygame.draw.ellipse(screen,GREY,(x+110,y,70,70)) #right circle
drawCloud(random.randint(0, 1000),random.randint(0, 150))
drawCloud(random.randint(0, 1000),random.randint(0, 150))
drawCloud(random.randint(0, 1000),random.randint(0, 150))
drawCloud(random.randint(0, 1000),random.randint(0, 150))
drawCloud(random.randint(0, 1000),random.randint(0, 150))
drawCloud(random.randint(0, 1000),random.randint(0, 150))
drawCloud(random.randint(0, 1000),random.randint(0, 150))

#Castle:
#Wall lines leading to back of castle
pygame.draw.polygon(screen,BROWN,((x,y),(x+50,y-50),(x+300,y-50),(x+350,y)))
#Outline
pygame.draw.line(screen,BLACK,(x,y),(x+50,y-50))
pygame.draw.line(screen,BLACK,(x+50,y-50),(x+300,y-50))
pygame.draw.line(screen,BLACK,(x+300,y-50),(x+350,y))

#Wall behind the towers
pygame.draw.rect(screen,BROWN,(x,y,350,195))
#Horizontal wall lines
pygame.draw.line(screen,BLACK,(x,y),(x+350,y))
pygame.draw.line(screen,BLACK,(x,y+15),(x+350,y+15))
pygame.draw.line(screen,BLACK,(x,y+30),(x+350,y+30))
pygame.draw.line(screen,BLACK,(x,y+45),(x+350,y+45))
pygame.draw.line(screen,BLACK,(x,y+60),(x+350,y+60))
pygame.draw.line(screen,BLACK,(x,y+75),(x+350,y+75))
pygame.draw.line(screen,BLACK,(x,y+90),(x+350,y+90))
pygame.draw.line(screen,BLACK,(x,y+105),(x+350,y+105))
pygame.draw.line(screen,BLACK,(x,y+120),(x+350,y+120))
pygame.draw.line(screen,BLACK,(x,y+135),(x+350,y+135))
pygame.draw.line(screen,BLACK,(x,y+150),(x+350,y+150))
pygame.draw.line(screen,BLACK,(x,y+165),(x+350,y+165))
pygame.draw.line(screen,BLACK,(x,y+180),(x+350,y+180))
pygame.draw.line(screen,BLACK,(x,y+195),(x+350,y+195))

#Side towers
def drawTower(x,y): #function for side towers
#Back tower blocks on top of towers
  pygame.draw.rect(screen,BROWN,(x+20,y-40,15,30)) #left block
  pygame.draw.line(screen,BLACK,(x+20,y-40),(x+35,y-40)) #top line
  pygame.draw.line(screen,BLACK,(x+20,y-40),(x+20,y-15)) #left line
  pygame.draw.line(screen,BLACK,(x+35,y-40),(x+35,y-20)) #right line
  pygame.draw.rect(screen,BROWN,(x+60,y-40,15,30)) #right block
  pygame.draw.line(screen,BLACK,(x+60,y-40),(x+75,y-40)) #top line
  pygame.draw.line(screen,BLACK,(x+60,y-40),(x+60,y-20)) #left line
  pygame.draw.line(screen,BLACK,(x+75,y-40),(x+75,y-15)) #right line

  #Top and bottom curve of side towers
  pygame.draw.rect(screen,BROWN,(x,y,100,225))
  pygame.draw.ellipse(screen,BROWN,(x,y-20,100,40))
  pygame.draw.ellipse(screen,BROWN,(x,y+220,100,10))
  pygame.draw.arc(screen,BROWN,(x,y+220,100,10),math.radians(180),math.radians(0),5)
  pygame.draw.arc(screen,BLACK,(x,y-20,100,40),math.radians(0),math.radians(180)) #outline of top of towers
  
  #curves on body of tower
  pygame.draw.arc(screen,BLACK,(x,y-10,100,10),math.radians(180),math.radians(0))
  pygame.draw.arc(screen,BLACK,(x,y+10,100,10),math.radians(180),math.radians(0))
  pygame.draw.arc(screen,BLACK,(x,y+25,100,10),math.radians(180),math.radians(0))
  pygame.draw.arc(screen,BLACK,(x,y+40,100,10),math.radians(180),math.radians(0))
  pygame.draw.arc(screen,BLACK,(x,y+55,100,10),math.radians(180),math.radians(0))
  pygame.draw.arc(screen,BLACK,(x,y+70,100,10),math.radians(180),math.radians(0))
  pygame.draw.arc(screen,BLACK,(x,y+85,100,10),math.radians(180),math.radians(0))
  pygame.draw.arc(screen,BLACK,(x,y+100,100,10),math.radians(180),math.radians(0))
  pygame.draw.arc(screen,BLACK,(x,y+115,100,10),math.radians(180),math.radians(0))
  pygame.draw.arc(screen,BLACK,(x,y+130,100,10),math.radians(180),math.radians(0))
  pygame.draw.arc(screen,BLACK,(x,y+145,100,10),math.radians(180),math.radians(0))
  pygame.draw.arc(screen,BLACK,(x,y+160,100,10),math.radians(180),math.radians(0))
  pygame.draw.arc(screen,BLACK,(x,y+175,100,10),math.radians(180),math.radians(0))
  pygame.draw.arc(screen,BLACK,(x,y+190,100,10),math.radians(180),math.radians(0))
  pygame.draw.arc(screen,BLACK,(x,y+205,100,10),math.radians(180),math.radians(0))
  pygame.draw.arc(screen,BLACK,(x,y+220,100,10),math.radians(180),math.radians(0))

 #Front tower blocks at the top of towers
  pygame.draw.rect(screen,BROWN,(x,y-30,15,30)) #left block
  pygame.draw.line(screen,BLACK,(x,y-30),(x+15,y-30)) #top line
  pygame.draw.line(screen,BLACK,(x+15,y-30),(x+15,y-2)) #left line
  pygame.draw.rect(screen,BROWN,(x+40,y-30,15,30)) #middle block
  pygame.draw.line(screen,BLACK,(x+40,y-30),(x+40,y)) #left line
  pygame.draw.line(screen,BLACK,(x+55,y-30),(x+55,y)) #top line
  pygame.draw.line(screen,BLACK,(x+40,y-30),(x+55,y-30)) #right line
  pygame.draw.rect(screen,BROWN,(x+85,y-30,15,30)) #right block
  pygame.draw.line(screen,BLACK,(x+85,y-30),(x+100,y-30)) #top line
  pygame.draw.line(screen,BLACK,(x+85,y-30),(x+85,y-2)) #left line

  #Black outlines on sides of tower
  pygame.draw.line(screen,BLACK,(x,y-30),(x,y+225)) #Black line on the left
  pygame.draw.line(screen,BLACK,(x+100,y-30),(x+100,y+225)) #Black line on the right

drawTower(x-100,y-15) #Left tower
drawTower(x+350,y-15) #Right tower

#Middle tower
def drawMidTower(x,y):
#Back boxes on top of tower
  pygame.draw.rect(screen,BROWN,(x+20,y-20,15,30)) #box color
  pygame.draw.line(screen,BLACK,(x+20,y-20),(x+20,y+10)) #left line
  pygame.draw.line(screen,BLACK,(x+20,y-20),(x+35,y-20)) #top line
  pygame.draw.line(screen,BLACK,(x+35,y-20),(x+35,y+10)) #right line
  pygame.draw.rect(screen,BROWN,(x+58,y-20,15,30)) #box color
  pygame.draw.line(screen,BLACK,(x+58,y-20),(x+58,y+8)) #left line
  pygame.draw.line(screen,BLACK,(x+58,y-20),(x+73,y-20)) #top line
  pygame.draw.line(screen,BLACK,(x+73,y-20),(x+73,y+8)) #right line
  pygame.draw.rect(screen,BROWN,(x+93,y-20,15,30)) #box color
  pygame.draw.line(screen,BLACK,(x+93,y-20),(x+93,y+9)) #left line
  pygame.draw.line(screen,BLACK,(x+93,y-20),(x+108,y-20)) #top line
  pygame.draw.line(screen,BLACK,(x+108,y-20),(x+108,y+8)) #right line
  pygame.draw.rect(screen,BROWN,(x+128,y-20,15,30)) #box color
  pygame.draw.line(screen,BLACK,(x+128,y-20),(x+128,y+9)) #left line
  pygame.draw.line(screen,BLACK,(x+128,y-20),(x+143,y-20)) #top line
  pygame.draw.line(screen,BLACK,(x+143,y-20),(x+143,y+8)) #right line
  pygame.draw.rect(screen,BROWN,(x+163,y-20,15,30)) #box color
  pygame.draw.line(screen,BLACK,(x+163,y-20),(x+163,y+9)) #left line
  pygame.draw.line(screen,BLACK,(x+163,y-20),(x+178,y-20)) #top line
  pygame.draw.line(screen,BLACK,(x+178,y-20),(x+178,y+8)) #right line

  #tower color
  pygame.draw.rect(screen,BROWN,(x,y+5,200,270))
  pygame.draw.ellipse(screen,BROWN,(x,y,200,10))
  pygame.draw.ellipse(screen,BROWN,(x,y+270,200,10))
  
  #curves on tower
  pygame.draw.arc(screen,BLACK,(x,y,200,20),math.radians(0),math.radians(180))
  pygame.draw.arc(screen,BLACK,(x,y+10,200,10),math.radians(180),math.radians(0))
  pygame.draw.arc(screen,BLACK,(x,y+30,200,10),math.radians(180),math.radians(0))
  pygame.draw.arc(screen,BLACK,(x,y+50,200,10),math.radians(180),math.radians(0))
  pygame.draw.arc(screen,BLACK,(x,y+70,200,10),math.radians(180),math.radians(0))
  pygame.draw.arc(screen,BLACK,(x,y+90,200,10),math.radians(180),math.radians(0))
  pygame.draw.arc(screen,BLACK,(x,y+110,200,10),math.radians(180),math.radians(0))
  pygame.draw.arc(screen,BLACK,(x,y+130,200,10),math.radians(180),math.radians(0))
  pygame.draw.arc(screen,BLACK,(x,y+150,200,10),math.radians(180),math.radians(0))
  pygame.draw.arc(screen,BLACK,(x,y+170,200,10),math.radians(180),math.radians(0))
  pygame.draw.arc(screen,BLACK,(x,y+190,200,10),math.radians(180),math.radians(0))
  pygame.draw.arc(screen,BLACK,(x,y+210,200,10),math.radians(180),math.radians(0))
  pygame.draw.arc(screen,BLACK,(x,y+230,200,10),math.radians(180),math.radians(0))
  pygame.draw.arc(screen,BLACK,(x,y+250,200,10),math.radians(180),math.radians(0))

  #Front boxes on top of tower
  pygame.draw.rect(screen,BROWN,(x,y-10,15,30)) #block colour
  pygame.draw.line(screen,BLACK,(x,y-10),(x+15,y-10)) #top line
  pygame.draw.line(screen,BLACK,(x+15,y-10),(x+15,y+17)) #right line
  pygame.draw.rect(screen,BROWN,(x+40,y-10,15,30)) #block colour
  pygame.draw.line(screen,BLACK,(x+40,y-10),(x+40,y+18)) #left line
  pygame.draw.line(screen,BLACK,(x+40,y-10),(x+55,y-10)) #top line
  pygame.draw.line(screen,BLACK,(x+55,y-10),(x+55,y+18)) #right line
  pygame.draw.rect(screen,BROWN,(x+75,y-10,15,30)) #block colour
  pygame.draw.line(screen,BLACK,(x+75,y-10),(x+75,y+19)) #left line
  pygame.draw.line(screen,BLACK,(x+75,y-10),(x+90,y-10)) #top line
  pygame.draw.line(screen,BLACK,(x+90,y-10),(x+90,y+18)) #right line
  pygame.draw.rect(screen,BROWN,(x+110,y-10,15,30)) #block colour
  pygame.draw.line(screen,BLACK,(x+110,y-10),(x+110,y+19)) #left line
  pygame.draw.line(screen,BLACK,(x+110,y-10),(x+125,y-10)) #top line
  pygame.draw.line(screen,BLACK,(x+125,y-10),(x+125,y+18)) #right line
  pygame.draw.rect(screen,BROWN,(x+145,y-10,15,30)) #block colour
  pygame.draw.line(screen,BLACK,(x+145,y-10),(x+145,y+19)) #left line
  pygame.draw.line(screen,BLACK,(x+145,y-10),(x+160,y-10)) #top line
  pygame.draw.line(screen,BLACK,(x+160,y-10),(x+160,y+18)) #right line
  pygame.draw.rect(screen,BROWN,(x+185,y-10,15,30)) #block colour
  pygame.draw.line(screen,BLACK,(x+185,y-10),(x+185,y+17)) #left line
  pygame.draw.line(screen,BLACK,(x+185,y-10),(x+200,y-10)) #top line

  #Side outlines of tower
  pygame.draw.line(screen,BLACK,(x,y-10),(x,y+275)) #Black line on the left
  pygame.draw.line(screen,BLACK,(x+200,y-10),(x+200,y+275)) #Black line on the left

  #Door
  pygame.draw.rect(screen,DOOR_BROWN,(x+60,y+180,75,100))
  pygame.draw.line(screen,BLACK,(x+60,y+180),(x+60,y+280)) #left outline
  pygame.draw.line(screen,BLACK,(x+135,y+180),(x+135,y+280)) #right outline
  pygame.draw.line(screen,BLACK,(x+75,y+180),(x+75,y+280)) #vertical line
  pygame.draw.line(screen,BLACK,(x+90,y+180),(x+90,y+280)) #vertical line
  pygame.draw.line(screen,BLACK,(x+105,y+180),(x+105,y+280)) #vertical line
  pygame.draw.line(screen,BLACK,(x+120,y+180),(x+120,y+280)) #vertical line

  #outline of base of tower
  pygame.draw.arc(screen,BLACK,(x,y+270,200,10),math.radians(180),math.radians(0))

  #Flag
  pygame.draw.line(screen,BLACK,(x+100,y+5),(x+100,y-65),2)
  pygame.draw.rect(screen,BLACK,(x+100,y-100,60,40),2)
  pygame.draw.rect(screen,BRIGHT_YELLOW,(x+102,y-97.5,56,36))
  #flower on flag
  pygame.draw.ellipse(screen,BLUE,(x+130,y-85,10,10)) #right petal
  pygame.draw.ellipse(screen,BLUE,(x+120,y-85,10,10)) #left petal
  pygame.draw.ellipse(screen,BLUE,(x+125,y-90,10,10)) #top petal
  pygame.draw.ellipse(screen,BLUE,(x+125,y-80,10,10)) #bottom petal
  pygame.draw.ellipse(screen,YELLOW,(x+125,y-85,10,10)) #flower middle
  
drawMidTower(x+75,y-60)

#Side tower windows
def drawWindow(x,y):
  pygame.draw.ellipse(screen,BLUE,(x,y-15,50,25))
  pygame.draw.arc(screen,BLACK,(x,y-15,50,25),math.radians(0),math.radians(180))
  pygame.draw.rect(screen,BLUE,(x,y,50,50))
  pygame.draw.line(screen,BLACK,(x+25,y-15),(x+25,y+50),3) #vertical line across window
  pygame.draw.line(screen,BLACK,(x,y+15),(x+50,y+15),3) #horizontal line across window
  #Window Outline
  pygame.draw.line(screen,BLACK,(x,y-5),(x,y+50))
  pygame.draw.line(screen,BLACK,(x+50,y-5),(x+50,y+50))
  pygame.draw.line(screen,BLACK,(x,y+50),(x+50,y+50))
 
drawWindow(x - 75,y + 25) #left tower
drawWindow(x + 375,y + 25) #right tower

#middle window
def drawWindow(x,y):
  pygame.draw.ellipse(screen,BLUE,(x-15,y-15,75,25))
  pygame.draw.rect(screen,BLUE,(x-15,y,75,50))
  pygame.draw.line(screen,BLACK,(x+22.5,y-15),(x+22.5,y+50),3) #vertical line across window
  pygame.draw.line(screen,BLACK,(x-15,y+15),(x+60,y+15),3) #horizontal line across window
  #Window Outline
  pygame.draw.arc(screen,BLACK,(x-15,y-15,75,25),math.radians(0),math.radians(180)) #top outline
  pygame.draw.line(screen,BLACK,(x-15,y-5),(x-15,y+50)) #left outline
  pygame.draw.line(screen,BLACK,(x+60,y-5),(x+60,y+50)) #right outline
  pygame.draw.line(screen,BLACK,(x-15,y+50),(x+60,y+50)) #bottom outline
drawWindow(x + 150,y + 25)


#Trees:
#Back 4 trees
def drawTree1(x,y):
  #Trunk
  pygame.draw.rect(screen,TREE_BROWN,(x,y,25,75))
  pygame.draw.polygon(screen,TREE_BROWN,((x,y+30),(x,y+75),(x-5,y+75)))
  pygame.draw.polygon(screen,TREE_BROWN,((x+25,y+35),(x+25,y+75),(x+30,y+75)))
  #Leaves
  pygame.draw.ellipse(screen,TREE_GREEN1,(x-10,y-40,60,60))
  pygame.draw.ellipse(screen,TREE_GREEN1,(x-20,y-52,30,30))
  pygame.draw.ellipse(screen,TREE_GREEN1,(x-30,y-45,30,30))
  pygame.draw.ellipse(screen,TREE_GREEN1,(x-25,y-25,30,30))
  pygame.draw.ellipse(screen,TREE_GREEN1,(x+35,y-25,30,30))
  pygame.draw.ellipse(screen,TREE_GREEN1,(x+28,y-50,30,30))
  pygame.draw.ellipse(screen,TREE_GREEN1,(x+10,y-60,30,30))
  pygame.draw.ellipse(screen,TREE_GREEN1,(x-10,y-65,30,30))
  pygame.draw.ellipse(screen,TREE_GREEN1,(x+28,y-10,30,30))
  pygame.draw.ellipse(screen,TREE_GREEN1,(x+15,y,30,30))
  pygame.draw.ellipse(screen,TREE_GREEN1,(x-10,y,30,30))
  pygame.draw.ellipse(screen,TREE_GREEN1,(x-25,y-10,30,30))
drawTree1(random.randint(33, 70),random.randint(290,330))
drawTree1(random.randint(130, 155),random.randint(290,330))
drawTree1(random.randint(810,830),random.randint(290,330))
drawTree1(random.randint(900,935),random.randint(290,330))

#Front 2 trees
def drawTree2(x,y):
  #Trunk
  pygame.draw.rect(screen,TREE_BROWN,(x,y,25,75))
  pygame.draw.polygon(screen,TREE_BROWN,((x,y+30),(x,y+75),(x-5,y+75)))
  pygame.draw.polygon(screen,TREE_BROWN,((x+25,y+35),(x+25,y+75),(x+30,y+75)))
  #Leaves
  pygame.draw.ellipse(screen,TREE_GREEN2,(x-10,y-40,60,60))
  pygame.draw.ellipse(screen,TREE_GREEN2,(x-20,y-52,30,30))
  pygame.draw.ellipse(screen,TREE_GREEN2,(x-30,y-45,30,30))
  pygame.draw.ellipse(screen,TREE_GREEN2,(x-25,y-25,30,30))
  pygame.draw.ellipse(screen,TREE_GREEN2,(x+35,y-25,30,30))
  pygame.draw.ellipse(screen,TREE_GREEN2,(x+28,y-50,30,30))
  pygame.draw.ellipse(screen,TREE_GREEN2,(x+10,y-60,30,30))
  pygame.draw.ellipse(screen,TREE_GREEN2,(x-10,y-65,30,30))
  pygame.draw.ellipse(screen,TREE_GREEN2,(x+28,y-10,30,30))
  pygame.draw.ellipse(screen,TREE_GREEN2,(x+15,y,30,30))
  pygame.draw.ellipse(screen,TREE_GREEN2,(x-10,y,30,30))
  pygame.draw.ellipse(screen,TREE_GREEN2,(x-25,y-10,30,30))
drawTree2(random.randint(85,110), random.randint(330,360))
drawTree2(random.randint(850,870),random.randint(330,360))

#Flowers
def drawFlower1(x,y):
  pygame.draw.ellipse(screen,flowerRandom1,(x+5,y,10,10)) #left petal
  pygame.draw.ellipse(screen,flowerRandom1,(x,y+5,10,10)) #bottom petal
  pygame.draw.ellipse(screen,flowerRandom1,(x,y-5,10,10)) #top petal
  pygame.draw.ellipse(screen,flowerRandom1,(x-5,y,10,10)) #right petal
  pygame.draw.ellipse(screen,YELLOW,(x+1,y,9,9)) #middle
  pygame.draw.line(screen,GREEN,(x+5,y+15),(x+5,y+25)) #stem
  pygame.draw.ellipse(screen,GREEN,(x-5,y+18,10,5)) #left leaf
  pygame.draw.ellipse(screen,GREEN,(x+5,y+15,10,5)) #right leaf
drawFlower1(random.randint(0, 1000),random.randint(530,670))
drawFlower1(random.randint(0, 1000),random.randint(530,670))
drawFlower1(random.randint(0, 1000),random.randint(530,670))
drawFlower1(random.randint(0, 1000),random.randint(530,670))
drawFlower1(random.randint(0, 1000),random.randint(530,670))

def drawFlower2(x,y):
  pygame.draw.ellipse(screen,flowerRandom2,(x+5,y,10,10)) #left petal
  pygame.draw.ellipse(screen,flowerRandom2,(x,y+5,10,10)) #bottom petal
  pygame.draw.ellipse(screen,flowerRandom2,(x,y-5,10,10)) #top petal
  pygame.draw.ellipse(screen,flowerRandom2,(x-5,y,10,10)) #right petal
  pygame.draw.ellipse(screen,YELLOW,(x+1,y,9,9)) #middle
  pygame.draw.line(screen,GREEN,(x+5,y+15),(x+5,y+25)) #stem
  pygame.draw.ellipse(screen,GREEN,(x-5,y+18,10,5)) #left leaf
  pygame.draw.ellipse(screen,GREEN,(x+5,y+15,10,5)) #right leaf
drawFlower2(random.randint(0, 1000),random.randint(530,670))
drawFlower2(random.randint(0, 1000),random.randint(530,670))
drawFlower2(random.randint(0, 1000),random.randint(530,670))
drawFlower2(random.randint(0, 1000),random.randint(530,670))
drawFlower2(random.randint(0, 1000),random.randint(530,670))

def drawFlower3(x,y):
  pygame.draw.ellipse(screen,flowerRandom3,(x+5,y,10,10)) #left petal
  pygame.draw.ellipse(screen,flowerRandom3,(x,y+5,10,10)) #bottom petal
  pygame.draw.ellipse(screen,flowerRandom3,(x,y-5,10,10)) #top petal
  pygame.draw.ellipse(screen,flowerRandom3,(x-5,y,10,10)) #right petal
  pygame.draw.ellipse(screen,YELLOW,(x+1,y,9,9)) #middle
  pygame.draw.line(screen,GREEN,(x+5,y+15),(x+5,y+25)) #stem
  pygame.draw.ellipse(screen,GREEN,(x-5,y+18,10,5)) #left leaf
  pygame.draw.ellipse(screen,GREEN,(x+5,y+15,10,5)) #right leaf
drawFlower3(random.randint(0, 1000),random.randint(530,670))
drawFlower3(random.randint(0, 1000),random.randint(530,670))
drawFlower3(random.randint(0, 1000),random.randint(530,670))
drawFlower3(random.randint(0, 1000),random.randint(530,670))
drawFlower3(random.randint(0, 1000),random.randint(530,670))

def drawBird(x,y):
  pygame.draw.arc(screen,BLACK,(x,y,20,15),math.radians(30),math.radians(170)) #left wing
  pygame.draw.arc(screen,BLACK,(x+15,y,20,15),math.radians(30),math.radians(170)) #right wing
drawBird(birdX1,birdY1)
drawBird(birdX2,birdY2)
drawBird(birdX3,birdY3)
drawBird(birdX4,birdY4)

pygame.display.flip()
pygame.time.wait(60000)
pygame.quit()
