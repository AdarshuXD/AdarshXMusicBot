from pyrogram import filters

import config
from strings import get_command
from AdarshXMusic import app
from AdarshXMusic.misc import SUDOERS
from AdarshXMusic.utils.database import autoend_off, autoend_on
from AdarshXMusic.utils.decorators.language import language

# Commands
AUTOEND_COMMAND = get_command("AUTOEND_COMMAND")


@app.on_message(filters.command(AUTOEND_COMMAND) & SUDOERS)
async def auto_end_stream(client, message):
    usage = "**Usage:**\n\n/autoend [enable|disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "Auto End Stream Enabled.\n\nAssistant Will Automatically Leave The Video Chat After Few Mins When No One Is Listening With A Warning Message."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("Auto End Stream Disabled.")
    else:
        await message.reply_text(usage)
