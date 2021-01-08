from config import base
from library.logger_generate import generate

logger = generate(base.logger_config())
logger.info("A")

logger = generate(base.logger_config(), "ex_B")
logger.info("B")

logger = generate(base.logger_config(), name='ex_C')
logger.info("C")

logger = generate(base.logger_config(), "ex", True)
logger.info("D")

logger = generate(base.logger_config(), need_serial=True)
logger.info("E")

logger = generate(base.logger_config(), name='ex_F', need_serial=True)
logger.info("F")
