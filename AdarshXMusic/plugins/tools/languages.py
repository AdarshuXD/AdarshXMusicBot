from pykeyboard import InlineKeyboard
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, Message

from config import BANNED_USERS
from strings import get_command, get_string
from AdarshXMusic import app
from AdarshXMusic.utils.database import get_lang, set_lang
from AdarshXMusic.utils.decorators import ActualAdminCB, language, languageCB

# Languages Available


def lanuages_keyboard(_):
    keyboard = InlineKeyboard(row_width=2)
    keyboard.row(
        InlineKeyboardButton(
            text="🇦🇺 English 🇦🇺",
            callback_data=f"languages:en",
        ),
        InlineKeyboardButton(
            text="🇮🇳 हिन्दी 🇮🇳",
            callback_data=f"languages:hi",
        ),
    )
    keyboard.row(
        InlineKeyboardButton(
            text="🇱🇰 සිංහල 🇱🇰",
            callback_data=f"languages:si",
        ),
        InlineKeyboardButton(
            text="🇦🇿 Azərbaycan 🇦🇿",
            callback_data=f"languages:az",
        ),
    )
    keyboard.row(
        InlineKeyboardButton(
            text="🇮🇳 ગુજરાતી 🇮🇳",
            callback_data=f"languages:gu",
        ),
        InlineKeyboardButton(
            text="🇹🇷 Türkiye Türkçesi 🇹🇷",
            callback_data=f"languages:tr",
        ),
    )
    keyboard.row(
        InlineKeyboardButton(
            text="🐕 Cheems 🐕",
            callback_data=f"languages:cheems",
        ),
    )
    keyboard.row(
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"close"),
    )
    return keyboard


LANGUAGE_COMMAND = get_command("LANGUAGE_COMMAND")


@app.on_message(
    filters.command(LANGUAGE_COMMAND) & filters.group & ~filters.edited & ~BANNED_USERS
)
@language
async def langs_command(client, message: Message, _):
    keyboard = lanuages_keyboard(_)
    await message.reply_text(
        _["setting_1"].format(message.chat.title, message.chat.id),
        reply_markup=keyboard,
    )


@app.on_callback_query(filters.regex("LG") & ~BANNED_USERS)
@languageCB
async def lanuagecb(client, CallbackQuery, _):
    try:
        await CallbackQuery.answer()
    except:
        pass
    keyboard = lanuages_keyboard(_)
    return await CallbackQuery.edit_message_reply_markup(reply_markup=keyboard)


@app.on_callback_query(filters.regex(r"languages:(.*?)") & ~BANNED_USERS)
@ActualAdminCB
async def language_markup(client, CallbackQuery, _):
    langauge = (CallbackQuery.data).split(":")[1]
    old = await get_lang(CallbackQuery.message.chat.id)
    if str(old) == str(langauge):
        return await CallbackQuery.answer(
            "You're Already Using Same Language Gor This Chat.", show_alert=True
        )
    try:
        _ = get_string(langauge)
        await CallbackQuery.answer(
            "Successfully Changed Your Language.", show_alert=True
        )
    except:
        return await CallbackQuery.answer(
            "Failed To Change Language Or The Language Is Under Maintenance.",
            show_alert=True,
        )
    await set_lang(CallbackQuery.message.chat.id, langauge)
    keyboard = lanuages_keyboard(_)
    return await CallbackQuery.edit_message_reply_markup(reply_markup=keyboard)
