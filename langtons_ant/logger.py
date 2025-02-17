import logging

def setup_logging(verbosity: int):
    """Configures logging based on verbosity level."""
    level = logging.WARNING - (verbosity * 10)
    logging.basicConfig(level=max(level, logging.DEBUG), format="%(levelname)s: %(message)s")
