
import asyncio

import speedtest

from strings import command
from YukkiMusic import app
from YukkiMusic.misc import SUDOERS


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("⇆ درحال تست سرعت دانلود ...")
        test.download()
        m = m.edit("⇆ درحال تست سرعت آپلود...")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("↻ به اشتراک گذاری سرعت ")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(command("SPEEDTEST_COMMAND",prefixes=["", "/"]) & SUDOERS)
async def speedtest_function(client, message):
    m = await message.reply_text("ʀᴜɴɴɪɴɢ sᴘᴇᴇᴅᴛᴇsᴛ")
    loop = asyncio.get_event_loop_policy().get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""**Speedtest Results**
    
<u>**کلاینت:**</u>
**ارائه دهنده سرویس :** {result['client']['isp']}
**Country :** {result['client']['country']}
  
<u>**سرور:**</u>
**نام :** {result['server']['name']}
**شرکت:** {result['server']['country']}, {result['server']['cc']}
**پشتیبان:** {result['server']['sponsor']}
**Latency:** {result['server']['latency']}  
**پینگ :** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, photo=result["share"], caption=output
    )
    await m.delete()
