import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import asyncio

async def send_email_with_image(subject, body, to_email, image_path, sender_email="your_email@gmail.com", sender_password="your_password"):
    try:
        # Thông tin tài khoản email của bạn
        sender_email = "your_email@gmail.com"
        sender_password = "your_password"

        # Đọc nội dung của hình ảnh
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()

        # Tạo một email đa phần
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = to_email
        msg["Subject"] = subject

        # Thêm nội dung văn bản
        msg.attach(MIMEText(body, "plain"))

        # Thêm hình ảnh như một phần của email
        image = MIMEImage(image_data, name="alert.png")
        msg.attach(image)

        # Kết nối đến máy chủ SMTP của Gmail
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Gửi email
        server.sendmail(sender_email, to_email, msg.as_string())

        # Đóng kết nối
        server.quit()
        print("Send successssssssssss")
    except Exception as ex:
        print("Can not send email:", ex)

