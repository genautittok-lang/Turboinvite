from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

def register_withdraw(dp):
    dp.include_router(router)

@router.message(Command("withdraw"))
async def withdraw_menu(message: Message):
    await message.answer(
        "💳 *Вивід коштів*\n\n"
        "Мінімальні суми:\n"
        "• 🇺🇸 0.25 USD\n"
        "• 🇺🇦 10 грн\n"
        "• 🇷🇺 25 RUB\n\n"
        "Виберіть метод виводу:",
        parse_mode="Markdown"
    )

