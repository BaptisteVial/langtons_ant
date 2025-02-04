# Standard
import argparse
import re

# Third party
import pygame

# First party
from .exceptions import ColorError, IntRangeError

def read_args() -> argparse.Namespace:
    """Read command line arguments."""
    # Create parser & set description
    parser = argparse.ArgumentParser(
            description="Langton's Ant simulation.",
            formatter_class = argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--steps_number", "-N", type = int, default= 10,
                        help="Set the number of steps that must be processed.")
    parser.add_argument("--output", "-o", type=str, help="Path to output file.")
    parser.add_argument("-v", action="count", default=0, help="Enable verbose logging.")
    parser.add_argument("gui_mode", "-G", type = int , default=0, help="Enable GUI mode if a non-nil value is entered.")
    parser.add_argument("--tile-size", type=int, default=10, help="Size of each square tile in pixels (GUI mode).")
    parser.add_argument("--ant-color", type=str, default="red", help="Color of the ant in GUI mode.")
    parser.add_argument("--fps", type=int, default=10, help="Frames per second in GUI mode.")

    # Parse
    args = parser.parse_args()
    return args