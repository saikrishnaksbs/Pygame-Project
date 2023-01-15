import pygame

pygame.init()

score=0

health=5

velocity=[1,1]
 
red= (255,0,0)

black=(0,255,0)

white= (0,0,255)


screen=pygame.display.set_mode((600,600)) 

bricks1=[pygame.Rect(10+(i*100), 60,80,30) for i in range(7)]
bricks2=[pygame.Rect(10+(i*100), 100,80,30) for i in range(7)]
bricks3=[pygame.Rect(10+(i*100), 140,80,30) for i in range(7)]



def draw(bricks):
    for brick in bricks:
        pygame.draw.rect(screen,white,brick)
        
background=pygame.image.load('new-product-500x500.webp')
transformedimage=pygame.transform.scale(background,(600,600))

paddle = pygame.Rect(250, 570, 100, 10)
ball = pygame.Rect(50, 250, 15, 10)

pygame.display.set_caption("Ball game")

sound = pygame.mixer.Sound('file_example_WAV_1MG.wav')
sound.set_volume(5)
sound.play()

gameloop=True

while gameloop:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameloop=False
            break
    
    
    screen.blit(transformedimage,(0,0))
    pygame.draw.rect(screen, red, paddle)
    pygame.draw.rect(screen, black, ball)
    draw(bricks1)
    draw(bricks2)
    draw(bricks3)
    ball.x = ball.x + velocity[0]
    ball.y = ball.y + velocity[1]
    if event.type == pygame.KEYDOWN:
        if event.key== pygame.K_LEFT:
            paddle.x = paddle.x - 5
        if event.key== pygame.K_RIGHT:
            paddle.x = paddle.x + 5
    if paddle.collidepoint(ball.x,ball.y):
        velocity[1]=-velocity[1]
    if ball.x>590 or ball.x<3:
        velocity[0]=-velocity[0]
    if ball.y<=3:
        velocity[1]=-velocity[1]
    if ball.y>595 and health!=0:
        health-=1
        score=0
        paddle = pygame.Rect(250, 570, 100, 10)
        ball = pygame.Rect(50, 250, 15, 10)
        screen.blit(transformedimage, (0, 0))
        pygame.display.flip()
    if ball.y>595 and health==0:
        
        text = font = pygame.font.Font(None, 60).render("Game Over ", 1, red)

        screen.fill((255, 255, 255))

        screen.blit(text, (150, 350))

        pygame.display.flip()

        pygame.time.wait(2000)

        GAMELOOP = False
        
    if score == 18:

        text = pygame.font.Font(None, 60).render("YOU WON ", 1, red)
        screen.blit(text, (150, 350))
        pygame.display.flip()

        pygame.time.wait(3000)
        GAMELOOP = False
    for brick in bricks1:
        if brick.collidepoint(ball.x,ball.y):
            bricks1.remove(brick)
            velocity[0]=-velocity[0]
            velocity[1]=-velocity[1]
    for brick in bricks2:
        if brick.collidepoint(ball.x,ball.y):
            bricks2.remove(brick)
            velocity[0]=-velocity[0]
            velocity[1]=-velocity[1]
    for brick in bricks3:
        if brick.collidepoint(ball.x,ball.y):
            bricks3.remove(brick)
            velocity[0]=-velocity[0]
            velocity[1]=-velocity[1]    
    pygame.time.wait(1)
    pygame.display.flip()
    