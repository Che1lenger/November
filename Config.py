from dataclasses import dataclass


@dataclass
class DatabaseConfig:
    db_host: str         # URL-адреса бази данних
    db_user: str         # Username користувача бази данних
    db_password: str     # Пароль до бази данних
    database: str        # Назва бази данних


    @dataclass
    class TgBot:
        token: str             # Токен для доступу до телеграм-бота
        admin_ids: list[int]   # Список id адміністраторів бота


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig
