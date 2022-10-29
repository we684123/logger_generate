import sys
import random
import string
import logging.handlers
from pathlib import Path

import coloredlogs


def _setConfig(logger_config: object,
               folderName: str,
               kwargs: object) -> object:

    # 如果沒有給 logger_config 就用預設的
    if logger_config is None:
        logger_config = {
            "logging_level": "DEBUG",  # DEBUG # INFO # ERROR # WARNING
            "log_file_path": f'./logs/{folderName}.log',
            "log_format": '%(asctime)s - %(levelname)s : %(message)s',
            "backupCount": 7,
            "when": 'D',
            "encoding": 'utf-8',
        }

    # 以下各種取 kwargs 來用
    if 'logging_level' in kwargs:
        logger_config['logging_level'] = kwargs['logging_level']

    if 'log_file_path' in kwargs:
        logger_config['log_file_path'] = kwargs['log_file_path']

    if 'log_format' in kwargs:
        logger_config['log_format'] = kwargs['log_format']

    if 'backupCount' in kwargs:
        logger_config['backupCount'] = kwargs['backupCount']

    if 'when' in kwargs:
        logger_config['when'] = kwargs['when']

    if 'encoding' in kwargs:
        logger_config['encoding'] = kwargs['encoding']

    return logger_config


def generate(logger_config=None,
             name='',
             need_serial=False,
             random_text_len=5,
             **kwargs):
    """生成 logger 用.

    可以使用預設的 logger_config 來快速生成 logger，也可以自己設定參數
    此外還會用 coloredlogs 來幫 log 上色

    Args:
        logger_config:
        預設長這樣
        {
            "logging_level": "DEBUG",  # DEBUG # INFO # ERROR # WARNING
            "log_file_path": f'./logs/{folderName}.log',
            "log_format": '%(asctime)s - %(levelname)s : %(message)s',
            "backupCount": 7,
            "when": 'D',
            "encoding": 'utf-8',
        }
        你可以做好一個 logger_config 直接傳入 function 取代

        name:
        生成出來的 logger 名稱，該名稱在執行環境中必須唯一存在，否則會重複紀錄。

        need_serial:
        如果怕 logger 名稱撞到，那可以把這個設為 True
        generate 時會在 logger 名稱後面自動加入 "_{隨機指定數量字元}" 來避開衝突

        random_text_len:
        如果有啟用 need_serial，則按 random_text_len 的指定隨機生成的字元數

        kwargs:
        讓你可以直接用 "generate(backupCount=14)" 這種參數輸入方式設定
        詳細

    Returns:
        有顏色的、設定過、可同時輸出至檔案跟 CLI 的 logger
    """

    folderName = Path().absolute().parts[-1]
    logger_config = _setConfig(logger_config, folderName, kwargs)

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
        rdt = ''.join(random.choice(string.ascii_letters + string.digits)
                      for x in range(random_text_len))
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
