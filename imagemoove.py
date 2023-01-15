import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()            #get a pygame clock object
player = pygame.image.load('abstract-orange-pattern-pixel-background_322958-851.jpg').convert()
entity = pygame.image.load('images.jpg').convert()
background = pygame.image.load('new-product-500x500.webp').convert()
screen.blit(background, (0, 0))
objects = []
p = pygame.draw.Rect(player, 10, 3)          #create the player object
for x in range(10):                    #create 10 objects</i>
    o = pygame.draw.Rect(entity, x*40, x)
    objects.append(o)
while True:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        p.move(up=True)
    if keys[pygame.K_DOWN]:
        p.move(down=True)
    if keys[pygame.K_LEFT]:
        p.move(left=True)
    if keys[pygame.K_RIGHT]:
        p.move(right=True)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    for o in objects:
        screen.blit(background, o.pos, o.pos)
    for o in objects:
        o.move()
        screen.blit(o.image, o.pos)
    pygame.display.update()
    clock.tick(60)