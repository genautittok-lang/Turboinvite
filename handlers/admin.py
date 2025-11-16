from aiogram.types import Message

def register_admin(dp):
    @dp.message(lambda m: m.text and m.from_user.id == 123456789 and m.text.startswith("/admin"))
    async def admin_panel(msg: Message):
        await msg.answer("Адмін-панель: підтвердження заявок, зміна цін, розсилка тощо. (Розширити)")
