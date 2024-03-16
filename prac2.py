import pygame
import random

pygame.init()

screen = pygame.display.set_mode((500,500))

clock = pygame.time.Clock()

x = 10
y = 20
speed = pygame.Vector2(x,y)

player_pro = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
dt = 0
r = 30
running = True

def random_color():
  """Generates a random color."""
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  return (r, g, b)



while running:
	screen.fill("yellow")
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	player_pro += speed * dt

	cir = pygame.draw.circle(screen, "red",(int(player_pro.x),int(player_pro.y)), r)
	pygame.cir.fill(random_color())

	if player_pro[0] > screen.get_width() - r:
		speed[0] = -x
	elif player_pro[1] > screen.get_height() - r:
		speed[1] = -y
	elif player_pro[0] < r:
		speed[0] = x
	elif player_pro[1] < r:
		speed[1] = y
	pygame.display.flip()



	dt = clock.tick(60) / 100