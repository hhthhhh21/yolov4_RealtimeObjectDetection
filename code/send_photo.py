import telegram

# Token của bot
my_token = "your-token-api-key"

# Tạo bot
bot = telegram.Bot(token=my_token)

# Gửi ảnh
try:
    bot.sendPhoto(chat_id="6183307421", photo=open("alert.png", "rb"), caption="Có xâm nhập, nguy hiểm!")
    print("Ảnh đã được gửi thành công!")
except Exception as ex:
    print("Không thể gửi ảnh qua Telegram:", ex)
    print(type(ex).__name__, ex.args)
