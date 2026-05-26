import logging
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ضع توكن البوت هنا
BOT_TOKEN = "8704302525:AAFYQoHZmJi-42scIIrRvr46GIw9goigJtM"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    name = user.first_name

    # "قياس" النسبة 😄
    score = random.randint(1, 100)

    if score >= 90:
        emoji = "😍🔥"
        comment = "أنت من أجمل الناس على وجه الأرض!"
    elif score >= 70:
        emoji = "😊✨"
        comment = "جميل/ة جداً، ما شاء الله!"
    elif score >= 50:
        emoji = "🙂"
        comment = "جمال عادي، بس فيك شي مميز!"
    elif score >= 30:
        emoji = "😐"
        comment = "الجمال في الروح مو في الشكل 😅"
    else:
        emoji = "💀"
        comment = "الله يعين... بس أكيد عندك مواهب ثانية! 😂"

    message = (
        f"مرحباً {name}! 👋\n\n"
        f"🔬 جاري قياس نسبة جمالك...\n"
        f"━━━━━━━━━━━━━━━\n"
        f"📊 نتيجتك: {score}% {emoji}\n"
        f"━━━━━━━━━━━━━━━\n"
        f"💬 {comment}\n\n"
        f"اضغط /start مرة ثانية لو ما عجبتك النتيجة 😂"
    )

    await update.message.reply_text(message)


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ البوت شغّال! اضغط Ctrl+C لإيقافه.")
    app.run_polling()


if __name__ == "__main__":
    main()
