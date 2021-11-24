import asyncio
from pytgcalls import idle
from driver.shasa import call_py, bot

async def mulai_bot():
    print("[SHASA]: STARTING BOT CLIENT")
    await bot.start()
    print("[SHASA]: STARTING PYTGCALLS CLIENT")
    await call_py.start()
    await idle()
    await pidle()
    print("[SHASA]: STOPPING BOT & USERBOT")
    await bot.stop()

loop = asyncio.get_event_loop()
loop.run_until_complete(mulai_bot())
