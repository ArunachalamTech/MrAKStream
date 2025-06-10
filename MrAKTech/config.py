#Copyright 2021 To 2024-present, Author: MrTamilKiD
 
import os
from os import environ as env
from dotenv import load_dotenv

load_dotenv()

class Telegram:
    MULTI_CLIENT = True
    API_ID = int(env.get("API_ID", "22225617"))
    API_HASH = str(env.get("API_HASH", "ef16f7597376f1689663304c954e4493"))
    BOT_TOKEN = str(env.get("BOT_TOKEN", "7972636771:AAECNBf-NIoKAYWDBvfBx7mm0I8Zv9z_o0I"))
    OWNER_ID = {int(x) for x in os.environ.get("OWNER_ID", "6072149828").split()}
    WORKERS = int(env.get("WORKERS", "999"))  # 6 workers = 6 commands at once
    DATABASE_URL = str(env.get('DATABASE_URL','mongodb+srv://arunachalamtech:S.Aruna1155@stream.1oiti.mongodb.net/?retryWrites=true&w=majority&appName=stream'))
    DATABASE_NAME = str(env.get('DATABASE_NAME','stream'))
    SLEEP_THRESHOLD = int(env.get("SLEEP_THRESHOLD", "60"))
    FILE_PIC = env.get('FILE_PIC', "https://graph.org/file/8cd764fbdf3ccd34abe22.jpg")
    START_PIC = env.get('START_PIC', "https://graph.org/file/290af25276fa34fa8f0aa.jpg")
    VERIFY_PIC = env.get('VERIFY_PIC', "https://graph.org/file/736e21cc0efa4d8c2a0e4.jpg")
    # Optional command
    FILE_STORE_BOT_TOKEN = str(env.get("FILE_STORE_BOT_TOKEN", "7839112623:AAG3AMqMMwQuAPLL2ZFX7zAYT5yReoZQhMc"))
    FILE_STORE_BOT_USERNAME = str(env.get("FILE_STORE_BOT_USERNAME", "MrAKStreamFileBot"))
    # Channel list
    AUTH_CHANNEL = int(env.get("AUTH_CHANNEL", "-1002467628368"))   # Logs channel for auth channel main
    AUTH_CHANNEL2 = int(env.get("AUTH_CHANNEL2", "-1002280665579")) # Logs channel for auth channel sub
    FLOG_CHANNEL = int(env.get("FLOG_CHANNEL", "-1001912497698"))   # Logs channel for file logs
    ULOG_CHANNEL = int(env.get("ULOG_CHANNEL", "-1002574716230"))   # Logs channel for user logs
    ELOG_CHANNEL = int(env.get("ELOG_CHANNEL", "-1002657841408"))   # Logs channel for error logs
    SULOG_CHANNEL = int(env.get("SULOG_CHANNEL", "-1002686790297")) # Logs channel for storage user logs

    # GroupS List
    SUPPORT_GROUP = int(env.get("SUPPORT_GROUP", "-1002189074737")) # Group for support
    REPORT_GROUP = int(env.get("REPORT_GROUP", "-1002189074737"))   # Group for report
    SPAMWATCH_GROUP = int(env.get("SPAMWATCH_GROUP", "-1002189074737")) # Group for spamwatch

class Domain:
    TEMP_URL = str(env.get("FQDN", "https://mrak.mraklinkzz.com/"))
    CHANNEL_URL = str(env.get("CHANNEL_URL", "https://mrak.mraklinkzz.com/")) 
    CLOUDFLARE_URLS = [
        "https://mrak.mraklinkzz.com/"
    ]  
    
class Server:
    PORT = int(env.get("PORT", 9003))
    BIND_ADDRESS = str(env.get("BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(env.get("PING_INTERVAL", "1200"))
    HAS_SSL = str(env.get("HAS_SSL", "0").lower()) in ("1", "true", "t", "yes", "y")
    NO_PORT = str(env.get("NO_PORT", "0").lower()) in ("1", "true", "t", "yes", "y")
    FQDN = str(env.get("FQDN", BIND_ADDRESS))
    URL = FQDN

