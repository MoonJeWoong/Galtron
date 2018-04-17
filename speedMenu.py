import sys

import pygame as pg

import sounds

image = pg.image.load('gfx/fixsetting4.png')
rect = image.get_rect()

# Create a variable to change current button being selected
def checkEvents(setting, screen, stats, sb, bMenu, ship, aliens, bullets, eBullets):
    """Respond to keypresses and mouse events."""
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
            # Check for key down has been pressed
        elif event.type == pg.KEYDOWN:
            # Check if down, up, enter, esc is pressed
            if event.key == pg.K_DOWN:
                sounds.control_menu.play()
                bMenu.down()
            elif event.key == pg.K_UP:
                sounds.control_menu.play()
                bMenu.up()
            elif event.key == pg.K_RETURN:
                sounds.select_menu.play()
                selectedName, selectedBtn = bMenu.getSelectedButton()
                if selectedBtn:
                    buttonAction(stats, selectedName, setting)
            elif event.key == pg.K_ESCAPE:
                sys.exit()

        elif event.type == pg.MOUSEMOTION:
            mouseBtnName, mouseBtn = bMenu.mouseCheck(event.pos[0], event.pos[1])
            if mouseBtn is not None:
                selectedName, selectedBtn = bMenu.getSelectedButton()
                if mouseBtn is not selectedBtn:
                    sounds.control_menu.play()
                    bMenu.selectByName(mouseBtnName)

        elif event.type == pg.MOUSEBUTTONDOWN:
            pressed = pg.mouse.get_pressed()
            if (pressed[0]):
                pos = pg.mouse.get_pos()
                mouseBtnName, mouseBtn = bMenu.mouseCheck(pos[0], pos[1])
                if mouseBtn is not None:
                    sounds.select_menu.play()
                    buttonAction(stats, mouseBtnName, setting)


def buttonAction(stats, selectedName, setting):
    if selectedName == 'fast':
        setting.gameSpeed = 'fast'
        stats.setGameLoop('settingsMenu')
    elif selectedName == 'middle':
        setting.gameSpeed = 'middle'
        stats.setGameLoop('settingsMenu')
    elif selectedName == 'slow':
        setting.gameSpeed = 'slow'
        stats.setGameLoop('settingsMenu')
    elif selectedName == 'menu':
<<<<<<< HEAD
<<<<<<< HEAD
         stats.setGameLoop('settingsMenu')

=======
=======
        stats.setGameLoop('settingsMenu')
>>>>>>> f85a50e374a3ee9445353e8a5660e311f34dfb26
=======
        stats.setGameLoop('settingsMenu')
>>>>>>> 1846737c17430f275f0bb7158e3868892f9209d5
    elif selectedName == 'quit':
        pg.time.delay(300)
        sys.exit()

def drawMenu(setting, screen, sb, bMenu):
    """Draw the menu and all of its elements"""
    global image, rect
    screen.fill(setting.bgColor)
    screen.blit(image, rect)
    bMenu.drawMenu()
    pg.display.flip()
