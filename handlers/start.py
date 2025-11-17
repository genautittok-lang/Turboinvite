from aiogram import types
from aiogram.filters import CommandStart
from keyboards import main_menu, language_menu
from utils import add_user, update_balance

def register_start(dp):
    # --- Команда /start ---
    @dp.message(CommandStart())
    async def start_handler(msg: types.Message):
        user_id = msg.from_user.id
        username = msg.from_user.username or msg.from_user.first_name
        add_user(user_id, username)

        # Перевірка рефералів
        if "?start=" in msg.text:
            ref_id = msg.text.split("=")[-1]
            if ref_id.isdigit() and int(ref_id) != user_id:
                update_balance(int(ref_id), 0.25)  # Бонус USD

        # Надсилаємо кнопки вибору мови
        await msg.answer(
            "Оберіть мову / Select your language / Выберите язык",
            reply_markup=language_menu()
        )

    # --- Обробник натискання кнопок мови ---
    @dp.callback_query()
    async def language_callback(callback: types.CallbackQuery):
        lang_code = callback.data  # lang_ua, lang_en, lang_ru
        await callback.answer()  # Обов'язково, щоб Telegram не крутив "loading"

        # Визначаємо мову для меню
        lang = lang_code.split("_")[-1].upper()

        # Надсилаємо головне меню
        await callback.message.edit_text(
            "Мову вибрано!" if lang == "UA" else
            "Language selected!" if lang == "EN" else
            "Язык выбран!",
            reply_markup=main_menu(lang=lang)
        )
