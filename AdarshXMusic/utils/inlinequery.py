from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="Pause",
            description=f"Pause Current Playing Stream On Video Chat.",
            thumb_url="https://telegra.ph/file/95f3f7557f5dfc919dda6.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="Resume",
            description=f"Resume The Paused Stream On Video Chat.",
            thumb_url="https://telegra.ph/file/865fee9a12949e6f2f4cc.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="Skip",
            description=f"Skip The Current Playing Stream On Video Chat And Moves To The Next Stream.",
            thumb_url="https://telegra.ph/file/a840a21b0640e375683a8.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="End",
            description="End The Current Playing Stream On Video Chat.",
            thumb_url="https://telegra.ph/file/4f6e989616c1fa5d3589f.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="Shuffle",
            description="Shuffle The Queued Songs IN Playlist.",
            thumb_url="https://telegra.ph/file/cb0ab21555f9fb12c49e7.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="Loop",
            description="Loop The Current Playing Track On Video Chat.",
            thumb_url="https://telegra.ph/file/af5e903bb23e0b77540c0.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
