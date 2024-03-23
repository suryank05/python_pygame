import pygame
import pygame.font

running = True

def main_menu():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Main Menu")
    running = True
    

    font = pygame.font.Font(None, 74)
    text_play = font.render("Play", True, (255, 0, 0))
    text_play_rect = text_play.get_rect(center=(400, 300))
    text_quit = font.render("Quit", True, (255, 0, 0))
    text_quit_rect = text_quit.get_rect(center=(400, 400))

    while running:

      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_play_rect.collidepoint(event.pos):
                    print("play is clicked pressed")
                if text_quit_rect.collidepoint(event.pos):
                    print("quit button is clicked")
                    pygame.quit()

        screen.fill((0, 0, 255))
        screen.blit(text_play, text_play_rect)
        screen.blit(text_quit, text_quit_rect)
        rectangle = pygame.Rect(300, 250, 200, 80)

        # Set the border color
        border_color = (255,255,255)

        pygame.draw.rect(screen, border_color, rectangle, 1)

        rectangle1=pygame.Rect(300,350,200,80)
        border_color1=(255,255,255)
        pygame.draw.rect(screen,border_color1,rectangle1,1)

        pygame.display.flip()

main_menu()
pygame.quit()
