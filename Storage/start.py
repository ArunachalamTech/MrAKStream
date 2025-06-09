# Copyright 2021 To 2024-present, Author: MrAKTech

import asyncio

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums.parse_mode import ParseMode
from pyrogram.errors import ChatAdminRequired

from MrAKTech.config import Telegram, Domain
from MrAKTech.database.u_db import u_db
from MrAKTech.tools.utils_bot import is_subscribed, is_user_joined
from MrAKTech.tools.txt import tamilxd, BUTTON


def get_all_media_file_data(m):
    media = m.video or m.document or m.audio
    if media:
        return media.file_id, media.file_unique_id[:6], media.file_name, media.file_size
    else:
        return None, None, None, None


@Client.on_message(filters.command("start"))
async def start(client, message):
    if not await u_db.sis_user_exist(message.from_user.id):
        await u_db.sadd_user(message.from_user.id)
        await client.send_message(
            Telegram.SULOG_CHANNEL,
            f"#NewUser \nID - `{message.from_user.id}` \nNᴀᴍᴇ - {message.from_user.mention}",
        )
    usr_cmd = message.text.split("_")[-1]
    if usr_cmd == "/start":
        if not await is_user_joined(client, message, Telegram.AUTH_CHANNEL2):
            return
        await message.reply_text(
            text=f" <b> Hᴇʟʟᴏ {message.from_user.first_name} \n\nɪ ᴀᴍ ᴀ ʙᴏᴛ ᴛʜᴀᴛ ᴘʀᴏᴠɪᴅᴇs ғɪʟᴇ ᴀᴄᴄᴇss ғᴏʀ @MrAKStreamBot ʙᴏᴛ. </b>\n\n/donation",
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("📢 Updates", url="https://t.me/+YVKEuuuH6l9mNDc1"),
                        InlineKeyboardButton("⚡ Support", url="https://t.me/MrAK_BOTS"),
                    ],
                    [
                        InlineKeyboardButton("❤️ Create Like This Link ❤️", url="https://t.me/MrAKStreamBot"),
                    ],
                    [
                        InlineKeyboardButton("🔰 Join Now 🔰", url="https://t.me/+1EgUhBbcIHQzMDU1"),
                    ]
                ]
            ),
        )
    else:
        if Telegram.AUTH_CHANNEL2 and not await is_subscribed(client, message, Telegram.AUTH_CHANNEL2):
            try:
                invite_link = await client.create_chat_invite_link(
                    int(Telegram.AUTH_CHANNEL2), creates_join_request=True
                )
            except ChatAdminRequired:
                await message.reply_text("MAKE SURE BOT IS ADMIN IN FORCESUB CHANNEL")
                return
            btn = [
                [InlineKeyboardButton("🔰 Join Now 🔰", url=invite_link.invite_link)],
                [
                    InlineKeyboardButton(
                        "🔄 Refresh / Try Again",
                        url=f"https://t.me/{(await client.get_me()).username}?start=KRBOTS_{usr_cmd}",
                    )
                ],
            ]
            try:
                return await client.send_message(
                    chat_id=message.from_user.id,
                    text=tamilxd.FORCE_SUB_TEXT.format(message.from_user.mention),
                    reply_markup=InlineKeyboardMarkup(btn),
                )
            except Exception as e:
                print(f"Force Sub Text Error\n{e}")
                return await client.send_message(
                    chat_id=message.from_user.id,
                    text=tamilxd.FORCE_SUB_TEXT.format(message.from_user.mention),
                    reply_markup=InlineKeyboardMarkup(btn),
                )
            #
        get_msg = await client.get_messages(
            chat_id=Telegram.FLOG_CHANNEL, message_ids=int(usr_cmd)
        )
        data = get_all_media_file_data(get_msg)
        stream_link = f"{Domain.TEMP_URL}watch/{get_msg.id}?hash={data[1]}"
        #

        tamil1 = await message.reply_text(
            "<b>Your 📁 File will be automatically deleted in ⏰ 10 minutes.↗ Forward it anywhere or save it privately before downloading</b>\n",
            disable_web_page_preview=True,
            quote=True,
        )

        tamil2 = await client.send_cached_media(
            chat_id=message.from_user.id,
            file_id=data[0],
            caption=tamilxd.STREAM_TXT.format(caption=data[2].replace("_", " "), stream_link=stream_link),
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("📽 Sᴛʀᴇᴀᴍ & Dᴏᴡɴʟᴏᴀᴅ 💾", url=stream_link)]]
            ),
        )
        await asyncio.sleep(1800)
        await tamil1.delete()
        await tamil2.delete()
        await message.delete()


@Client.on_message(filters.command(["donate", "donation"]))
async def donate(app, message):
    await message.reply_text(
        text=tamilxd.DONATE_TXT,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
        reply_markup=BUTTON.DONATE_BUTTONS,
        quote=True,
    )

@Client.on_callback_query(filters.regex(pattern=r"donate"))
async def donate_cb(_, query):
    await query.message.edit(
        text=tamilxd.DONATE_TXT,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
        reply_markup=BUTTON.DONATE_BUTTONS,
    )
    await query.answer()

@Client.on_callback_query(filters.regex(pattern=r"close"))
async def close_cb(_, query):
    await query.message.delete()
    await query.answer()
