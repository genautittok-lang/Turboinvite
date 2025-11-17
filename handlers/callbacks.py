from aiogram import types
from aiogram.filters import CallbackQuery
from keyboards import main_menu, language_menu
from texts import TEXTS
from utils import set_language, get_user

def register_callbacks(dp):
    @dp.callback_query(lambda c: c.data and c.data.startswith("lang_"))
    async def lang_choose(callback: types.CallbackQuery):
        lang = callback.data.split("_")[-1]
        user_id = callback.from_user.id
        set_language(user_id, lang)
        user = get_user(user_id)
        name = callback.from_user.full_name or callback.from_user.username or "User"
        text = TEXTS["welcome"][lang].format(name=name)
        await callback.message.edit_text(text, reply_markup=main_menu(lang))
        await callback.answer()  # close "loading" on client

    @dp.callback_query(lambda c: c.data == "menu")
    async def menu(callback: types.CallbackQuery):
        user = get_user(callback.from_user.id)
        lang = user["language"] if user else "EN"
        await callback.message.edit_text(TEXTS["menu_title"][lang], reply_markup=main_menu(lang))
        await callback.answer()

    @dp.callback_query(lambda c: c.data == "back")
    async def back(callback: types.CallbackQuery):
        user = get_user(callback.from_user.id)
        lang = user["language"] if user else "EN"
        await callback.message.edit_text(TEXTS["menu_title"][lang], reply_markup=main_menu(lang))
        await callback.answer()

    @dp.callback_query(lambda c: c.data == "balance")
    async def show_balance(callback: types.CallbackQuery):
        user = get_user(callback.from_user.id)
        lang = user["language"] if user else "EN"
        bal = user["balance"] if user else 0
        cur = user["currency"] if user else "USD"
        ref = user["referrals_count"] if user else 0
        await callback.message.answer(TEXTS["balance"][lang].format(bal=bal, cur=cur, ref=ref))
        await callback.answer()

    @dp.callback_query(lambda c: c.data == "earn")
    async def earn(callback: types.CallbackQuery):
        user = get_user(callback.from_user.id)
        lang = user["language"] if user else "EN"
        link = f"t.me/{callback.bot.username}?start={callback.from_user.id}"
        await callback.message.answer(TEXTS["earn_text"][lang].format(link=link))
        await callback.answer()

    @dp.callback_query(lambda c: c.data == "withdraw")
    async def withdraw_menu(callback: types.CallbackQuery):
        user = get_user(callback.from_user.id)
        lang = user["language"] if user else "EN"
        await callback.message.answer("Тут можна зробити вивід.\nНапиши /withdraw щоб створити запит.")
        await callback.answer()

    @dp.callback_query(lambda c: c.data == "support")
    async def support(callback: types.CallbackQuery):
        await callback.message.answer("📞 Support: contact admin or use /help")
        await callback.answer()
