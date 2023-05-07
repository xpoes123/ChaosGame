import pygame
import time
import random
#global vars
width = 1500
height = 750
cur = [200,100]

green1= (170,255,0)
green4 = (9,121,105)
green3 = (75, 225, 175)
green5 = (80, 200, 120)
green2 = (0, 233, 0)
green6 = (79, 121, 66)
green7 = (34, 139, 34)
green8 = (124, 252, 0)
green9 = (53, 94, 59)
green10 = (42, 170, 138)
green11 = (144, 238, 144)
white = (0,0,0)
colors = [green1, green2, green3, green4, green5,green6,green7,green8,green9,green10,green11]

points = []
crazy = (int)(input("Do you want to be crazy?? (1-yes 0-no)"))
if crazy == 1:
    numPoints = (int)(input("How many points do you want to start with?"))
    randomQ = (int)(input("Do you want randomly generated points? (1-yes 0-no)"))
    if(randomQ == 0):
        for i in range(numPoints):
            xt = (int)(input("What do you want your " + str(i) + "-points x coordinate to be? (20-900)"))
            yt = (int)(input("What do you want your " + str(i) + "-points y coordinate to be? (20-700)"))
            points.append((xt,yt))
    else:
        for i in range(numPoints):
            points.append((random.randint(20,900),random.randint(20,700)))
    factor = (int)(input("What scale factor (n) do you want? (1/n)"))
else:
    numPoints = (int)(input("How many points do you want to start with?"))
    if numPoints == 3:
        points.append((50,50))
        points.append((600,50))
        points.append((325, 500))
        factor = 2
    if numPoints == 4:
        factor = 2
        points.append((50,50))
        points.append((600,600))
        points.append((50,600))
        points.append((600,50))

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width,height))
butt1 = pygame.image.load('butt1.png').convert_alpha()
butt2 = pygame.image.load('butt2.png').convert_alpha()
dots = pygame.image.load('dots.png').convert_alpha()
class Button():
    def __init__(self, x, y, image):
        image = pygame.transform.scale(image, (width*.1, height*.1))
        self.image = image
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                time.sleep(.2)
            else:
                self.clicked = False
        screen.blit(self.image,(self.rect.x, self.rect.y))
        return action

but1 = Button(1000,20,butt1)
but2 = Button(1000,120,butt2)
but3 = Button(1000,220,dots)

animation = True
x = random.randint(50, 750)
y = random.randint(50, 500)
currP = (x,y)
newPoints = [currP]
lastChoice = (0,0)
while animation:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animation = False
    screen.fill(white)
    if but1.draw():
        draw1 = True
    else:
        draw1 = False
    if but2.draw():
        draw50 = True
    else:
        draw50 = False
    if but3.draw():
        drawing = True
    else:
        drawing = False
    for i in points:
        pygame.draw.circle(screen, green2, i, 3)
    if draw1:
        randPoint = random.choice(points)
        x = (x+randPoint[0])/factor
        y = (y+randPoint[1])/factor
        newPoints.append((x,y))
    if draw50:
        for i in range(50):
        # time.sleep(0.01)
            randPoint = random.choice(points)
            x = (x+randPoint[0])/2
            y = (y+randPoint[1])/2
            newPoints.append((x,y))
    if drawing:
        for i in range(500):
            randPoint = random.choice(points)
            x = (x+randPoint[0])/2
            y = (y+randPoint[1])/2
            newPoints.append((x,y))
    for i in newPoints:
        pygame.draw.circle(screen, random.choice(colors), i,1)
    pygame.display.update()