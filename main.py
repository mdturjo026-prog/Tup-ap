import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8607390888:AAHdvuCwsDjrjaW7tli_qFWnrm1Aq2Pkf_8"

# 1. Flask app - Render এর পোর্ট খুশি রাখার জন্য
web_app = Flask(__name__)

@web_app.route('/')
def home():
    return "Bot is Alive! 🔥"

# 2. Telegram bot এর কাজ
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Web Service দিয়েই চলতেছে ভাই! 🔥")

async def id_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Tomar ID: {update.effective_user.id}")

def run_bot():
    print("Telegram Polling Start...")
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("id", id_command))
    application.run_polling()

if __name__ == '__main__':
    # 3. বট আলাদা Thread এ চালাও
    threading.Thread(target=run_bot).start()
    
    # 4. Flask দিয়ে Render এর পোর্ট ধরে রাখো
    port = int(os.environ.get('PORT', 10000))
    print(f"Flask Server Starting on port {port}")
    web_app.run(host='0.0.0.0', port=port)
