
from loguru import logger

logger.add("app.log")


def do_something():
    x = 2*3
    logger.info("Do something")
    logger.error("Show an error")
    return x
