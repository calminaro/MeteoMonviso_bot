import requests
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

PDF_URL = "https://www.parcomonviso.eu/spool/meteomonviso.last.pdf"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ciao! Invia /meteo per ricevere il bollettino PDF del Monviso.")

async def meteo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # Scarica il PDF
        response = requests.get(PDF_URL)
        response.raise_for_status()

        # Salva temporaneamente il PDF
        file_path = "/tmp/meteomonviso.pdf"
        with open(file_path, "wb") as f:
            f.write(response.content)

        # Invia il PDF come documento
        await update.message.reply_document(document=open(file_path, "rb"))

    except Exception as e:
        await update.message.reply_text(f"Errore nel recupero del PDF: {e}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("meteo", meteo))

    app.run_polling()
