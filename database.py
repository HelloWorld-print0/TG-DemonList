import requests
from math import ceil
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

url = "https://api.demonlist.org/level/classic/list"
url1 = "https://api.demonlist.org/level/future/list"
headers = {"Accept": "application/json"}

r = requests.get(url, headers=headers, timeout=15)
r.raise_for_status()
payload = r.json()

r1 = requests.get(url1, headers=headers, timeout=15)
r1.raise_for_status()
payload1 = r1.json()

classic_levels = payload["data"]["levels"]
future_levels = payload1["data"]["levels"]

PAGE_SIZE = 5

# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------

# CLASSIC LIST
def classic_list(page=0):
    text = f"📋 Demonlist | Page {page + 1}\n\n"

    start = page * PAGE_SIZE
    end = start + PAGE_SIZE
    page_levels = classic_levels[start:end]

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

    return (f"{text}"
            f"ℹ For more information - /demon (name) or /top (number)\n"
            f"/help")

# CLASSIC LIST BUTTONS
def classic_list_button(page=0):
    buttons = []
    total_pages = ceil(len(classic_levels) / PAGE_SIZE)

    if page > 0:
        buttons.append(
            InlineKeyboardButton(text="⬅️ Back", callback_data=f"cslist_{page - 1}")
        )

    if page < total_pages - 1:
        buttons.append(
            InlineKeyboardButton(text="➡️ Next", callback_data=f"cslist_{page + 1}")
        )

    return InlineKeyboardMarkup(inline_keyboard=[buttons])


# CLASSIC LIST RESEARCH BY NAME
def cslist_name_research(csdemon_name):
    csdemon_name = csdemon_name.strip().lower()

    for level in classic_levels:
        if level["name"].lower() == csdemon_name:
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

# CLASSIC LIST RESEARCH BY POSITION
def top_posit_research(demon_id):
    for level in classic_levels:
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

# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------

# FUTURE LIST
def future_list(page=0):
    text = f"📋 Future Demonlist | Page {page + 1}\n\n"

    start = page * PAGE_SIZE
    end = start + PAGE_SIZE
    page_levels = future_levels[start:end]

    for level in page_levels:
        name = level["name"]
        level_category = level["category"]
        showcase_url = level["showcase_url"]

        text += (
            f"🏆<b>{name}</b>\n"
            f"<b>Category</b> - {level_category}\n"
            f"<b>Showcase</b> - {showcase_url}\n\n"
        )

    return (f"{text}"
            f"ℹ For more information - /ftdemon (name)\n"
            f"/help")

# FUTURE LIST BUTTONS
def future_list_button(page=0):
    buttons = []

    total_pages = ceil(len(future_levels) / PAGE_SIZE)

    if page > 0:
        buttons.append(
            InlineKeyboardButton(text="⬅️ Back", callback_data=f"ftlist_{page - 1}")
        )

    if page < total_pages - 1:
        buttons.append(
            InlineKeyboardButton(text="➡️ Next", callback_data=f"ftlist_{page + 1}")
        )

    return InlineKeyboardMarkup(inline_keyboard=[buttons])


# FUTURE LIST RESEARCH BY NAME
def ftlist_name_research(ftdemon_name):
    ftdemon_name = ftdemon_name.strip().lower()

    for level in future_levels:
        if level["name"].lower() == ftdemon_name:
            name = level["name"]

            level_category = level["category"]
            showcase_url = level["showcase_url"]

            return (
                f"🏆<b>{name}</b>\n"
                f"ℹ <b>Category</b> - {level_category}\n"
                f"🔗 <b>Showcase</b> - {showcase_url}\n\n"

                f"/help"
            )

    return ("⛔ <b>Incorrect name</b>, try again!\n"
            "/help")

# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------

