import pygame
import sys

pygame.init()

pygame.font.init()

clock = pygame.time.Clock()

surface = pygame.display.set_mode((1777, 1000))
pygame.display.set_mode((1777, 1000))
pygame.display.set_caption("Encontre rua rota!")

def home_screen(surface):
  title_font = pygame.font.SysFont('Josefin Sans', 64)
  

  ship = pygame.image.load('assets/ship.png')
  ship = pygame.transform.scale(ship,(358,358))
  
  title_text = title_font.render('Encontre o melhor roteiro para seu navio', 1, (255, 194, 41))

  surface.blit(ship, (714, 439))
  surface.blit(title_text, (500, 327))

  pygame.display.update()

def background(surface):
  surface.fill((13, 59, 102))

  label_font = pygame.font.SysFont('Karla', 40)

  label_text = label_font.render('Partida', 1, (0, 0, 0))
  label_text2 = label_font.render('Destino', 1, (0, 0, 0))
  button_label = label_font.render('Todos a bordo!', 1, (255, 255, 255))
  button = pygame.image.load('assets/button.png')

  pygame.draw.rect(surface, (244, 211, 94), (0, 0, 1777, 235))
  
  surface.blit(label_text, (100,60))
  surface.blit(label_text2, (780,60))
  surface.blit(button, (1400,90))
  surface.blit(button_label, (1460,120))
  
  pygame.display.update()

def input_func(pos_x,pos_y, running):

  input_img = pygame.image.load('assets/input.png')

  input_box = pygame.Rect(pos_x, pos_y, 514, 60)
  color = pygame.Color(255,252,252)

  base_font = pygame.font.Font(None, 32)
  user_text = ''

  for event in pygame.event.get():
    
    if event.type == pygame.QUIT:
      running = False
      pygame.quit()
      sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
      if input_box.collidepoint(event.pos):
        active = True
      else:
        active = False

    if event.type == pygame.KEYDOWN:
      # Check for backspace
      if event.key == pygame.K_BACKSPACE:
        # get text input from 0 to -1 i.e. end.
        user_text = user_text[:-1]

      # Unicode standard is used for string
      # formation
      else:
        user_text += event.unicode
  
    surface.blit(input_img, (pos_x - 20, pos_y - 10))
    pygame.draw.rect(surface, color, input_box)

    text_surface = base_font.render(user_text, True, (0, 0, 0))

    surface.blit(text_surface, (input_box.x + 5, input_box.y+5))
    pygame.display.flip()

    clock.tick(1000)

active = False

def system():
  background(surface)
  home_screen(surface)
  
  running = True
  while running:
    for event in pygame.event.get():

    # if user types QUIT then the screen will close
      if event.type == pygame.QUIT:
        running = False
        pygame.quit()
        sys.exit()
    
    input_func(780,110, running)
    input_func(95,110, running)

system()



