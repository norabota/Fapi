from typing import Final
import os
from dotenv import load_dotenv

load_dotenv()


class TgKeys:
    TOKEN = str(os.getenv("TOKEN"))
    DB_USER = str(os.getenv("DB_USER"))
    DB_PASS = str(os.getenv("DB_PASS"))
    DB_NAME = str(os.getenv("DB_NAME"))
    host = str(os.getenv("HOST"))

# class TgKeys:
#     TOKEN: Final = "5759627481:AAF1PSq3MTOU8H1SDdcedIKqTPiVl3Zz5ug"
#     DB_USER: Final = "physics"
#     DB_PASS: Final = "rootroot"
#     DB_NAME: Final = "gino"
#     host = "localhost"
