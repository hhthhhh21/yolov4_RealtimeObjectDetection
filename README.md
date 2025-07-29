# Realtime Object Detection using YOLOv4-Tiny

## Introduction

This project implements a real-time intrusion detection system using the YOLOv4-Tiny model. When a person is detected within a predefined danger zone, the system:

- Draws bounding boxes and centroids on camera frames  
- Triggers an alert with visual warning  
- Sends photo notifications via **Telegram** and **Email**  
- Plays an **alarm sound** to deter intrusion  

It is designed for scenarios requiring **automated security monitoring** using low-latency object detection.
You can watch a short [**demo video here**](https://youtu.be/orFa52maBXw?si=LjydZJmOwiLJoZgR) to see the system in action.

---

## Features

- Real-time object detection using YOLOv4-Tiny (OpenCV DNN)
- Polygon-based danger zone with shapely geometry
- Send alerts via:
  - Telegram bot (with image and warning)
  - Email with photo attachment
  - Sound alarm (local audio)
- Asynchronous messaging and thread-safe scheduling
- Modular codebase (image sending, sound, email, main detection)

---

## Folder Structure

```
IntrusionDetection_YOLOv4/
└── code/
    ├── main.py                 # Entry point: start camera and detection
    ├── yolodetect.py           # YOLOv4 detection class and alert handling
    ├── email_noti.py           # Send email with photo attachment
    ├── telegram_noti.py        # Send photo alert via Telegram
    ├── send_photo.py           # Utility: resize and save alert image
    ├── sound.py                # Play local alarm sound
    ├── y2mate.com-[audio].mp3  # Alarm sound file
    ├── setup.txt               # Setup instructions and requirements
└── model/
    ├── yolov4-tiny.weights
    ├── yolov4-tiny.cfg
    └── classnames.txt
├── slide_presentation.pdf  # Project summary
```

---

## Setup Instructions

> Ensure Python 3.10+ and required packages are installed.

### 1. Clone Repository

```bash
git clone https://github.com/hhthhhh21/IntrusionDetection_YOLOv4.git
cd IntrusionDetection_YOLOv4
```

### 2. Install Dependencies

```bash
pip install opencv-python shapely python-telegram-bot
```

> Optionally install: `smtplib`, `asyncio`, and other built-in libraries.

---

## Usage

### 1. Configure Alert Zones
In `main.py`, define the polygon danger zone (`points = [...]`) as a list of coordinates.

```python
points = [(x1, y1), (x2, y2), (x3, y3), ...]
```

### 2. Set Telegram and Email Credentials

- In `telegram_noti.py`, replace `"your-token-api-key"` and chat_id with your real values.
- In `email_noti.py`, configure sender email, SMTP server, and password.

### 3. Run the System

```bash
python main.py
```

The webcam feed will open. If a **person** enters the defined polygon area, the system will:
- Display “ALARM” on screen  
- Save a resized `alert.png`  
- Send Telegram photo alert  
- Send email with image attachment  
- Play warning sound

---

## Model & Detection

- **Model:** YOLOv4-Tiny  
- **Framework:** OpenCV DNN module  
- **Detection class:** Only `person` is currently detected (can be changed via `detect_class`)

### Model Files
Place the following inside the `model/` folder:
- `yolov4-tiny.cfg`
- `yolov4-tiny.weights`
- `classnames.txt` (should include 'person' on one line)

---

## Alert Logic

The `YoloDetect.alert()` function ensures alerts are not spammed. By default, it waits **15 seconds** between alerts to avoid repetition.

You can adjust this interval with:

```python
self.alert_telegram_each = 15  # seconds
```

---

## Future Improvements

- Add face recognition for identity verification  
- Use external camera (IP cam or RTSP)  
- Integrate with a database to store alert history  
- Deploy as a background service with GUI dashboard  

---

## Credits

Developed as part of an AI security application project using OpenCV, YOLOv4, and messaging APIs.
