# (c) @MrAKTech

import asyncio
import random

from pyrogram import filters, Client
from pyrogram.errors import FloodWait
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from MrAKTech import StreamBot
from config import Telegram, Domain
from database.u_db import u_db
from tools.utils_bot import short_link, verify_user
from tools.human_readable import humanbytes
from tools.file_properties import get_name, get_hash, get_media_file_size


@StreamBot.on_message(
    (filters.private) & (filters.document | filters.video | filters.audio), group=4
)
async def private_receive_handler(c: Client, m: Message):
    if not await verify_user(c, m):
        return
    #
    mediax = m.document or m.video or m.audio
    if m.document or m.video or m.audio:
        if m.caption:
            file_caption = f"{m.caption}"
        else:
            file_caption = ""
    file_captionx = file_caption.replace(".mkv", "")
    log_msg = await m.forward(chat_id=Telegram.FLOG_CHANNEL)
    user = await u_db.get_user(m.from_user.id)
    caption_position = user["method"]
    c_caption = user["caption"]
    storage = f"https://telegram.me/{Telegram.FILE_STORE_BOT_USERNAME}?start=download_{log_msg.id}"
    storagex = await short_link(storage, user)
    stream_linkx = f"{random.choice(Domain.CLOUDFLARE_URLS)}watch/{str(log_msg.id)}?hash={get_hash(log_msg)}"
    stream_link = await short_link(stream_linkx, user)
    online_link = await short_link(
        f"{random.choice(Domain.CLOUDFLARE_URLS)}dl/{str(log_msg.id)}?hash={get_hash(log_msg)}",
        user,
    )
    try:
        if caption_position == "links":
            await m.reply_text(
                text=c_caption.format(
                    file_name="" if get_name(log_msg) is None else get_name(log_msg),
                    caption="" if file_captionx is None else file_captionx,
                    file_size=(
                        ""
                        if humanbytes(get_media_file_size(m)) is None
                        else humanbytes(get_media_file_size(m))
                    ),
                    download_link="" if online_link is None else online_link,
                    stream_link="" if stream_link is None else stream_link,
                    storage_link="" if storagex is None else storagex,
                ),
                quote=True,
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("Dᴏᴡɴʟᴏᴀᴅ ɴᴏᴡ 📥", url=stream_link)]]
                ),
            )
        elif caption_position == "files":
            await c.send_cached_media(
                chat_id=m.from_user.id,
                file_id=mediax.file_id,
                caption=c_caption.format(
                    file_name="" if get_name(log_msg) is None else get_name(log_msg),
                    caption="" if file_captionx is None else file_captionx,
                    file_size=(
                        ""
                        if humanbytes(get_media_file_size(m)) is None
                        else humanbytes(get_media_file_size(m))
                    ),
                    download_link="" if online_link is None else online_link,
                    stream_link="" if stream_link is None else stream_link,
                    storage_link="" if storagex is None else storagex,
                ),
            )
        await log_msg.reply_text(
            text=f"**RᴇQᴜᴇꜱᴛᴇᴅ ʙʏ :** [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n**Uꜱᴇʀ ɪᴅ :** `{m.from_user.id}`\n **Fɪʟᴇ Uɴɪǫᴜᴇ ID:** {mediax.file_unique_id}\n**Stream ʟɪɴᴋ :** {stream_linkx}\n**Storage ʟɪɴᴋ :** {storage}",
            disable_web_page_preview=True,
            quote=True,
        )

    except FloodWait as e:
        print(f"Sleeping for {str(e.x)}s")
        await asyncio.sleep(e.x)
        await c.send_message(
            chat_id=Telegram.ELOG_CHANNEL,
            text=f"Gᴏᴛ FʟᴏᴏᴅWᴀɪᴛ ᴏғ {str(e.x)}s from [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n\n**𝚄𝚜𝚎𝚛 𝙸𝙳 :** `{str(m.from_user.id)}`",
            disable_web_page_preview=True,
        )
