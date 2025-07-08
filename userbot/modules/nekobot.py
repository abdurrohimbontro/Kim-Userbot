import os
import re

import requests
from PIL import Image
from validators.url import url

from userbot import CMD_HELP
from userbot.events import register

EMOJI_PATTERN = re.compile(
    "["
    "\U0001f1e0-\U0001f1ff"  # flags (iOS)
    "\U0001f300-\U0001f5ff"  # symbols & pictographs
    "\U0001f600-\U0001f64f"  # emoticons
    "\U0001f680-\U0001f6ff"  # transport & map symbols
    "\U0001f700-\U0001f77f"  # alchemical symbols
    "\U0001f780-\U0001f7ff"  # Geometric Shapes Extended
    "\U0001f800-\U0001f8ff"  # Supplemental Arrows-C
    "\U0001f900-\U0001f9ff"  # Supplemental Symbols and Pictographs
    "\U0001fa00-\U0001fa6f"  # Chess Symbols
    "\U0001fa70-\U0001faff"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027b0"  # Dingbats
    "]+"
)


def deEmojify(inputString: str) -> str:
    return re.sub(EMOJI_PATTERN, "", inputString)


# for nekobot
async def trumptweet(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={text}"
    ).json()
    geng = r.get("message")
    kapak = url(geng)
    if not kapak:
        return "check syntax once more"
    with open("gpx.png", "wb") as f:
        f.write(requests.get(geng).content)
    img = Image.open("gpx.png").convert("RGB")
    img.save("gpx.webp", "webp")
    return "gpx.webp"


async def changemymind(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=changemymind&text={text}"
    ).json()
    geng = r.get("message")
    kapak = url(geng)
    if not kapak:
        return "check syntax once more"
    with open("gpx.png", "wb") as f:
        f.write(requests.get(geng).content)
    img = Image.open("gpx.png").convert("RGB")
    img.save("gpx.webp", "webp")
    return "gpx.webp"


async def kannagen(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=kannagen&text={text}"
    ).json()
    geng = r.get("message")
    kapak = url(geng)
    if not kapak:
        return "check syntax once more"
    with open("gpx.png", "wb") as f:
        f.write(requests.get(geng).content)
    img = Image.open("gpx.png").convert("RGB")
    img.save("gpx.webp", "webp")
    return "gpx.webp"


async def qorygore(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=tweet&text={text}&username=QoryGore"
    ).json()
    geng = r.get("message")
    kapak = url(geng)
    if not kapak:
        return "check syntax once more"
    with open("gpx.png", "wb") as f:
        f.write(requests.get(geng).content)
    img = Image.open("gpx.png").convert("RGB")
    img.save("gpx.webp", "webp")
    return "gpx.webp"


async def tweets(text1, text2):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=tweet&text={text1}&username={text2}"
    ).json()
    geng = r.get("message")
    kapak = url(geng)
    if not kapak:
        return "check syntax once more"
    with open("gpx.png", "wb") as f:
        f.write(requests.get(geng).content)
    img = Image.open("gpx.png").convert("RGB")
    img.save("gpx.webp", "webp")
    return "gpx.webp"


async def purge():
    try:
        os.remove("gpx.png")
        os.remove("gpx.webp")
    except OSError:
        pass


@register(outgoing=True, pattern=r"^\.trump(?: |$)(.*)")
async def trump(event):
    text = event.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    if not text:
        if event.is_reply and not reply_to_id.media:
            text = reply_to_id.message
        else:
            await event.edit("`Send you text to trump so he can tweet.`")
            return
    await event.edit("`Requesting trump to tweet...`")
    text = deEmojify(text)
    img = await trumptweet(text)
    await event.client.send_file(event.chat_id, img, reply_to=reply_to_id)
    await event.delete()
    await purge()


@register(outgoing=True, pattern=r"^\.qg(?: |$)(.*)")
async def qg(event):
    text = event.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    if not text:
        if event.is_reply and not reply_to_id.media:
            text = reply_to_id.message
        else:
            await event.edit("`Send you text to @QoryGore so he can tweet.`")
            return
    await event.edit("`Requesting QoryGore to tweet...`")
    text = deEmojify(text)
    img = await qorygore(text)
    await event.client.send_file(event.chat_id, img, reply_to=reply_to_id)
    await event.delete()
    await purge()


@register(outgoing=True, pattern=r"^\.cmm(?: |$)(.*)")
async def cmm(event):
    text = event.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    if not text:
        if event.is_reply and not reply_to_id.media:
            text = reply_to_id.message
        else:
            await event.edit("`Give text for to write on banner!`")
            return
    await event.edit("`Your banner is under creation wait a sec...`")
    text = deEmojify(text)
    img = await changemymind(text)
    await event.client.send_file(event.chat_id, img, reply_to=reply_to_id)
    await event.delete()
    await purge()


@register(outgoing=True, pattern=r"^\.kanna(?: |$)(.*)")
async def kanna(event):
    text = event.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    if not text:
        if event.is_reply and not reply_to_id.media:
            text = reply_to_id.message
        else:
            await event.edit("`What should kanna write give text!`")
            return
    await event.edit("`Kanna is writing your text...`")
    text = deEmojify(text)
    img = await kannagen(text)
    await event.client.send_file(event.chat_id, img, reply_to=reply_to_id)
    await event.delete()
    await purge()


@register(outgoing=True, pattern=r"\.tweet(?: |$)(.*)")
async def tweet(event):
    text = event.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    if not text:
        if event.is_reply:
            if not reply_to_id.media:
                text = reply_to_id.message
            else:
                await event.edit("`What should i tweet? Give your username and tweet!`")
                return
        else:
            await event.edit("What should i tweet? Give your username and tweet!`")
            return
    if "." in text:
        username, text = text.split(".")
    else:
        await event.edit("`What should i tweet? Give your username and tweet!`")
    await event.edit(f"`Requesting {username} to tweet...`")
    text = deEmojify(text)
    img = await tweets(text, username)
    await event.client.send_file(event.chat_id, img, reply_to=reply_to_id)
    await event.delete()
    await purge()


CMD_HELP.update(
    {
        "nekobot": ">`.tweet` <username>.<tweet>"
        "\nUsage: Create tweet with custom username.\n\n"
        ">`.trump` <tweet>"
        "\nUsage: Create tweet for Donald Trump.\n\n"
        ">`.qg` <tweet>"
        "\nUsage: Create tweet for `@QoryGore`.\n\n"
        ">`.cmm` <text>"
        "\nUsage: Create banner for Change My Mind.\n\n"
        ">`.kanna` <text>"
        "\nUsage: Kanna is writing your text."
    }
)
