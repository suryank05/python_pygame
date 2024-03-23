import pygame
import math

pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Slingshot ball")
# color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# constants
FPS = 60
Gravity = 0.1

# sling properties
slingshot_pos = (200, HEIGHT - 100)
slingshot_radius = 30
pull_back_length = 100

# slingshot mechanics variables
is_pulling_back = False
pull_back_distance = 0
angle = 0

# ball properties
ball_radius = 20
ball_color = RED
ball_pos = pygame.Vector2(slingshot_pos)
ball_velocity = pygame.Vector2(0, 0)

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                is_pulling_back = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                is_pulling_back = False
                ball_speed = min(pull_back_distance, pull_back_length) * 0.1
                angle_radians = math.radians(angle)
                ball_velocity = pygame.Vector2(
                    ball_speed * math.cos(angle_radians),
                     ball_speed * math.sin(angle_radians),
                )
                pull_back_distance = 0

    if is_pulling_back:
        mouse_pos = pygame.mouse.get_pos()
        pull_back_distance = -min(
            math.sqrt((mouse_pos[0] - slingshot_pos[0]) ** 2
                      + (mouse_pos[1] - slingshot_pos[1]) ** 2),
            pull_back_length,
        )
        angle = math.degrees(
            math.atan2(slingshot_pos[1] - mouse_pos[1],
                       slingshot_pos[0] - mouse_pos[0]),
        )

    pygame.draw.circle(screen, BLACK, slingshot_pos, slingshot_radius)
    pygame.draw.line(
        screen,
        BLACK,
        slingshot_pos,
        (
            slingshot_pos[0] + pull_back_distance * math.cos(math.radians(angle)),
            slingshot_pos[1] + pull_back_distance * math.sin(math.radians(angle)),
        ),
        2,
    )

    pygame.draw.circle(screen, ball_color, (int(ball_pos.x), int(ball_pos.y)),
                ball_radius)

    # Update ball position
    ball_pos += ball_velocity
    ball_velocity.y += Gravity  # Apply gravity

    # If ball reaches ground, reset position and velocity
    if ball_pos.y >= HEIGHT - ball_radius:
        ball_pos.y = HEIGHT - ball_radius
   #     ball_velocity *= -0.7  # Dampen velocity upon collision with the ground

    # If ball goes beyond screen boundaries, reset position and velocity
    if ball_pos.x < -ball_radius or ball_pos.x > WIDTH + ball_radius:
        ball_pos = pygame.Vector2(slingshot_pos)
        ball_velocity = pygame.Vector2(0, 0)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
