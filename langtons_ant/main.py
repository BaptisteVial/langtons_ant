import colorlog
import logging
import sys

from .simulation import Simulation
from .dir import Dir
from .cmd_line import read_args
from .gui import run_gui

if __name__ == "__main__":
    args = read_args()
    'setup_logging(args.v)'
    sim = Simulation(row = 0, colon = 0, direction = Dir.UP, steps = args.steps_number)
    sim.run()
    with open(args.output, "w") as f:
        f.write(sim.get_state())

    if args.gui_mode != 0: # condition for launching the GUI mode
        run_gui(sim, args.tile_size, args.ant_color, args.fps)


# Set up color logger
logger = logging.getLogger("LangtonsAnt")
color_fmt = colorlog.ColoredFormatter(
    "%(log_color)s[%(asctime)s][%(levelname)s] %(message)s",
    log_colors={
        "DEBUG": "yellow",
        "INFO": "green",
        "WARNING": "purple",
        "ERROR": "red",
        "CRITICAL": "red",
    },
)

color_handler = colorlog.StreamHandler()
color_handler.setFormatter(color_fmt)
logger.addHandler(color_handler)
logger.setLevel(logging.DEBUG)  # Set the logging level

def main()-> None:
    args = read_args()
    'setup_logging(args.v)'
    sim = Simulation(row = 0, colon = 0, direction = Dir.UP, steps = args.steps_number)
    if args.gui_mode != 0: # condition for launching the GUI mode
        run_gui(sim, args.tile_size, args.ant_color, args.fps)
    else :
        sim.run()
        print(sim.get_state())
    print('Done')

