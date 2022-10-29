# logger_generate

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/26699f09d35542bcb96c9d0164e27a1e)](https://www.codacy.com/gh/we684123/logger_generate/dashboard?utm_source=github.com&utm_medium=referral&utm_content=we684123/logger_generate&utm_campaign=Badge_Grade)

生成 logger 用的，清涼舒爽  
開箱即用的 logger。

A python package  
easy to generate logger.

## Install

pip
```bash
pip install -U logger-generate
```

poetry
```bash
poetry add logger-generate
```


## Example

```python
from config import base
from logger_generate import generate

logger = generate()
logger.info("引入即用 ( •̀ ω •́ )✧")

logger_config = {
    "logging_level": 'DEBUG',
    "log_file_path": './logs/by_logger_config.log',
    "log_format": '%(asctime)s - %(levelname)s : %(message)s',
    "backupCount": 7,
    "when": 'D',
    "encoding": 'utf-8',
}
logger = generate(logger_config, name='from_dict')
logger.info("亦可用程式內 dict 設定")

logger = generate(base.logger_config(), "from_config_file")
logger.info("也以用從檔案引入 config")

logger = generate(logger_config, name='方便生成隨機log名稱', need_serial=True)
logger.info("←後方隨機5字元")

logger = generate(base.logger_config(), "ex", True)
logger.info("示範單純用位置作為輸入手段")
```

![2022-10-29 22_38_04-logger_generate @ z170_hero](https://user-images.githubusercontent.com/22027801/198837773-27f1a516-c99a-4518-86e9-42ff9c4faab0.png)

