# Copyright 2021 To 2024-present, Author: MrAKTech

import re
import time
import random
import datetime
import math
import logging
import mimetypes
import secrets
from aiohttp import web
from aiohttp.http_exceptions import BadStatusLine

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from MrAKTech import StreamBot, multi_clients, work_loads
from MrAKTech.server.exceptions import FIleNotFound, InvalidHash
from MrAKTech.tools.custom_dl import ByteStreamer, chunk_size, offset_fix
from MrAKTech.tools.render_template import render_page
from MrAKTech.tools.utils_bot import temp, readable_time
from MrAKTech.tools.file_properties import get_file_ids, get_namex
from MrAKTech.tools.human_readable import humanbytes
from MrAKTech.tools.txt import tamilxd
from MrAKTech.config import Telegram, Server, Domain

logger = logging.getLogger("routes")

routes = web.RouteTableDef()


@routes.get("/", allow_head=True)
async def root_route_handler(_):
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
	<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-GH31XK8QDT"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-GH31XK8QDT');
</script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MrAK BOTS Updates</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-blue-50 font-sans">
    <section class="text-center py-16 px-6 bg-blue-100">
        <div class="max-w-2xl mx-auto">
            <div class="mb-6">
                <div class="flex justify-center items-center w-12 h-12 bg-white rounded-full mx-auto">
                    <i class="fas fa-cloud text-blue-600 text-2xl"></i>
                </div>
            </div>
            <h1 class="text-3xl font-extrabold text-gray-900 mb-4">Welcome to 𝙼𝚁𝗔𝗞 𝐁𝐎𝐓𝐒</h1>
            <p class="text-lg text-gray-600 mb-2">➥ An organization making Telegram bots</p>
            <p class="text-lg text-gray-600 mb-2">➥ We are trying to provide the best 👍💯</p>
            <p class="text-lg text-gray-600 mb-2">Made in India</p>
            <p class="text-lg text-gray-600 mb-2">🧑‍💻 CEO: @MrAKTech</p>
            <p class="text-lg text-gray-600 mb-2">(c) @MrAK_BOTS & @MrAK Tech</p>
            <p class="text-lg text-gray-600 mb-4">💜 Thank you for supporting us</p>
            <a href="https://telegram.me/MrAK_BOTS"
                class="bg-blue-700 text-white py-3 px-8 rounded-full shadow-md hover:bg-blue-800 transition duration-300">Join
                MrAK BOTS Updates</a>
        </div>
    </section>
    <section class="max-w-6xl mx-auto py-12 px-4 grid gap-6 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">
        
        <div class="bg-white rounded-xl shadow-lg p-6 text-center hover:shadow-xl transition-shadow duration-300">
            <div class="flex justify-center mb-4">
                <i class="fas fa-globe text-blue-600 text-3xl"></i>
            </div>
            <h2 class="text-xl font-semibold text-gray-900 mb-2">TG Personal Bot</h2>
            <p class="text-gray-600 mb-6">Get a personal Telegram bot! I create and host on Heroku/VPS. Contact me to get
                started!</p>
            <a href="https://telegram.me/MrAK_BOTS" target="_blank"
                class="bg-blue-900 text-white py-2 px-6 rounded shadow-md hover:bg-gray-950 transition duration-300">Contact
                Us</a>
        </div>
        
    </section>
    <footer class="py-6 mt-12 bg-blue-100">
        <div class="max-w-6xl mx-auto text-center text-gray-600">
            <p class="text-sm">Designed by <a href="https://telegram.me/MrAK_BOTS" target="_blank"
                    class="text-blue-600 hover:underline">MrAK_BOTS</a></p>
        </div>
    </footer>
</body>
</html>
"""
    return web.Response(text=html_content, content_type="text/html")


# @routes.get(r"/{path:\S+}")
# async def undefined_url_handler(request):
#     return web.HTTPFound("/error")


@routes.get("/error")
async def error_handler(request):
    html_content = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Error Page</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  </head>
  <body>
    <div class="container">
      <h1>Error Page</h1>
      <p>Sorry, the requested page could not be found.</p>
      <p>Please check the URL or try again later.</p>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  </body>
</html>
    """
    return web.Response(text=html_content, content_type="text/html")


@routes.post("/api/report")
async def api_handler(request):
    try:
        data = await request.json()
        logging.info(f"Received report: {data}")
        india_time = datetime.datetime.now(
            datetime.timezone(datetime.timedelta(hours=5, minutes=30))
        )
        file_data = await get_file_ids(
            StreamBot, int(Telegram.FLOG_CHANNEL), int(data.get("file_id"))
        )
        await StreamBot.send_message(
            chat_id=Telegram.REPORT_GROUP,
            text=tamilxd.REPORT_TXT.format(
                date=india_time.strftime("%d-%B-%Y"),
                time=india_time.strftime("%I:%M:%S %p"),
                file_name=file_data.file_name,
                file_size=humanbytes(file_data.file_size),
                mime_type=file_data.mime_type,
                file_unique_id=file_data.unique_id,
                file_url=f"{Server.URL}watch/{data.get('file_id')}?hash={file_data.unique_id[:6]}",
                post_url=f"https://t.me/{str(Telegram.FLOG_CHANNEL).replace('-100','c/')}/{data.get('file_id')}",
                report=data.get("report"),
                report_msg=data.get("reportMsg"),
            ),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Delete 🤷‍♂️", callback_data=f"delete_{data.get("file_id")}"
                        ),
                        InlineKeyboardButton("verify ☑️", callback_data="verify"),
                    ],
                    [InlineKeyboardButton("Close", callback_data="close")],
                ]
            ),
            disable_web_page_preview=True,
        )
        return web.json_response(
            {"status": "success", "message": "Data received and processed successfully"}
        )
    except Exception as e:
        logging.error(f"Error processing API request: {str(e)}")
        return web.json_response(
            {"status": "error", "message": "Failed to process the request"}
        )


@routes.post("/api/file")
async def api_handlerx(request):
    try:
        id = await request.json()
        file_data = await get_file_ids(
            StreamBot, int(Telegram.FLOG_CHANNEL), int(id.get("id"))
        )
        return web.json_response(
            {
                "status": "success",
                "file_name": file_data.file_name,
                "file_size": humanbytes(file_data.file_size),
                "mime_type": file_data.mime_type,
                "file_unique_id": file_data.unique_id,
                "file_url": f"{random.choice(Domain.CLOUDFLARE_URLS)}v3/{id.get("id")}?hash={file_data.unique_id[:6]}",
                "store_link": f"https://telegram.me/{Telegram.FILE_STORE_BOT_USERNAME}?start=download_{id.get("id")}",
            },
        )
    except Exception as e:
        logging.error(f"Error processing API request: {str(e)}")
        return web.json_response(
            {"status": "error", "message": "Failed to process the request"}
        )


@routes.get("/status", allow_head=True)
async def status_route_handler(_):
    bot_workloads = sorted(work_loads.items(), key=lambda x: x[1], reverse=True)
    total_workload = sum(workload for _, workload in bot_workloads)
    bot_workload_dict = dict(
        ("bot" + str(c + 1), workload) for c, (_, workload) in enumerate(bot_workloads)
    )
    return web.json_response(
        {
            "server_status": "running",
            "uptime": readable_time((time.time() - temp.START_TIME)),
            "telegram_bot": "@" + temp.U_NAME,
            "connected_bots": len(multi_clients),
            "loads": bot_workload_dict,
            "TotalLoads": total_workload,
            "version": "V1.7.7",
        }
    )


@routes.get(r"/watch/{path:\S+}", allow_head=True)
async def stream_handler(request: web.Request):
    try:
        path = request.match_info["path"]
        match = re.search(r"^([a-zA-Z0-9_-]{6})(\d+)$", path)
        if match:
            secure_hash = match.group(1)
            message_id = int(match.group(2))
        else:
            message_id = int(re.search(r"(\d+)(?:\/\S+)?", path).group(1))
            secure_hash = request.rel_url.query.get("hash")
        return web.Response(
            text=await render_page(message_id, secure_hash), content_type="text/html"
        )
    except InvalidHash as e:
        raise web.HTTPForbidden(text=e.message)
    except FIleNotFound as e:
        raise web.HTTPNotFound(text=e.message)
    except (AttributeError, BadStatusLine, ConnectionResetError):
        pass
    except Exception as e:
        logger.critical(str(e), exc_info=True)
        raise web.HTTPInternalServerError(text=str(e))


@routes.get(r"/dl/{path:\S+}", allow_head=True)
async def dl_stream_handler(request: web.Request):
    try:
        path = request.match_info["path"]
        match = re.search(r"^([a-zA-Z0-9_-]{6})(\d+)$", path)
        if match:
            secure_hash = match.group(1)
            message_id = int(match.group(2))
        else:
            message_id = int(re.search(r"(\d+)(?:\/\S+)?", path).group(1))
            secure_hash = request.rel_url.query.get("hash")
        return await media_streamer(request, message_id, secure_hash)
    except InvalidHash as e:
        raise web.HTTPForbidden(text=e.message)
    except FIleNotFound as e:
        raise web.HTTPNotFound(text=e.message)
    except (AttributeError, BadStatusLine, ConnectionResetError):
        pass
    except Exception as e:
        logger.critical(str(e), exc_info=True)
        raise web.HTTPInternalServerError(text=str(e))


@routes.get(r"/v2/{path:\S+}", allow_head=True)
async def v2_stream_handler(request: web.Request):
    try:
        path = request.match_info["path"]
        return await media_streamer(request, message_id=int(path[6:]), secure_hash=str(path[:6]))
    except InvalidHash as e:
        raise web.HTTPForbidden(text=e.message)
    except FIleNotFound as e:
        raise web.HTTPNotFound(text=e.message)
    except (AttributeError, BadStatusLine, ConnectionResetError):
        pass
    except Exception as e:
        logger.critical(str(e), exc_info=True)
        raise web.HTTPInternalServerError(text=str(e))


@routes.get(r"/v3/{path:\S+}", allow_head=True)
async def v3_stream_handler(request: web.Request):
    try:
        path = request.match_info["path"]
        return await media_streamer(request, message_id=int(path[6:]), secure_hash=str(path[:6]))
    except InvalidHash as e:
        raise web.HTTPForbidden(text=e.message)
    except FIleNotFound as e:
        raise web.HTTPNotFound(text=e.message)
    except (AttributeError, BadStatusLine, ConnectionResetError):
        pass
    except Exception as e:
        logger.critical(str(e), exc_info=True)
        raise web.HTTPInternalServerError(text=str(e))


class_cache = {}


async def media_streamer(request: web.Request, message_id: int, secure_hash: str):
    range_header = request.headers.get("Range", 0)
    
    index = min(work_loads, key=work_loads.get)
    faster_client = multi_clients[index]

    # if Telegram.MULTI_CLIENT:
    # logging.info(f"Client {index} is now serving {request.remote}")

    if faster_client in class_cache:
        tg_connect = class_cache[faster_client]
        logger.debug(f"Using cached ByteStreamer object for client {index}")
    else:
        logger.debug(f"Creating new ByteStreamer object for client {index}")
        tg_connect = ByteStreamer(faster_client)
        class_cache[faster_client] = tg_connect
    logger.debug("before calling get_file_properties")
    file_id = await tg_connect.get_file_properties(message_id)
    logger.debug("after calling get_file_properties")
    
    
    if file_id.unique_id[:6] != secure_hash:
        logger.debug(f"Invalid hash for message with ID {message_id}")
        raise InvalidHash

    file_size = file_id.file_size

    if range_header:
        from_bytes, until_bytes = range_header.replace("bytes=", "").split("-")
        from_bytes = int(from_bytes)
        until_bytes = int(until_bytes) if until_bytes else file_size - 1
    else:
        from_bytes = request.http_range.start or 0
        until_bytes = request.http_range.stop or file_size - 1

    # logging.debug(f"from_bytes: {from_bytes} until_bytes: {until_bytes}")
    # if from_bytes <10 and until_bytes >200:
    #     await db.increment_dl_count(file_id.org_id)

    req_length = until_bytes - from_bytes
    new_chunk_size = await chunk_size(req_length)
    offset = await offset_fix(from_bytes, new_chunk_size)
    first_part_cut = from_bytes - offset
    last_part_cut = (until_bytes % new_chunk_size) + 1
    part_count = math.ceil(req_length / new_chunk_size)
    body = tg_connect.yield_file(
        file_id, index, offset, first_part_cut, last_part_cut, part_count, new_chunk_size
    )

    mime_type = file_id.mime_type
    file_name = file_id.file_name
    disposition = "attachment"
    if mime_type:
        if not file_name:
            try:
                file_name = f"{secrets.token_hex(2)}.{mime_type.split('/')[1]}"
            except (IndexError, AttributeError):
                file_name = f"{secrets.token_hex(2)}.unknown"
    else:
        if file_name:
            mime_type = mimetypes.guess_type(file_id.file_name)
        else:
            mime_type = "application/octet-stream"
            file_name = f"{secrets.token_hex(2)}.unknown"
    return_resp = web.Response(
        status=206 if range_header else 200,
        body=body,
        headers={
            "Content-Type": f"{mime_type}",
            "Range": f"bytes={from_bytes}-{until_bytes}",
            "Content-Range": f"bytes {from_bytes}-{until_bytes}/{file_size}",
            "Content-Disposition": f'{disposition}; filename="{file_name}"',
            "Accept-Ranges": "bytes",
        },
    )

    if return_resp.status == 200:
        return_resp.headers.add("Content-Length", str(file_size))

    return return_resp
