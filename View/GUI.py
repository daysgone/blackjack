import sys
from View import UI
import pygame
from pygame.locals import *
pygame.init()  # TODO needed?
# window properties
(width, height) = (1024, 768)
background_color = (255, 255, 255)

screen = pygame.display.set_mode((width, height), HWSURFACE | DOUBLEBUF | RESIZABLE)
pygame.display.set_caption("Blackjack")
screen.fill(background_color)
pygame.mouse.set_cursor(*pygame.cursors.arrow)

# default card info
card_path = "cards/"


# how many players?


def scale(w, h, x, y, maximum=True):
    """
    scale image so proportions will be either at most or at least the given one
    :param w: incoming width
    :param h: incoming height
    :param x: outgoing width
    :param y: outgoing height
    :param maximum: if False will resize to make width match x
                    if True it will fit in box of x/y
    :return: scaled values (x,y)
    """
    nw = y * w/h
    nh = x * h/w
    if maximum ^ (nw >= x):
        return nw or 1, y
    return x, nh or 1


def build_card(cardvalue, player):
    card = pygame.image.load(card_path + "%s_of_%s.png" % cardvalue)
    cardrect = card.get_rect()
    card = pygame.transform.smoothscale(card, scale(cardrect.width, cardrect.height, 180, 180))
    return card, cardrect

# this should be passed in my controller
cardvalue = ('ace', 'diamonds')
player1_pos = (60, 60)

card, cardrect = build_card(cardvalue, 'player1')

cardrect = cardrect.move(player1_pos)
# get new card
#
# card1 = pygame.image.load("cards/ace_of_clubs.png")
# cardrect1 = card1.get_rect()
# x, y = scale(cardrect1.width, cardrect1.height, 180, 180)  # get orig image size to scale correctly
# card1 = pygame.transform.smoothscale(card1, (x, y))
# cardrect1 = cardrect1.move(60, 60)


while 1:
    # look for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # is this needed?
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            print "mouse clocked at (%d,%d)" % event.pos
        elif event.type == MOUSEBUTTONDOWN and event.button == 3:
            print("Right Button Pressed")
        '''
        elif event.type == VIDEORESIZE:
            screen = pygame.display.set_mode(event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
            screen.blit(pygame.transform.scale(card, event.dict['size']), (0, 0))
            pygame.display.flip()
        '''

    screen.blit(card, cardrect)
   # screen.blit(card1, cardrect1)

    pygame.display.flip()  # display in window
    pygame.display.update()

    '''
    cardrect = cardrect.move(speed)
    if cardrect.left < 0 or cardrect.right > width:
        speed[0] = -speed[0]
    if cardrect.top < 0 or cardrect.bottom > height:
        speed[1] = -speed[1]
    '''


