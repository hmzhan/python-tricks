
from loguru import logger
from app import do_something

logger.add("app.log")

do_something()

logger.info("info test")
logger.debug("debug test")
logger.error("error test")
