from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "5983773731:AAHEFikvGJyV3sLuTfi0jicoi4jLx2AwgR4"
ADMIN_ID = 1291903545
CHANNEL_LINK = "https://t.me/+ssZviThaOOc2NGQy"

WELCOME_TEXT = "Assalomalekum!\n\nBu bot orqali muallifga savol va takliflaringizni yuborishingiz mumkin.\n\nKanalga a'zo bo'lish: https://t.me/+ssZviThaOOc2NGQy"

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_TEXT)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, welcome))
app.run_polling()
