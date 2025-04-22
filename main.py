import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "7698199405:AAG222XOobLWU4S1b5beMwQDmQW6ATpIguo"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot opérationnel ✅\nTape /help pour voir les commandes disponibles.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Démarrer le bot\n"
        "/help - Voir les commandes\n"
        "/signal - Voir le signal du jour"
    )

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        "📊 SIGNAL DU JOUR : AUDUSD\n\n"
        "🔹 Direction : Achat\n"
        "🔹 Zone d'entrée : 0.6525 – 0.6540\n"
        "🔹 Stop Loss : 0.6495\n"
        "🔹 Take Profit : 0.6600 / 0.6650\n\n"
        "🎯 Confluence :\n"
        "✔️ FVG H1\n"
        "✔️ Structure haussière M15\n"
        "✔️ Pas de news à haut impact\n\n"
        "⚠️ FundedNext : évite de trader 5 min avant/après news AUD"
    )
    await update.message.reply_text(message)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("signal", signal))
    app.run_polling()

if __name__ == '__main__':
    main()
