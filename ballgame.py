import pygame

pygame.init()

WHITE = (255, 255, 255)
DARKBLUE = (36, 90, 190)
LIGHTBLUE = (0, 176, 240)
RED = (255, 0, 0)


bricks1 = [pygame.Rect(10 + i * 100, 60, 80, 30) for i in range(6)]
bricks2 = [pygame.Rect(10 + i * 100,  100, 80, 30) for i in range(6)]
bricks3 = [pygame.Rect(10 + i * 100, 140, 80, 30) for i in range(6)]


def print_wall(bricks):
    '''to draw bricks'''
    for brick in bricks:
        pygame.draw.rect(screen, WHITE, brick)


SCORE = 0

HEALTH = 3

speed = [1, 1]

size = (600, 600)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Ball Game")

paddle = pygame.Rect(250, 570, 100, 10)
ball = pygame.Rect(50, 250, 15, 10)


bgcolor = pygame.image.load('new-product-500x500.webp')
bg_transformed = pygame.transform.scale(bgcolor, (600, 600))


sound = pygame.mixer.Sound('file_example_WAV_1MG.wav')
sound.set_volume(5)
sound.play()

GAMELOOP = True

while GAMELOOP:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAMELOOP = False

    screen.blit(bg_transformed, (0, 0))

    pygame.draw.rect(screen, LIGHTBLUE, paddle)

    scoretext = pygame.font.Font(None, 40).render(
        "SCORE " + str(SCORE), True, RED, DARKBLUE)

    livestext = pygame.font.Font(None, 40).render(
        "Lives"+str(HEALTH), True,
        RED, DARKBLUE)

    screen.blit(scoretext, (20, 10))
    screen.blit(livestext, (400, 10))

    # paddle move:
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            if paddle.x < 540:
                paddle.x = paddle.x + 5

        if event.key == pygame.K_LEFT:
            if paddle.x > 0:
                paddle.x = paddle.x - 5

    # creating bricks
    print_wall(bricks1)
    print_wall(bricks2)
    print_wall(bricks3)
    # ball movement
    ball.x = ball.x + speed[0]
    ball.y = ball.y + speed[1]

    if ball.x > 590 or ball.x < 0:
        sound.set_volume(0)
        speed[0] = -speed[0]
        sound.set_volume(5)

    if ball.y <= 3:
        sound.set_volume(0)
        speed[1] = -speed[1]
        sound.set_volume(5)

    if paddle.collidepoint(ball.x, ball.y):
        sound.set_volume(0)

        speed[1] = -speed[1]
        sound.set_volume(5)

    if ball.y >= 590 and HEALTH != 0:
        sound.set_volume(0)
        HEALTH -= 1
        SCORE = 0
        paddle = pygame.Rect(250, 570, 100, 10)
        ball = pygame.Rect(50, 250, 15, 10)
        screen.blit(bg_transformed, (0, 0))
        pygame.display.flip()
        sound.set_volume(1)

    if ball.y >= 590 and HEALTH == 0:
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over ", 1, RED)

        screen.fill((255, 255, 255))

        screen.blit(text, (150, 250))

        pygame.display.flip()

        pygame.time.wait(2000)

        break

    pygame.draw.rect(screen, RED, ball)

    for i in bricks1:
        if i.collidepoint(ball.x, ball.y):
            sound.set_volume(0)
            bricks1.remove(i)
            speed[0] = -speed[0]
            speed[1] = -speed[1]
            SCORE = SCORE + 1

    for i in bricks2:
        if i.collidepoint(ball.x, ball.y):
            sound.set_volume(0)
            bricks2.remove(i)
            speed[0] = -speed[0]
            speed[1] = -speed[1]
            SCORE = SCORE + 1

    for i in bricks3:
        if i.collidepoint(ball.x, ball.y):
            bricks3.remove(i)
            sound.set_volume(0)
            speed[0] = -speed[0]
            speed[1] = -speed[1]
            SCORE = SCORE + 1

    if SCORE == 18:
        font = pygame.font.Font(None, 74)
        text = font.render("YOU WON ", 1, RED)
        screen.blit(text, (150, 350))
        pygame.display.flip()

        pygame.time.wait(3000)
        break
    pygame.time.wait(1)
    pygame.display.flip()

pygame.quit()
