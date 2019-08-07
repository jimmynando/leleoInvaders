import pygame

pygame.init()
sx, sy = 400, 700
screen = pygame.display.set_mode((sx, sy))

done = False
direction = 0

lx, ly = (sx * 0.5), (sy * 0.85)
leleo = pygame.image.load('./images/leleo.jpg')

raio = []
ry = []
rx = []
shootC = 0
tirinho = []

clock = pygame.time.Clock()

raio.append(pygame.image.load('./images/raio.png'))
tirinho.append(True)
shootC = len(raio) - 1
ry.append(ly)
rx.append(lx + 28)

cx, cy = 0, 0
cop = []
copCounter = 0

for i in range(10):
    cop.append(pygame.image.load('./images/cop.png'))
    copCounter = i

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                raio.append(pygame.image.load('./images/raio.png'))
                tirinho.append(True)
                shootC = len(raio) - 1
                ry.append(ly)
                rx.append(lx + 28)

    pressed = pygame.key.get_pressed()
    screen.fill((255, 255, 255))

    if pressed[pygame.K_LEFT]:
        direction = "LEFT"
    if pressed[pygame.K_RIGHT]:
        direction = "RIGHT"

    if direction == "LEFT":
        if lx >= 10:
            lx -= 10
            direction = ""
            rx[shootC] = lx + 28
    if direction == "RIGHT":
        if lx <= 320:
            lx += 10
            direction = ""
            rx[shootC] = lx + 28

    if len(raio) > 0:
        print(len(raio), ry)
        for shoot in range(shootC):
            screen.blit(raio[shoot], (rx[shoot], ry[shoot]))
            if len(tirinho) > 0:
                if tirinho[shoot] == True:
                    ry[shoot] -= 10
                    if ry[shoot] < 0:
                        del raio[shoot]
                        del tirinho[shoot]
                        del rx[shoot]
                        del ry[shoot]
                        shootC -= 1

    screen.blit(leleo, (lx, ly))
    for i in range(copCounter):
        if i < 5:
            screen.blit(cop[i], (i * 85, 1))
        else:
            screen.blit(cop[i], ((i - 5) * 95, 90))

    clock.tick(60)
    pygame.display.update()
