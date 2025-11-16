import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME", "TurboInviteBot")
ADMIN_ID = int(os.getenv("ADMIN_ID", 123456789))
DEFAULT_CURRENCY = "USD"

MIN_WITHDRAW = {
    "USD": 50,
    "UAH": 500,
    "RUB": 1000
}
