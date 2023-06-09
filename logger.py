from loguru import logger

logger.add('info.log', format= "{time} {level} {message}",
           rotation = "00:00", level = "INFO")
