WIDTH = 800
HEIGHT = 600
player_x = 500
player_y = 550

def draw():
  screen.blit(images.backdrop, (0, 0))
  # puts ship behind Mars
  screen.blit(images.ship, (130, 150))
  screen.blit(images.mars, (50, 50))