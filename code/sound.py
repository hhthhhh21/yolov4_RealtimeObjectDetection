import asyncio
import time
from playsound import playsound

async def mainnn():
    # Giả sử có người vào vùng cảnh báo
    detected_person = True

    if detected_person:
        # Phát âm thanh cảnh báo
        playsound('telegrsm/y2meta.com - Còi báo thức, âm thanh kinh hoàng trong quân đội (128 kbps).mp3')  # Thay đổi đường dẫn đến file âm thanh của bạn

if __name__ == "__main__":
    asyncio.run(mainnn())