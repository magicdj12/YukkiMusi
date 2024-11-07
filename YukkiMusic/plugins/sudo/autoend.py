from strings import command
from YukkiMusic import app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.utils.database import autoend_off, autoend_on


@app.on_message(command("AUTOEND_COMMAND",prefixes=["", "/"]) & SUDOERS)
async def auto_end_stream(client, message):
    usage = "**ᴜsᴀɢᴇ:**\n\n/autoend [enable|disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "ختم خودکا.\n\nربات ویس چت را ترک میکند اگر یکی گوش کند.."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("Autoend disabled")
    else:
        await message.reply_text(usage)
