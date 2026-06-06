from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes

TOKEN = "5983773731:AAHEFikvGJyV3sLuTfi0jicoi4jLx2AwgR4"
ADMIN_ID = 1291903545

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Assalomalekum!\n\nBu bot orqali muallifga savol va takliflaringizni yuborishingiz mumkin.\n\nKanalga a'zo bolish: https://t.me/+ssZviThaOOc2NGQy")

async def forward(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Xabaringiz yuborildi! Tez orada javob berishadi.")
    await context.bot.forward_message(chat_id=ADMIN_ID, from_chat_id=update.message.chat_id, message_id=update.message.message_id)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.ALL, forward))
app.run_polling()
