import sys
from loguru import logger
from app import do_something

# logger.add("app.log")
logger.add(
    "app.log",
    format="{time} | {name} | {level} | {message}",
    level="INFO"
)

do_something()

logger.info("info test")
logger.debug("debug test")
logger.error("error test")
logger.critical("critical test")
