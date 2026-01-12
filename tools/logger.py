import logging



def get_logger(name: str) -> logging.Logger:

    logger = logging.getLogger(name=name)   # Инициализация логгера с указанным именем
    logger.setLevel(logging.DEBUG)          # Устанавливаем уровень логирования DEBUG

    handler = logging.StreamHandler()       # Создаем обработчик, который будет выводить логи в консоль
    handler.setLevel(logging.DEBUG)         # Устанавливаем уровень логирования DEBUG, чтобы обрабатывал сообщения от DEBUG и выше

    # Задаем форматирование лог-сообщений: включаем время, имя логгера, уровень и сообщение
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    handler.setFormatter(fmt=formatter)     # Применяем форматтер к обработчику

    logger.addHandler(hdlr=handler)         # Добавляем обработчик к логгеру

    return logger