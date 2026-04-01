from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8692466509:AAFfpvAYTR1Ts9N_0SCg8s5fVM03iCtqLhc"

# 🔗 Your links here
REGISTER_URL = "https://your-site.com/register"
CHANNEL_URL = "https://t.me/yourchannel"
CS_URL = "https://t.me/youradmin"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = (
        "🌿 *Welcome to Rayner's Orchard!*\n\n"
        "⚠️ *Remember we have no bonuses.*\n"
        "Do not do any private transactions to avoid getting scammed!\n\n"
        "👇 Choose an option below:"
    )

    keyboard = [
        [InlineKeyboardButton("📝 Register", url=REGISTER_URL)],
        [InlineKeyboardButton("📢 Channel", url=CHANNEL_URL)],
        [InlineKeyboardButton("🎧 Customer Service", url=CS_URL)],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        text,
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

# Run bot
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot running...")
app.run_polling()