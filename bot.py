from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters
import os

TOKEN = os.getenv("BOT_TOKEN")

# 🔘 Buttons (edit your links here)
def get_buttons():
    keyboard = [
        [InlineKeyboardButton("Register", url="https://your-site.com/register")],
        [InlineKeyboardButton("Channel", url="https://t.me/yourchannel")],
        [InlineKeyboardButton("Customer Service", url="https://t.me/youradmin")]
    ]
    return InlineKeyboardMarkup(keyboard)

# 🟢 Start command (private chat)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to BYD.\n\n"
        "Remember we have no bonuses.\n"
        "Do not do any private transaction to avoid getting scammed.\n\n"
        "Choose an option below:",
        reply_markup=get_buttons()
    )

# 🟢 Welcome message (when someone joins group)
async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for user in update.message.new_chat_members:
        await update.message.reply_text(
            f"Welcome {user.first_name}.\n\n"
            "Remember we have no bonuses.\n"
            "Do not do any private transaction to avoid getting scammed.\n\n"
            "Choose an option below:",
            reply_markup=get_buttons()
        )

# 🚀 Run bot
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))

print("Bot is running...")
app.run_polling()
