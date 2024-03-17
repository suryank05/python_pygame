import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))

clock = pygame.time.Clock()

x = 200
y = 200
speed = pygame.Vector2(x,y)

player_pro = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
dt = 0
r = 30
running = True
while running:
	screen.fill("black")
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	player_pro += speed * dt

	circle = pygame.draw.circle(screen, "red",(int(player_pro.x),int(player_pro.y)), r)
	key=pygame.key.get_pressed()
	if key[pygame.K_w]:
		player_pro.y -= 10 + dt
	if key[pygame.K_s]:
		player_pro.y += 10 + dt
	if key[pygame.K_a]:
		player_pro.x -= 10 + dt
	if key[pygame.K_q]:
		pygame.quit()
	if key[pygame.K_d]:
	    player_pro.x += 10 + dt
	

	if player_pro.x > (screen.get_width()) + (r):
		player_pro.x = 0-r
	if player_pro.y > (screen.get_height()) + (r):
		player_pro.y = 0-r	

	if player_pro.x >= screen.get_width()-r:
		speed *= -1
	if player_pro.y >= screen.get_height()-r:
		speed *= -1

		



	pygame.display.flip()

	dt = clock.tick(60) / 1000   



pygame.quit	