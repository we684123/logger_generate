def logger_config():
    return {
        "logging_level": "DEBUG",  # DEBUG # INFO # ERROR # WARNING
        "log_file_path": './logs/example.log',
        "log_format": '%(asctime)s - %(levelname)s : %(message)s',
        "backupCount": 7,
        "when": 'D',
        "encoding": 'utf-8',
    }
