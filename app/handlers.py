from aiogram import Router, F
from aiogram.filters import Command, CommandObject
from aiogram.types import Message, CallbackQuery

from app.database import classic_list, classic_list_button, cslist_name_research, top_posit_research
from app.database import future_list, future_list_button, ftlist_name_research

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer_photo(
        caption='<b>Demonlist On TG</b>\n'
                'The best ranking of the hardest Geometry Dash demons on TG, maintained by a dedicated community.'
                
                '\n\n<b>📋 1700+ The hardest levels</b>'
                '\n<b>👥 0 Users</b> (You can be the first)'
                
                '\n\n⚙ Write /help to see all functions!'
                '\n<tg-spoiler>© By using Demonlist API</tg-spoiler>',

        photo='https://pbs.twimg.com/profile_images/1284693744009256961/atZ4JwOr_400x400.jpg'
    )

@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "<b>⚙ List of Commands:</b>\n\n"
        
        "• /lists - <b>See all lists</b>\n"
        ""
    )

# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------

@router.message(Command("lists"))
async def cmd_list(message: Message):
    await message.answer(
        "<b>📃 Select list what you want:</b>\n\n"
        
        "🏆 /classiclist - <b>See current level list!</b>\n"
        "🔮 /futurelist - <b>See upcoming levels list!</b> (are sorted alphabetically, not by their difficulty)"
    )

# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------

# CLASSIC LIST
@router.message(Command("classiclist"))
async def cmd_cslist(message: Message):
    await message.answer(
        text=classic_list(0),
        reply_markup=classic_list_button(0)
    )

# CLASSIC LIST BUTTON
@router.callback_query(F.data.startswith("classiclist_"))
async def cslist_pages(callback: CallbackQuery):
    page = int(callback.data.split("_")[1])

    await callback.message.edit_text(
        text=classic_list(page),
        reply_markup=classic_list_button(page)
    )

    await callback.answer()


# CLASSIC LIST RESEARCH BY NAME
@router.message(Command("csdemon"))
async def cmd_csdemon(message: Message, command: CommandObject):
    csdemon_name = command.args

    if not csdemon_name:
        await message.answer("Use: /csdemon level name\n"
                             "/help")
        return

    await message.answer(
        cslist_name_research(csdemon_name))

# CLASSIC LIST RESEARCH BY POSITION
@router.message(Command("top"))
async def cmd_top(message: Message, command: CommandObject):
    if not command.args:
        await message.answer("Use: /top number\n"
                             "/help")
        return

    try:
        demon_id = int(command.args)
    except ValueError:
        await message.answer("🔢 Not a <b>number!</b>")
        return

    await message.answer(top_posit_research(demon_id))

# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------

# FUTURE LIST
@router.message(Command("futurelist"))
async def cmd_ftlist(message: Message):
    await message.answer(
        text=future_list(0),
        reply_markup=future_list_button(0)
    )

# CLASSIC LIST BUTTON
@router.callback_query(F.data.startswith("futurelist_"))
async def ftlist_pages(callback: CallbackQuery):
    page = int(callback.data.split("_")[1])

    await callback.message.edit_text(
        text=future_list(page),
        reply_markup=future_list_button(page)
    )

    await callback.answer()


# FUTURE LIST RESEARCH BY NAME
@router.message(Command("ftdemon"))
async def cmd_ftdemon(message: Message, command: CommandObject):
    ftdemon_name = command.args

    if not ftdemon_name:
        await message.answer("Use: /ftdemon level name\n"
                             "/help")
        return

    await message.answer(
        ftlist_name_research(ftdemon_name))
