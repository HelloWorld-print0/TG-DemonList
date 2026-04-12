from aiogram import Router, F
from aiogram.filters import Command, CommandObject
from aiogram.types import Message, CallbackQuery

from app.database import demonlist, demonlist_button, demon_name_research, top_research

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
        "/list - <b>show a demonlist</b>\n"
        "/demon (name) - <b>show a more information about demon</b>\n"
        "/top (number) - <b>show a more information about demon at this position</b>"
    )



@router.message(Command("list"))
async def cmd_list(message: Message):
    await message.answer(
        text=demonlist(0),
        reply_markup=demonlist_button(0)
    )

@router.callback_query(F.data.startswith("list_"))
async def list_pages(callback: CallbackQuery):
    page = int(callback.data.split("_")[1])

    await callback.message.edit_text(
        text=demonlist(page),
        reply_markup=demonlist_button(page)
    )

    await callback.answer()



@router.message(Command("demon"))
async def cmd_demon(message: Message, command: CommandObject):
    demon_name = command.args

    if not demon_name:
        await message.answer("Use: /demon level name\n"
                             "/help")
        return

    await message.answer(
        demon_name_research(demon_name))


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

    await message.answer(top_research(demon_id))