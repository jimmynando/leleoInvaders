import pygame
from model.Player import Player

pygame.init()
w, h = 400, 700
screen = pygame.display.set_mode((w, h))

done = False
direction = 0

player = Player(pygame.image.load('./images/leleo.jpg'), (w * 0.5), (h * 0.85))

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
                ry.append(player.y)
                rx.append(player.x + 28)

    pressed = pygame.key.get_pressed()
    screen.fill((255, 255, 255))

    player.move(pressed)

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
                            if (ry[shootIn] - 100) <= ey[enemyIn] and (
                                    rx[shootIn] >= ex[enemyIn]
                                    and rx[shootIn] <= ex[enemyIn] + 90
                            ) and deadBiro[enemyIn] == False:
                                deadBiro[enemyIn] = True
                                del raio[shootIn]
                                del tirinho[shootIn]
                                del rx[shootIn]
                                del ry[shootIn]
                                break
                        break
                    if shootIn >= 0:
                        if ry[shootIn] <= 0:
                            del raio[shootIn]
                            del tirinho[shootIn]
                            del rx[shootIn]
                            del ry[shootIn]

    countDownEnemy += 1
    if countDownEnemy == 60:
        countDownEnemy = 0
        downEnemy += 5

    screen.blit(player.sprite, (player.x, player.y))

    clock.tick(60)
    pygame.display.update()
    pygame.display.set_caption('Killing Bozo')
