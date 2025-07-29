# telegram_utils.py
import telegram
import asyncio

async def send_telegram(photo_path="alert.png"):
    try:
        my_token = "your-token-api-key"
        bot = telegram.Bot(token=my_token)
        with open(photo_path, "rb") as photo:
            await bot.sendPhoto(chat_id="6183307421", photo=photo, caption="Có chó, nguy hiểm!")
        print("Send success")
    except telegram.error.TimedOut as e:
        print("Request timed out:", e)
    except Exception as ex:
        print("Can not send message telegram", ex)
