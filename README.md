# logger_generate
生成logger用的，清涼舒爽

```python
from config import base
from library.logger_generate import generate

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
![2022-10-02 23_32_45-README md — C__Users_we684123_Dropbox_各類專案_Github_logger_generate — Atom](https://user-images.githubusercontent.com/22027801/193462753-a5456909-28d5-449e-b8dc-5e1648ab87d0.png)
