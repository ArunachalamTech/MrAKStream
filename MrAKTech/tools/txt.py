#Copyright 2021 To 2024-present, Author: MrAKTech

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class tamilxd(object):

    CUSTOM_SHORTNER_TXT = """<b><u>📝 CUSTOM SHORTNER</u>

To shorten your links using your preferred provider, make sure to connect it with me first.

➢ /api - To Add Your Shortener API
➢ /site - To Add Your Shortener URL </b>
    """

    SETTINGS_TXT = '''<b><U>㊂ User Settings</u>

┏📂 Daily Upload  : <code>∞ / ️∞</code> per day
┠♈ Site : <spoiler><code>{URLX}</code></spoiler>
┠♐ API : <spoiler><code>{APIX}</code></spoiler>
┗📄 Caption : <code>{CAPTION}</code>

🦊 Mᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ ›› <a href=https://t.me/MrAK_BOTS>𝙼𝚁𝗔𝗞 𝐁𝐎𝐓𝐒</a></b>'''

    RESET_SETTINGS = 'Do you want to Reset Settings ?'
    
    #"<b><u>⚙️ SETTINGS</u>\n♻️ ʜᴇʀᴇ ɪs ᴍʏ ᴀʟʟ sᴇᴛᴛɪɴɢs ᴍᴇɴᴜ ♻️</b>"
    
    USER_ABOUT_MESSAGE = """
**❤️ ʜᴇʀᴇ ᴀʀᴇ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ sᴇᴛᴛɪɴɢs ғᴏʀ ᴛʜɪs ʙᴏᴛ : !!

🌐 ᴡᴇʙsɪᴛᴇ ➙ {shortener_url}

🔌 ᴀᴘɪ ➙ {shortener_api}

🕹 ᴍᴇᴛʜᴏᴅ ➙ {method}

🗃 sᴛᴏʀᴀɢᴇ ➙ {storage}
**"""
    
    CUSTOM_CAPTION_TXT = """<b><u>📝 CUSTOM CAPTION</u>

➢ /addcaption  - ᴛᴏ ᴀᴅᴅ ʏᴏᴜʀ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ 
➢ Sʜᴏᴡ ᴄᴀᴘᴛɪᴏɴ ɴᴏᴛ ᴡᴏʀᴋɪɴɢ ᴜsᴇ /showcaption

[HTML Style](https://docs.pyrogram.org/topics/text-formatting#html-style) &&  [Markdown Style](https://docs.pyrogram.org/topics/text-formatting#markdown-style) 

<u>AVAILABLE FILLINGS:</u>
<code>{file_name}</code> : ғɪʟᴇ ɴᴀᴍᴇ
<code>{file_size}</code> : ғɪʟᴇ sɪᴢᴇ
<code>{caption}</code> : ᴅᴇғᴀᴜʟᴛ ᴄᴀᴘᴛɪᴏɴ ᴏғ ᴍᴇssᴀɢᴇs
<code>{download_link}</code> : ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ
<code>{stream_link}</code> : sᴛᴇᴀᴍɪɴɢ ʟɪɴᴋ
"""
    CHL_CUSTOM_CAPTION_TXT = '''<b><u>㊂ Caption Settings :</u>

➲ Custom Caption : <code>{CAPTIONX}</code>

➲ Description : <code>Bot Automatically edit your files Name</code></b>'''

    CHL_CHANNEL_DETAILS_TXT = '''<b><u>📄 Channel Details</u>
    
┏🏷️ TITLE: <code>{TITLEX}</code>
┠📋 CHANNEL ID: <code>{CHANNEL_DIX}</code>
┗👤 USERNAME: {USERNAMEX}

┏📂 Daily Upload  : <code>∞ / ️∞</code> Per Day
┠♈ Site : <spoiler>{URLX}</spoiler>
┠♐ API : <spoiler>{APIX}</spoiler>
┗📄 Caption : <code>{CAPTION}</code>

🦊 Mᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ ›› <a href=https://t.me/MrAK_BOTS>𝙼𝚁𝗔𝗞 𝐁𝐎𝐓𝐒</a></b>'''

    CHL_SHORTNER_TXT = '''<b><u>㊂ Shortner Settings :</u>

➲ Custom URL : {URLX}
➲ Custom API : {APIX}

➲ Description : None'''

    CHL_CHANNEL_ADD_TXT = '''<b>Please add me as admin with atleast 'Post Messages' and 'Edit message of others' rights to the desired channel

After that, forward a message from the channel.

Cancel this process using /cancel. 

Timeout: 60 sec (If their is no reply in 60 sec, action will be auto cancelled.)</b>'''
    
    START_TXT = """<b>Hello {}

I am Powerfull files to link and shortner link in 4GB.
<u>Working on channels and private chasts.</u>

<i>Send me any media to Generate Permanent Download and Stream Link. (for forward restricted media send message link)</i>

<u>⚠️ Warnig.</u>
<i>Sending P*rn Content lead to permanent ban</i>

🦊 Maintained By ›› <a href=https://t.me/MrAK_BOTS>𝙼𝚁𝗔𝗞 𝐁𝐎𝐓𝐒</a></b>"""

    ABOUT_TXT = """<b>╭──────❰ <U>🤖 Bot Details</U> ❱──────〄
│ 
│ 🤖 Mʏ Nᴀᴍᴇ : <a href=https://t.me/MrAKStreamBot>𝙼𝚁𝗔𝗞 𝐅𝚒𝚕𝚎𝐓𝚘𝐋𝚒𝚗𝚔𝐁𝚘𝚝</a>
│ 👨‍💻 Dev : <a href=https://t.me/MrAK_BOTS>𝙼𝚁𝗔𝗞 𝐁𝐎𝐓𝐒</a>
│ 📢 Uᴘᴅᴀᴛᴇꜱ : <a href=https://t.me/MrAK_BOTS>𝙼𝚁𝗔𝗞 𝐁𝐎𝐓𝐒</a>
│ 📡 Server : <a href=https://www.heroku.com/>Heroku Eco</a>
│ 🗣️ Language : <a href=https://www.python.org>Python 3.12.4</a>
│ 📚 Library : <a href=https://github.com/Mayuri-Chan/pyrofork>PyroFork 2.3.37</a> 
│ 🛢️ Database : <a href=https://www.mongodb.com/>MongoDB 7.0.12</a>
│ 🗒️ Build Version : V1.8.2 [ Bᴇᴛᴀ ]
│ 
╰────────────────────⍟</b>"""

    FORCE_SUB_TEXT = "👋 Hii {},\n\n <b>ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ!</b> \n\nDᴜᴇ ᴛᴏ ᴏᴠᴇʀʟᴏᴀᴅ, ᴏɴʟʏ ᴄʜᴀɴɴᴇʟ sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜᴇ ʙᴏᴛ!"
    
    HELP_TXT = """<b>⊹ ʜᴏᴡ ᴛᴏ ᴜsᴇ ғɪʟᴇs ᴛᴏ ʟɪɴᴋ ʙᴏᴛ ⊹</b>

⇒ <code>sᴇɴᴅ ᴍᴇ ᴀɴʏ ғɪʟᴇ (ᴏʀ) ᴍᴇᴅɪᴀ ғʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ..</code>
⇒ <code>ᴛʜɪs ʙᴏᴛ ᴡɪʟʟ sᴇɴᴅ ʏᴏᴜ ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ</code>
⇒ <code>ᴛʜɪs ʟɪɴᴋ ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴏʀ sᴛʀᴇᴀᴍ ғɪʟᴇs[ᴜsɪɴɢ ᴇxᴛᴇʀɴᴀʟ ᴠɪᴅᴇᴏ ᴘʟᴀʏᴇʀ] ᴛʜʀᴏᴜɢʜ ᴍʏ sᴇʀᴠᴇʀ</code>
⇒ <code>ғᴏʀ sᴛʀᴇᴀᴍɪɴɢ ᴊᴜsᴛ ᴄᴏᴘʏ ᴛʜᴇ ᴍᴏɴᴏ ʟɪɴᴋ ᴀɴᴅ ᴘᴀsᴛᴇ ɪᴛ ɪɴ ʏᴏᴜʀ ᴠɪᴅᴇᴏ ᴘʟᴀʏᴇʀ ᴛᴏ sᴛᴀʀᴛ sᴛʀᴇᴀᴍɪɴɢ</code>
⇒ <code>ᴛʜɪs ʙᴏᴛ sʜᴀʀᴇs ᴛʜᴇ ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ ᴛᴏ ʏᴏᴜ.</code>
⇒ <code>ᴛʜɪs ʙᴏᴛ ɪs ᴀʟsᴏ sᴜᴘᴘᴏʀᴛᴇᴅ ɪɴ ᴄʜᴀɴɴᴇʟs. ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴄʜᴀɴɴᴇʟ ᴀs ᴀᴅᴍɪɴ ᴛᴏ ᴍᴀᴋᴇ ᴍᴇ ᴡᴏʀᴋᴀʙʟᴇ...!</code>
⇒ <code>ʜᴏᴡ ᴛᴏ ᴀᴅᴅ sʜᴏʀᴛɴᴇʀ-ʟɪɴᴋ</code> -<b>/features</b>
⇒ <code>ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</code> :<b> <a href=https://t.me/MrAK_BOTS>𝙼𝚁𝗔𝗞 𝐁𝐎𝐓𝐒</a></b>

<b><u>⚠️ Warnig ⚠</u>
<i>Sending P*rn Content lead to permanent ban</i></b>

<i>if you bot is not working properly and you are experiencing issues, please do not hesitate to contact me.</i>

<b>👨‍💻 Admin : @IamMrAK_bot
📢 Updates : @MrAK_BOTS
❣️ Supports : @MrAK_BOTS</b>"""
    
    OWNER_INFO = """<b><u>🤖 Owner Details 🌿</u>

‣ Full Name : 𝙼𝚁𝗔𝗞
‣ Username : @IamMrAK_bot 
‣ Permanent DM link :<a href=https://t.me/IamMrAK_bot>Click Here</a></b>"""
    
    SOURCE_TXT = """<b><u>Notes</u>:

<code>⚠️ This bot is an private source project.

⇒ I will create a bot for you
⇒ Contact me</code> - <a href=https://t.me/IamMrAK_bot>♚ ᴀᴅᴍɪɴ ♚</a></b>"""


    DEV_TXT = """**__Special Thanks & Developers__

» 𝗦𝗢𝗨𝗥𝗖𝗘 𝗖𝗢𝗗𝗘 : [Click Here](https://github.com/MrAKTech) 

• @IamMrAK_bot
• @MrAK_BOTS

📢 Updates : @MrAK_BOTS
❣️ Supports : @MrAK_BOTS**"""
    
    COMMENTS_TXT = """<b><u> ⊹ ʜᴏᴡ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ᴏᴡɴ sʜᴏʀᴛɴᴇʀ ⊹</u>

<u>MAIN CMD</u>
1. /site or /shortner_url
2. /api or /shortner_api
3. /addcaption 
4. /showcaption
5. /settings
6. /stats
7. /status

<u>SUB CMD</u>
1. /about
2. /help
3. /dc
4. /ping
5. /users

➾ <u>ᴇxᴀᴍᴘʟᴇ ↓↓↓</u></b>
<code>/site example.com</code>
<code>/api ec8ba7deff6128848def53bf2d4e69608443cf27</code>

<i>if you bot is not working properly and you are experiencing issues, please do not hesitate to contact me.</i>

<b>👨‍💻 Admin : @IamMrAK_bot
📢 Updates : @MrAK_BOTS
❣️ Supports : @MrAK_BOTS</b>"""



    DONATE_TXT = """<b><u>💗 Thank you showing internet in donation</u></b>

<i>Donate us to keep our services continously alive, You can send any amount 😢.</i>

<b><u>How You Can Donate:</u>
You can support us with any amount that suits you, such as ₹20, ₹50, ₹100, or ₹200. Every contribution makes a difference!

<u>📨 Payment Methods:</u>

• UPI ID: <code>mraklinkzz@axl</code></b>

For more information and further queries, please message @TamilXD.

Thank you for your support! 🙏</b>"""    
    ADN_COMS = """
<b> Aᴅᴍɪɴ Cᴏᴍᴍᴀɴᴅs

/ban

/unban

/status 

/broadcast or pin_broadcast

/logs

/invite_link 

/leave

/warnz
</b>
"""

    STREAM_MSG_TXT = """<b><u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u>

📂 File name : {file_name} 

📦 File size : {file_size}

📥 Download : {download_link}

🖥 Watch : {stream_link}

🚸 Note : this permanent link, Not expired

© ♻️@MrAK_BOTS </b> """

    STREAM_TXT = """<b>{caption}

💻 𝐖ᴀᴛᴄʜ & 𝐃𝚒𝚛𝚎𝚌𝚝 𝐅ᴀꜱᴛ 𝐃𝚘𝚠𝚗𝚕𝚘𝚊𝚍 𝐋𝚒𝚗𝚔 : {stream_link}

❤️ 𝐒𝐡𝐚𝐫𝐞 & 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐔𝐬 💗
♻️@MrAK_BOTS</b>"""

    BAN_TXT = """<b>🚫 Sorry, You are banned to use me !</b>
    
<b>📢 Contact : <a href=https://telegram.me/MrAK_BOTS_Support_Group>Support Group</a> They will help you.</b>"""

    SWCMD_TXT = """<b><u>Something wrong contact my developer.</u> 
    
<b>📢 Contact : <a href=https://telegram.me/MrAK_BOTS_Support_Group>Support Group</a> They will help you.</b>"""

    STATUS_TXT = '''╭──────[ <b><u>🤖 Bot Stats</u></b> ]──────〄
│
│ <b>⏰ Date:</b> {date}
│ <b>⌚ Time:</b> {time}
│ <b>📅 Day:</b> {day}
│ <b>🧭 UTC:</b> {utc_offset}
│
├─────[ 🧰 Bot Statistics ]─────⍟
│
│ <b>⚡ Uptime:</b> {currentTime}
│ <b>🎛️ CPU:</b> {cpuUsage} % | 💽 RAM: {memory} %
│ <b>🗄 Disk Size:</b> {total}
│ <b>🗂 Disk Used:</b> {used}
│ <b>📂 Free Disk:</b> {free}
│ <b>💾 Disk:</b> {disk} %
│
├─────[ 📑 Data Usage ]─────⍟
│
│ <b>⬇️ DL:</b> {sent} | <b>⬆️ UP:</b> {recv}
│ <b>⏩ Multi Clients:</b> {multi_clients}
│ <b>🚦DL1 Traffic: Total:</b> {v1_traffic_total} | Me: {v1_traffic_me}
│ <b>🚦DL2 Traffic: Total:</b> {v2_traffic_total} | Me: {v2_traffic_me}
│
╰────────────────────⍟'''

    REPORT_TXT = '''<b><u>📢 New Report Received</u></b>

<b>📅 Date:</b> <code>{date}</code>
<b>🕰 Time:</b> <code>{time}</code>

<b>📂 File Name:</b> <code>{file_name}</code>
<b>💾 File Size:</b> <code>{file_size}</code>
<b>📂 File Type:</b> <code>{mime_type}</code>
<b>📥 File URL: {file_url}</b>
<b>📧 Post URL: {post_url}</b>

<b>🕵 Report :</b> <code>{report}</code>
<b>🪪 Report ID:</b> <code>{file_unique_id}</code>
<b>📝 Report Msg:</b> <i>{report_msg}</i>'''

# ------------------------------------------------------------------------------

class BUTTON(object):
    
    OWNER_BUTTONS =  InlineKeyboardMarkup([
        InlineKeyboardButton('𝙼𝚁𝗔𝗞 𝐁𝐎𝐓𝐒', url='https://t.me/MrAK_BOTS')
    ])

    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('♡︎ Cᴏɴᴛᴀᴄᴛ 🧛‍♂️ Aᴅᴍɪɴ ♡︎', url=f'http://t.me/MrAK_BOTS')
        ],[
        InlineKeyboardButton('📢 Uᴘᴅᴀᴛᴇ', url='https://t.me/+YVKEuuuH6l9mNDc1'),
        InlineKeyboardButton('⚡ Sᴜᴘᴘᴏʀᴛ', url='https://t.me/MrAK_BOTS_Support_Group')
        ],[
        InlineKeyboardButton('⚙️ Hᴇʟᴘ', callback_data='help'),
        InlineKeyboardButton('📚 Aʙᴏᴜᴛ', callback_data='about')
        ],[
        InlineKeyboardButton('⚙️ Sᴇᴛᴛɪɴɢs ', callback_data='settings')
        ]]
    )

    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("📊 Status", callback_data="stats")
        ],[
        InlineKeyboardButton("⛺ Home", callback_data="start"),
        InlineKeyboardButton("🗑 Close", callback_data="close")
        ]]
    )

    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢 Uᴘᴅᴀᴛᴇ', url='https://t.me/+YVKEuuuH6l9mNDc1'),
        ],[
        InlineKeyboardButton("🌿 sᴏᴜʀᴄᴇ", callback_data = "source"),
        InlineKeyboardButton("👨‍💻 Dᴇᴠs 🥷", callback_data = "dev")
        ],[
        InlineKeyboardButton("⛺ Hᴏᴍᴇ", callback_data = "start"),
        InlineKeyboardButton("🗑 Cʟᴏsᴇ", callback_data = "close")
        ]]
    )
    
    DONATE_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("Pᴀʏ 💰 Aᴍᴏᴜɴᴛ",
                                             url="https://t.me/MrAK_BOTS")
        ],[
        InlineKeyboardButton("⛺ Hᴏᴍᴇ", callback_data="start"),
        InlineKeyboardButton("🗑 Cʟᴏsᴇ", callback_data="close")
        ]]
    ) 

    DEV_BUTTONS = InlineKeyboardMarkup( 
        [[
        InlineKeyboardButton('𝙼𝚁𝗔𝗞 𝐁𝐎𝐓𝐒', url='https://t.me/MrAK_BOTS'),
        ],[
        InlineKeyboardButton("≺≺ Back", callback_data = "about"),
        InlineKeyboardButton("🗑 Close", callback_data = "close")
        ]]
    ) 

    ADN_BUTTONS = InlineKeyboardMarkup( 
        [[
        InlineKeyboardButton("🗑 Close", callback_data = "close")
        ]]
    ) 

    SOURCE_BUTTONS = InlineKeyboardMarkup( 
        [[
        InlineKeyboardButton("♙ ʜᴏᴍᴇ", callback_data = "start"),
        InlineKeyboardButton("🗑 Close", callback_data = "close")
        ]]
    )
