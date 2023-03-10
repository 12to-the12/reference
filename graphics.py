import pygame
import pygame.gfxdraw

pygame.init()
h_res, v_res = 1280,720
surface = pygame.display.set_mode((h_res, v_res))

clock = pygame.time.Clock()
while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Do logical updates here.
    # ...

    surface.fill("purple")  # Fill the display with a solid color
    # Render the graphics here.
    # ...
    color = (255,255,255)
    pygame.gfxdraw.aapolygon(surface, ((200, 300), (400, 300), (600, 700)), color)

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)