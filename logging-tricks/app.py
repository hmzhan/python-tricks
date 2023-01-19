import sys
from loguru import logger

logger.add(
    sys.stderr,
    format="{time:YYYY-MM-DD at HH:mm:ss} | {name} | {level} | {message}",
    level="INFO"
)


def do_something():
    x = 2*3
    logger.info("Do something")
    logger.error("Show an error")
    return x
