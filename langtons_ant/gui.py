# gui.py
import pygame
import pygame_menu
from .simulation import Simulation
from .dir import Dir

def run_gui(simulation: Simulation, tile_size: int, ant_color: str, fps: int):
    """Runs the GUI visualization of Langton's Ant using pygame."""
    pygame.init()
    screen_size = 800, 600
    screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
    screen.fill((255, 255, 255))
    pygame.display.set_caption("Langton's Ant Simulation")
    clock = pygame.time.Clock()
    
    ant = simulation._ant
    grid = simulation._grid
    
    # Scrollbar setup
    menu = pygame_menu.Menu("Scroll", 200, 200, theme=pygame_menu.themes.THEME_DARK)
    scroll_x = menu.add.range_slider("Scroll X", 0, -1000, 1000, 1)
    scroll_y = menu.add.range_slider("Scroll Y", 0, -1000, 1000, 1)
    
    running = True
    step = 0

    
    while running and step < simulation._steps:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                screen_size = event.size
                screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
        
        # Update simulation
        x, y = ant.position
        turn_right = grid.is_white(x, y)
        ant.turn(turn_right)
        grid.flip_tile(x, y)
        ant.move()
        
        # Get new position
        ant_x, ant_y = ant.position
        offset_x = screen_size[0] // 2 - ant_x * tile_size + int(scroll_x.get_value())
        offset_y = screen_size[1] // 2 - ant_y * tile_size + int(scroll_y.get_value())
        
        # Draw black tiles
        for (tile_x, tile_y) in grid.get_black_tiles():
            pygame.draw.rect(
                screen, (0, 0, 0), 
                pygame.Rect(offset_x + tile_x * tile_size, offset_y + tile_y * tile_size, tile_size, tile_size)
            )
        
        # Draw ant with direction
        ant_rect = pygame.Rect(offset_x + ant_x * tile_size, offset_y + ant_y * tile_size, tile_size, tile_size)
        pygame.draw.rect(screen, pygame.Color(ant_color), ant_rect)
        
        # Draw direction indicator
        center = ant_rect.center
        if ant.direction == Dir.UP:
            pygame.draw.polygon(screen, (255, 0, 0), [(center[0], center[1] - tile_size//2), (center[0] - tile_size//3, center[1] + tile_size//3), (center[0] + tile_size//3, center[1] + tile_size//3)])
        elif ant.direction == Dir.DOWN:
            pygame.draw.polygon(screen, (255, 0, 0), [(center[0], center[1] + tile_size//2), (center[0] - tile_size//3, center[1] - tile_size//3), (center[0] + tile_size//3, center[1] - tile_size//3)])
        elif ant.direction == Dir.LEFT:
            pygame.draw.polygon(screen, (255, 0, 0), [(center[0] - tile_size//2, center[1]), (center[0] + tile_size//3, center[1] - tile_size//3), (center[0] + tile_size//3, center[1] + tile_size//3)])
        elif ant.direction == Dir.RIGHT:
            pygame.draw.polygon(screen, (255, 0, 0), [(center[0] + tile_size//2, center[1]), (center[0] - tile_size//3, center[1] - tile_size//3), (center[0] - tile_size//3, center[1] + tile_size//3)])
        
        # Update display
        pygame.display.set_caption(f"Langton's Ant - Step {step}")
        pygame.display.update()
        clock.tick(fps)
        step += 1
    
    pygame.quit()

