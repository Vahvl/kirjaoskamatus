#algkood
import pygame
from random import *
from time import *
from math import *
pygame.font.init()
font = pygame.font.SysFont("Arial" , 54 , bold = True)
clock = pygame.time.Clock()
pilt = pygame.image.load("Programmeerimine\ohne.jpg")
import ctypes

myappid = 'sigmaco.gabmle.blessed.1'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

pygame.mixer.init()#rämmar muusika
pygame.mixer.music.load("Programmeerimine\loterii.mp3") #võtab ivo (the goat) linna plaadi välja
pygame.mixer.music.play()
tick = pygame.mixer.Sound("Programmeerimine\loterii.mp3")
 

pygame.display.set_icon(pilt)
a = b = c = kaotused = voidud = eep = 0
stopper = False
z=6
i = False
def refresh (a,b,c):
    ekr.fill(varv2)
    tekst(a, 640, 300, font, varv1)
    tekst(b, 960, 300, font, varv1)
    tekst(c, 1280, 300, font, varv1)
    tekst(f"Võidud: {voidud}", 960, 170, font, varv1)
    tekst(f"Kaotused: {kaotused}", 960, 230, font, varv1)
def gamba (x):
    global a, b, c, z, i, kaotused, voidud, eep
    eep = 0.1
    if i == False:
        for j in range (x):
            a = randint(1,z)
            b = randint(1,z)
            c = randint(1,z)
            sleep(eep)
            eep *= 1.15
            refresh(a,b,c)
            pygame.mixer.Sound.play(tick)
            ekr.blit(surface, (0,0))
            pygame.display.flip()
            print(a,b,c, "1!", "i:", i)
        if i == False:
            print(a,b,c, "2!")
            if a == b and b == c: 
                print("GAMBAAAAAAA")
                voidud += 1
                i = True
            else: 
                kaotused += 1
                
#gamba(10)
print("sigma")
#pygame setup värgid
pygame.init()
pygame.display.set_caption("Rahapada")
ekr = pygame.display.set_mode((1920, 1000))
jutt = "fdsgh"
def tekst(tekst, x, y, font, varv):
    bla = font.render(str(tekst), True, varv)
    text_rect = bla.get_rect(center=(x, y))
    ekr.blit(bla, text_rect)

#äppi tsükkel
too = True
while too== True:
    for event in pygame.event.get(): #kontrollib ristikest
        if event.type == pygame.QUIT:
            too == False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("vajutus")
                gamba(10)
    varv1 = (152, 122, 159)
    varv2 = (47, 76, 57)
    ekr.fill(varv2)
    surface = pygame.Surface((1920,1000))
    graye = (200,200,200)
    surface.fill(graye)
    surface.set_colorkey(graye)
    varv4 = (190, 227, 186)
    varv3 = (126, 89, 135)
    recta = pygame.Rect(540, 360, 200, 200)
    rectb = pygame.Rect(860, 360, 200, 200)
    rectc = pygame.Rect(1180, 360, 200, 200)
    rectd = pygame.Rect(0, 0, 100, 1000)
    recte = pygame.Rect(1820, 0, 100, 1000)

    pygame.draw.rect(surface, varv4, recta, width=200, border_radius=10)
    pygame.draw.rect(surface, varv4, rectb, width=200, border_radius=10)
    pygame.draw.rect(surface, varv4, rectc, width=200, border_radius=10)
    pygame.draw.rect(surface, varv3, rectd, width=100)
    pygame.draw.rect(surface, varv3, recte, width=200)

    refresh(a,b,c)
    tekst(f"Kaotused: {kaotused}", 960, 230, font, varv1)
    tekst(f"Võidud: {voidud}", 960, 170, font, varv1)
    if i == True:
        tekst(f"Võit!!!!!! Võimalus: {round((kaotused+1)/z**2*100, 7)}%", 960, 600, font, varv1)
    clock.tick(5000)
    #print(clock.get_fps())
    ekr.blit(surface, (0,0))
    pygame.display.flip()
pygame.quit()