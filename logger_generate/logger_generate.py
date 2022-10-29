import sys
import random
import string
import logging.handlers
from pathlib import Path

import coloredlogs


def generate(logger_config=None, name='', need_serial=False, **kwargs):
    """
    logger_config is like to
    {
        "logging_level": "INFO",  # DEBUG # INFO # ERROR # WARNING
        "log_file_path": './logs/{folderName}.log',
        "log_format": '%(asctime)s - %(levelname)s : %(message)s',
        "backupCount": 7,
        "when": 'D',
        "encoding": 'utf-8',
    }

    need_serial just a boolean
    if True, will generate have serial logger
    """

    folderName = Path().absolute().parts[-1]
    if logger_config is None:
        # 如果沒有給 logger_config
        if 'logging_level' in kwargs:
            logging_level = kwargs['logging_level']
        else:
            logging_level = "INFO"

        logger_config = {
            "logging_level": logging_level,
            "log_file_path": f'./logs/{folderName}.log',
            "log_format": '%(asctime)s - %(levelname)s : %(message)s',
            "backupCount": 7,
            "when": 'D',
            "encoding": 'utf-8',
        }

    if 'need_serial' in kwargs:
        need_serial = kwargs['need_serial']

    log_file_path = Path(logger_config['log_file_path']).absolute()
    parts = log_file_path.parts
    parts_inherit = Path().absolute()
    for part in parts[:-1]:
        # 除了最後一個是log檔，其他的上層資料夾都要確保存在
        if not (parts_inherit := parts_inherit / part).exists():
            # 資料夾不存在就建
            parts_inherit.mkdir()

    if name == '':
        name = folderName
    if need_serial:
        rdt_len = 5
        rdt = ''.join(random.choice(string.ascii_letters + string.digits)
                      for x in range(rdt_len))
        logger = logging.getLogger(f"{name}_{rdt}")
    else:
        logger = logging.getLogger(name)
    handler1 = logging.StreamHandler(sys.stdout)
    handler2 = logging.handlers.TimedRotatingFileHandler(
        filename=logger_config['log_file_path'],
        when=logger_config['when'],
        encoding=logger_config['encoding'],
        backupCount=logger_config['backupCount'],
    )
    formatter = logging.Formatter(logger_config['log_format'])
    handler1.setFormatter(formatter)
    handler2.setFormatter(formatter)

    logging_level = logger_config['logging_level']
    logger.setLevel(logging_level)
    handler1.setLevel(logging_level)
    handler2.setLevel(logging_level)

    logger.addHandler(handler1)
    logger.addHandler(handler2)

    coloredlogs.install(level=logging_level, logger=logger)
    return logger
    #  ===== logger設定完畢 =====
