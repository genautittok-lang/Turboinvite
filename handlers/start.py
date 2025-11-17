from aiogram import types
from aiogram.filters import CommandStart
from keyboards import main_menu, language_menu
from utils import add_user, update_balance

USER_LANG = {}

def register_start(dp):

    @dp.message(CommandStart())
    async def start_handler(msg: types.Message):
        user_id = msg.from_user.id
        username = msg.from_user.username or msg.from_user.first_name
        add_user(user_id, username)

        if "?start=" in msg.text:
            ref_id = msg.text.split("=")[-1]
            if ref_id.isdigit() and int(ref_id) != user_id:
                update_balance(int(ref_id), 0.25)

        await msg.answer(
            "Оберіть мову / Select your language / Выберите язык",
            reply_markup=language_menu()
        )

    @dp.callback_query(lambda c: c.data.startswith("lang_"))
    async def language_callback(callback: types.CallbackQuery):
        user_id = callback.from_user.id
        await callback.answer()

        lang = callback.data.split("_")[-1].upper()
        USER_LANG[user_id] = lang

        username = callback.from_user.username or callback.from_user.first_name

        greetings = {
            "UA": f"👋 Привіт, {username}!\nТи в TurboInviteBot!\n\nТут можна:\n💸 Заробляти за друзів\n🚀 Розкручувати свій канал\n⭐ Купувати Telegram Stars\n💳 Виводити гроші",
            "EN": f"👋 Hello, {username}!\nYou are in TurboInviteBot!\n\nHere you can:\n💸 Earn from friends\n🚀 Promote your channel\n⭐ Buy Telegram Stars\n💳 Withdraw money",
            "RU": f"👋 Привет, {username}!\nТы в TurboInviteBot!\n\nЗдесь можно:\n💸 Зарабатывать на друзьях\n🚀 Продвигать свой канал\n⭐ Покупать Telegram Stars\n💳 Выводить деньги"
        }

        await callback.message.edit_text(
            greetings[lang],
            reply_markup=main_menu(lang=lang)
        )

    @dp.callback_query(lambda c: c.data in ["balance","withdraw","earn","promo","stars","settings","support"])
    async def main_menu_callback(callback: types.CallbackQuery):
        user_id = callback.from_user.id
        lang = USER_LANG.get(user_id, "EN")
        await callback.answer()

        data = callback.data

        responses = {
            "balance": {
                "UA": "Ваш баланс: 0 USD\nЗапрошено користувачів: 0",
                "EN": "Your balance: 0 USD\nUsers invited: 0",
                "RU": "Ваш баланс: 0 USD\nПриглашено пользователей: 0"
            },
            "withdraw": {
                "UA": "Тут можна зробити вивід.",
                "EN": "Here you can make a withdraw.",
                "RU": "Здесь можно сделать вывод."
            },
            "earn": {
                "UA": "Тут можна заробляти. Використовуйте своє реферальне посилання!",
                "EN": "Here you can earn. Use your referral link!",
                "RU": "Здесь можно зарабатывать. Используйте вашу реферальную ссылку!"
            },
            "promo": {
                "UA": "Тут можна розкручувати канали.",
                "EN": "Here you can promote channels.",
                "RU": "Здесь можно продвигать каналы."
            },
            "stars": {
                "UA": "Купити Telegram Stars можна тут.",
                "EN": "You can buy Telegram Stars here.",
                "RU": "Купить Telegram Stars можно здесь."
            },
            "settings": {
                "UA": "Налаштування бота.",
                "EN": "Bot settings.",
                "RU": "Настройки бота."
            },
            "support": {
                "UA": "Підтримка користувачів.",
                "EN": "User support.",
                "RU": "Поддержка пользователей."
            }
        }

        if data in responses:
            await callback.message.answer(responses[data][lang])
