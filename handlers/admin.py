from aiogram import types
from config import ADMIN_ID
from database import get_connection

def register_admin(dp):
    @dp.message(lambda m: m.from_user.id == ADMIN_ID and m.text.startswith("/withdraws"))
    async def list_withdraws(msg: types.Message):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM withdraw_requests WHERE status = 'pending'")
        rows = cur.fetchall()
        if not rows:
            await msg.reply("No pending withdraws.")
            conn.close()
            return
        text = "Pending withdraws:\n"
        for r in rows:
            text += f"ID: {r['id']} user:{r['user_id']} amount:{r['amount']} {r['currency']} method:{r['method']} details:{r['details']}\n"
        conn.close()
        await msg.reply(text)

    @dp.message(lambda m: m.from_user.id == ADMIN_ID and m.text.startswith("/approve"))
    async def approve(msg: types.Message):
        parts = msg.text.split()
        if len(parts) < 2:
            await msg.reply("Usage: /approve <id>")
            return
        req_id = parts[1]
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("UPDATE withdraw_requests SET status = 'approved' WHERE id = ?", (req_id,))
        conn.commit()
        conn.close()
        await msg.reply(f"Request {req_id} approved.")

    @dp.message(lambda m: m.from_user.id == ADMIN_ID and m.text.startswith("/decline"))
    async def decline(msg: types.Message):
        parts = msg.text.split()
        if len(parts) < 2:
            await msg.reply("Usage: /decline <id>")
            return
        req_id = parts[1]
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("UPDATE withdraw_requests SET status = 'declined' WHERE id = ?", (req_id,))
        conn.commit()
        conn.close()
        await msg.reply(f"Request {req_id} declined.")
