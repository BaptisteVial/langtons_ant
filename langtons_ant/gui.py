import pygame
import pygame_menu
from .simulation import Simulation
from .dir import Dir

def run_gui(simulation: Simulation, tile_size: int, ant_color: str, fps: int):
    """Runs the GUI visualization of Langton's Ant using pygame."""
    pygame.init()
    screen_size = [800, 600]
    menu_width = 150  # Width of the menu
    screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
    screen.fill((255, 255, 255))
    pygame.display.set_caption("Langton's Ant Simulation")
    clock = pygame.time.Clock()
    
    ant = simulation._ant
    grid = simulation._grid
    
    # Scrollbar setup (positioned on the right side)
    menu = pygame_menu.Menu(
    "Scroll", 150, screen_size[1], 
    theme=pygame_menu.themes.THEME_DARK, 
    position=(1.0, 0, True)  # 1.0 means 100% (right edge), True means absolute positioning
)

    scroll_x = menu.add.range_slider("Scroll X", 0, (-1000, 1000), 1)
    scroll_y = menu.add.range_slider("Scroll Y", 0, (-1000, 1000), 1)
    
    running = True
    step = 0

    while running and step < simulation._steps:
        screen.fill((255, 255, 255))  # Clear screen

        # Get all events
        events = pygame.event.get()
        
        # Update menu (check if it handles an event)
        if menu.is_enabled() and menu.update(events):
            menu.draw(screen)
            pygame.display.flip()
            continue  # Skip simulation update to allow UI interaction

        # Process pygame events
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                screen_size = event.size
                screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
                menu.resize(150, screen_size[1])  

        # Get scrollbar values
        scroll_x_val = int(scroll_x.get_value())
        scroll_y_val = int(scroll_y.get_value())

        # Update simulation
        x, y = ant.position
        turn_right = grid.is_white(x, y)
        ant.turn(turn_right)
        grid.flip_tile(x, y)
        ant.move()

        # Calculate offsets for scrolling
        ant_x, ant_y = ant.position
        offset_x = screen_size[0] // 2 - ant_x * tile_size + scroll_x_val
        offset_y = screen_size[1] // 2 - ant_y * tile_size + scroll_y_val

        # Draw grid and ant
        for (tile_x, tile_y) in grid.get_black_tiles():
            pygame.draw.rect(
                screen, (0, 0, 0),
                pygame.Rect(offset_x + tile_x * tile_size, offset_y + tile_y * tile_size, tile_size, tile_size)
            )

        # Draw red triangle (ant)
        center_x = offset_x + ant_x * tile_size + tile_size // 2
        center_y = offset_y + ant_y * tile_size + tile_size // 2

        if ant.direction == Dir.UP:
            ant_shape = [(center_x, center_y - tile_size // 2), 
                        (center_x - tile_size // 3, center_y + tile_size // 3), 
                        (center_x + tile_size // 3, center_y + tile_size // 3)]
        elif ant.direction == Dir.DOWN:
            ant_shape = [(center_x, center_y + tile_size // 2), 
                        (center_x - tile_size // 3, center_y - tile_size // 3), 
                        (center_x + tile_size // 3, center_y - tile_size // 3)]
        elif ant.direction == Dir.LEFT:
            ant_shape = [(center_x - tile_size // 2, center_y), 
                        (center_x + tile_size // 3, center_y - tile_size // 3), 
                        (center_x + tile_size // 3, center_y + tile_size // 3)]
        elif ant.direction == Dir.RIGHT:
            ant_shape = [(center_x + tile_size // 2, center_y), 
                        (center_x - tile_size // 3, center_y - tile_size // 3), 
                        (center_x - tile_size // 3, center_y + tile_size // 3)]

        pygame.draw.polygon(screen, (255, 0, 0), ant_shape)

        # Draw menu
        menu.draw(screen)

        # Update window title with step and position
        pygame.display.set_caption(f"Langton's Ant - Step {step+1} | Position: ({ant_x}, {ant_y})")

        # Refresh display
        pygame.display.flip()
        clock.tick(fps)
        step += 1

    # Simulation finished -> Wait for user input before closing
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # User clicked the red cross
                waiting = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # User pressed space
                waiting = False

    pygame.quit()
