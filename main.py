import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "7698199405:AAG222XOobLWU4S1b5beMwQDmQW6ATpIguo"
CAPITAL = 50000  # Montant utilisé pour calculer le risque

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot opérationnel ✅\nTape /help pour voir les commandes disponibles.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Démarrer le bot\n"
        "/help - Voir les commandes\n"
        "/signal - Voir le signal du jour\n"
        "/risk [pourcentage] sl [stoploss] - Calcul de la taille de lot"
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

async def risk(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        args = context.args
        if len(args) < 3 or args[1].lower() != "sl":
            raise ValueError("Format invalide")
        risk_percent = float(args[0])
        stop_loss = float(args[2])
        risk_amount = CAPITAL * (risk_percent / 100)
        lot_size = round(risk_amount / stop_loss, 2)
        response = (
            f"📌 Calcul du lot :\n"
            f"💰 Capital : {CAPITAL}$\n"
            f"📉 Risque : {risk_percent}% = {risk_amount}$\n"
            f"🛑 Stop Loss : {stop_loss} pips\n"
            f"📏 Taille de lot : {lot_size}"
        )
    except:
        response = "❌ Utilisation : /risk [pourcentage] sl [stoploss]\nExemple : /risk 0.5 sl 30"
    await update.message.reply_text(response)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("signal", signal))
    app.add_handler(CommandHandler("risk", risk))
    app.run_polling()

if __name__ == '__main__':
    main()
