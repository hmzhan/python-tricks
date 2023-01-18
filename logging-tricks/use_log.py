import sys
from loguru import logger
from app import do_something

# logger.add("app.log")
logger.add(
    "app.log",
    format="{time:YYYY-MM-DD at HH:mm:ss} | {name} | {level} | {message}",
    level="INFO"
)

logger.add(
    "error.log",
    format="{time:YYYY-MM-DD at HH:mm:ss} | {name} | {level} | {message}",
    level="ERROR"
)

do_something()

logger.info("info test")
logger.debug("debug test")
logger.error("error test")
logger.critical("critical test")
