import asyncio

from pyrogram import filters

import config
from strings import get_command
from AdarshXMusic import app
from AdarshXMusic.misc import SUDOERS
from AdarshXMusic.utils.database.memorydatabase import get_video_limit
from AdarshXMusic.utils.formatters import convert_bytes

VARS_COMMAND = get_command("VARS_COMMAND")


@app.on_message(filters.command(VARS_COMMAND) & SUDOERS)
async def varsFunc(client, message):
    mystic = await message.reply_text("Please Wait, Adarsh ....Getting Your Config Variables...")
    v_limit = await get_video_limit()
    bot_name = config.MUSIC_BOT_NAME
    up_r = f"[Repo]({config.UPSTREAM_REPO})"
    up_b = config.UPSTREAM_BRANCH
    auto_leave = config.AUTO_LEAVE_ASSISTANT_TIME
    yt_sleep = config.YOUTUBE_DOWNLOAD_EDIT_SLEEP
    tg_sleep = config.TELEGRAM_DOWNLOAD_EDIT_SLEEP
    playlist_limit = config.SERVER_PLAYLIST_LIMIT
    fetch_playlist = config.PLAYLIST_FETCH_LIMIT
    song = config.SONG_DOWNLOAD_DURATION
    play_duration = config.DURATION_LIMIT_MIN
    cm = config.CLEANMODE_DELETE_MINS
    auto_sug = config.AUTO_SUGGESTION_TIME
    if config.AUTO_LEAVING_ASSISTANT == str(True):
        ass = "ʏᴇs"
    else:
        ass = "ɴᴏ"
    if config.PRIVATE_BOT_MODE == str(True):
        pvt = "ʏᴇs"
    else:
        pvt = "ɴᴏ"
    if config.AUTO_SUGGESTION_MODE == str(True):
        a_sug = "ʏᴇs"
    else:
        a_sug = "ɴᴏ"
    if config.AUTO_DOWNLOADS_CLEAR == str(True):
        down = "ʏᴇs"
    else:
        down = "ɴᴏ"

    if not config.GITHUB_REPO:
        git = "ɴᴏ"
    else:
        git = f"[Repo]({config.GITHUB_REPO})"
    if not config.START_IMG_URL:
        start = "ɴᴏ"
    else:
        start = f"[Image]({config.START_IMG_URL})"
    if not config.SUPPORT_CHANNEL:
        s_c = "ɴᴏ"
    else:
        s_c = f"[Channel]({config.SUPPORT_CHANNEL})"
    if not config.SUPPORT_GROUP:
        s_g = "ɴᴏ"
    else:
        s_g = f"[Support]({config.SUPPORT_GROUP})"
    if not config.GIT_TOKEN:
        token = "No"
    else:
        token = "Yes"
    if not config.SPOTIFY_CLIENT_ID and not config.SPOTIFY_CLIENT_SECRET:
        sotify = "No"
    else:
        sotify = "Yes"
    owners = [str(ids) for ids in config.OWNER_ID]
    owner_id = " ,".join(owners)
    tg_aud = convert_bytes(config.TG_AUDIO_FILESIZE_LIMIT)
    tg_vid = convert_bytes(config.TG_VIDEO_FILESIZE_LIMIT)
    text = f"""**Music Bot Config Variables:**

**<u>Basic Variables:</u>**
**Music_Bot_Name** : `{bot_name}`
**Duration_Limit** : `{play_duration} Minutes`
**Song_Download_Duration_Limit** :` {song} Minutes`
**Owner_ID** : `{owner_id}`
    
**<u>Repository Variables:</u>**
**Upstream_Repo** : `{up_r}`
**Upstream_Branch** : `{up_b}`
**GitHub_Repo** :` {git}`
**Git_Token**:` {token}`


**<u>Bot Variables:</u>**
**Auto_Leaving_Assistant** : `{ass}`
**Assistant_Leave_Time** : `{auto_leave} Seconds`
**Auto_Suggestion_Mode** :` {a_sug}`
**Auto_Suggestion_Time** : `{auto_sug} Seconds`
**Auto_Downloads_Clear** : `{down}`
**Private_Bot_Mode** : `{pvt}`
**YouTube_Edit_Sleep** : `{yt_sleep} Seconds`
**Telegram_Edit_Sleep** :` {tg_sleep} Seconds`
**CleanMode_Mins** : `{cm} Minutes`
**Video_Stream_Limit** : `{v_limit} Chats`
**Server_Playlist_Limit** :` {playlist_limit}`
**Playlist_Fetch_Limit** :` {fetch_playlist}`

**<u>Spotify Variables:</u>**
**Spotify_Client_ID** :` {sotify}`
**Spotify_Client_Secret** : `{sotify}`

**<u>Playsize Vars:</u>**
**Tg_Audio_Filesize_Limit** :` {tg_aud}`
**Tg_Video_Filesize_Limit** :` {tg_vid}`

**<u>Extra Variables:</u>**
**Support_Channel** : `{s_c}`
**Support_Group** : ` {s_g}`
**Start_Img_Url** : ` {start}`
    """
    await asyncio.sleep(1)
    await mystic.edit_text(text)
