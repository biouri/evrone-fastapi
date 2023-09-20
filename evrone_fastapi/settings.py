"""
    Settings
"""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Settings Class
    """
    # Нужно задать значение по умолчанию,
    # если не будет установлена переменная среды окружения
    main_url: str = "/"

    # Это неработающий пример, возможно есть ошибка?
    # def __post_init__(self):
    #     if self.main_url is None:
    #         self.main_url = "/"


# Активируем переменные
settings = Settings()
# Так можно принудительно задать значения, вместо переменных среды окружения
# settings = Settings(main_url="/")
