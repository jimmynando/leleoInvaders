import pygame

pygame.init()
w, h = 400, 700
screen = pygame.display.set_mode((w, h))

done = False
direction = 0

lx, ly = (w * 0.5), (h * 0.85)
leleo = pygame.image.load('./images/leleo.jpg')

raio = []
ry = []
rx = []
tirinho = []

enemy = []
ey = []
ex = []
qntEnemy = w / 90
linhasEnemy = 3
deadBiro = []

clock = pygame.time.Clock()

countDownEnemy = 0
downEnemy = 0

for l in range(linhasEnemy):
    for e in range(qntEnemy):
        enemy.append(pygame.image.load('./images/biroliro.jpg'))
        ex.append((e * 98) + 10)
        ey.append((l * 77) + 10)
        deadBiro.append(False)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                raio.append(pygame.image.load('./images/raio.png'))
                tirinho.append(True)
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
    if direction == "RIGHT":
        if lx <= 320:
            lx += 10
            direction = ""

    for l in range(linhasEnemy):
        for e in range(len(enemy)):
            enemyIn = e - 1
            if deadBiro[enemyIn] == False:
                screen.blit(enemy[enemyIn],
                            (ex[enemyIn], (ey[enemyIn] + downEnemy)))

    if (len(raio) - 1) >= 0:
        for shoot in range(len(raio)):
            shootIn = shoot - 1
            screen.blit(raio[shootIn], (rx[shootIn], ry[shootIn]))
            if len(tirinho) > 0:
                if tirinho[shootIn] == True:
                    ry[shootIn] -= 10
                    for l in range(linhasEnemy):
                        for e in range(len(enemy)):
                            enemyIn = e - 1
                            if (ry[shootIn] - 70) <= ey[enemyIn] and (
                                    rx[shootIn] >= ex[enemyIn]
                                    and rx[shootIn] <= ex[enemyIn] + 90
                            ) and deadBiro[enemyIn] == False:
                                deadBiro[enemyIn] = True

                    if ry[shootIn] <= 0:
                        del raio[shootIn]
                        del tirinho[shootIn]
                        del rx[shootIn]
                        del ry[shootIn]

    countDownEnemy += 1
    if countDownEnemy == 60:
        countDownEnemy = 0
        downEnemy += 5

    screen.blit(leleo, (lx, ly))

    clock.tick(60)
    pygame.display.update()
