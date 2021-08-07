import pygame
import sys
import button

pygame.init()

pygame.font.init()

clock = pygame.time.Clock()

surface = pygame.display.set_mode((1777, 1000))

pygame.display.set_caption("Encontre sua rota!")


def home_screen(surface):
  title_font = pygame.font.SysFont('Josefin Sans', 64)
  
  ship = pygame.image.load('assets/ship.png')
  ship = pygame.transform.scale(ship,(358,358))
  
  title_text = title_font.render('Encontre o melhor roteiro para seu navio', 1, (255, 194, 41))

  surface.blit(ship, (714, 439))
  surface.blit(title_text, (500, 327))

  pygame.display.update()

def background(surface):
  global search_button
  surface.fill((13, 59, 102))

  label_font = pygame.font.SysFont('Karla', 40)

  btn_img = pygame.image.load('assets/button.png').convert_alpha()
  search_button = button.Button(1400, 90, btn_img, 1)

  label_text = label_font.render('Partida', 1, (0, 0, 0))
  label_text2 = label_font.render('Destino', 1, (0, 0, 0))
  global button_label
  button_label = label_font.render('Todos a bordo!', 1, (255, 255, 255))


  pygame.draw.rect(surface, (244, 211, 94), (0, 0, 1777, 235))
  
  surface.blit(label_text, (100,60))
  surface.blit(label_text2, (780,60))

  pygame.display.update()


def system():
  background(surface)
  home_screen(surface)
  
  while True:
    if search_button.draw(surface):
      print('FOI')
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    surface.blit(button_label, (1460,120))
    pygame.display.update()
    

system()



