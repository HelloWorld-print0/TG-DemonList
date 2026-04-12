import requests
from math import ceil
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

url = "https://api.demonlist.org/level/classic/list"
headers = {"Accept": "application/json"}

r = requests.get(url, headers=headers, timeout=15)
r.raise_for_status()

payload = r.json()
levels = payload["data"]["levels"]


PAGE_SIZE = 5

def demonlist(page=0):
    text = f"📋 Demonlist | Page {page + 1}\n\n"

    start = page * PAGE_SIZE
    end = start + PAGE_SIZE
    page_levels = levels[start:end]

    for level in page_levels:
        placement = level["placement"]
        name = level["name"]
        verifier_name = level["verifier"]["username"]
        holder_name = level["holder"]

        text += (
            f"<b>🏆#{placement} - {name}</b>\n"
            f"<b>Publisher</b> - {holder_name}\n"
            f"<b>Verifier</b> - {verifier_name}\n\n"
        )

    return text


def demonlist_button(page=0):
    buttons = []
    total_pages = ceil(len(levels) / PAGE_SIZE)

    if page > 0:
        buttons.append(
            InlineKeyboardButton(text="⬅️ Назад", callback_data=f"list_{page - 1}")
        )

    if page < total_pages - 1:
        buttons.append(
            InlineKeyboardButton(text="➡️ Дальше", callback_data=f"list_{page + 1}")
        )

    return InlineKeyboardMarkup(inline_keyboard=[buttons])



def demon_name_research(demon_name):
    demon_name = demon_name.strip().lower()

    for level in levels:
        if level["name"].lower() == demon_name:
            placement = level["placement"]
            name = level["name"]

            holder_name = level["holder"]
            verifier_name = level["verifier"]["username"]

            ingame_id = level["ingame_id"]
            url = level["verification_url"]

            return (
                f"<b>🏆#{placement} - {name}</b>\n"
                f"<b>⚒ Publisher</b> - {holder_name}\n"
                f"<b>👨‍💻 Verifier</b> - {verifier_name}\n\n"
                
                f"🆔 <b>ID</b>: {ingame_id}\n"
                f"🔗 <b>URL</b>: {url}\n\n"

                f"/help"
            )

    return ("⛔ <b>Incorrect name</b>, try again!\n"
            "f/help")


def top_research(demon_id):
    for level in levels:
        if level["placement"] == demon_id:
            placement = level["placement"]
            name = level["name"]

            holder_name = level["holder"]
            verifier_name = level["verifier"]["username"]

            ingame_id = level["ingame_id"]
            url = level["verification_url"]

            return (
                f"🏆#{placement} - {name}\n"
                f"⚒ Publisher - {holder_name}\n"
                f"👨‍💻 Verifier - {verifier_name}\n\n"

                f"🆔 <b>ID</b>: {ingame_id}\n"
                f"🔗 <b>URL</b>: {url}\n\n"
                
                f"/help"
            )

    return ("⛔ <b>Incorrect number</b>, try again!\n"
            "/help")