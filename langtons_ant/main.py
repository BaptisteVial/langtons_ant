import pygame
from .simulation import Simulation
from .cmd_line import read_args

def run_gui(simulation, tile_size, ant_color, fps):
    """Runs the GUI visualization of Langton's Ant using pygame."""
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()

if __name__ == "__main__":
    args = read_args()
    'setup_logging(args.v)'
    sim = Simulation(args.steps_number)
    sim.run()
    with open(args.output, "w") as f:
        f.write(sim.get_state())

    if args.gui_mode != 0: # condition for launching the GUI mode
        run_gui(sim, args.tile_size, args.ant_color, args.fps) # where run_gui is still to be written...

def main()-> None:
    args = read_args()
    'setup_logging(args.v)'
    sim = Simulation(args.steps_number)
    if args.gui_mode != 0: # condition for launching the GUI mode
        run_gui(sim, args.tile_size, args.ant_color, args.fps) # where run_gui is still to be written...
    else :
        sim.run()
        print(sim.get_state())
    print('hasul')
    '''with open(args.output, "w") as f:
        f.write(sim.get_state())'''
