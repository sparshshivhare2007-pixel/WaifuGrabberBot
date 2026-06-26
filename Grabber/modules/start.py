import config
from Grabber import app, BOT_USERNAME, BOT_NAME
from pyrogram import filters, enums
from Grabber.core import script
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# -------------------------- Buttons -------------------------- #

buttons = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("Add to Group", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
    ],
    [
        InlineKeyboardButton("Support", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton("Guide", callback_data="guide_")
    ],
    [
        InlineKeyboardButton("🧩 ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/oye_sparsh_babu")
    ]
])

guide_buttons = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("Masters", callback_data="masters_"),
        InlineKeyboardButton("Back", callback_data="back_")
    ]])

group_buttons = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("Add to Group", url=f"https://t.me/{BOT_USERNAME}?start=true")
    ]
])

master_back = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("Back", callback_data="guide_")
    ]
])


# -------------------------- Start -------------------------- #

@app.on_message(filters.command("start"))
async def start_(_, message):
    name = message.from_user.mention
    if message.chat.type == enums.ChatType.PRIVATE:
        await message.reply_photo(photo=script.PHOTOS["START_IMG"],                         
            caption=script.START_TEXT.format(name, BOT_NAME),
            reply_markup=buttons
        )
    else:
        await message.reply_text(f"Hello everyone! I’m **{BOT_NAME}**, your anime collector companion, here to summon waifus from different universes. Add me to your group and let the collecting, trading, and competition begin!",
            reply_markup=group_buttons
        )


# -------------------------- Regex-Start -------------------------- #

@app.on_callback_query(filters.regex(r"guide_"))
async def guide_regex(_, query):
    await query.message.edit_text(script.GUIDE_TEXT, reply_markup=guide_buttons)
    
@app.on_callback_query(filters.regex(r"masters_"))
async def masters_regex(_, query):
    user_id = query.from_user.id
    if user_id not in list(set(config.OWNER_ID + config.SUDO_IDS)):
        return await query.answer("This feature is beyond your authority. Only my masters may use it. 😌",show_alert=True)
    await query.message.edit_text(script.MASTER_TEXT, reply_markup=master_back)

@app.on_callback_query(filters.regex(r"back_"))
async def home_regex(_, query):
    await query.message.edit_text(script.START_TEXT, reply_markup=buttons)
    
