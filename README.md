# Hand Gesture Volume Controller 🎚️✋

Control your system volume in real time using simple hand gestures captured through your webcam. This project uses **OpenCV**, **MediaPipe**, and **pycaw** to map the distance between your fingers to the system audio level.

---

## ✨ Features

- Real-time hand tracking using MediaPipe
- Gesture-based volume control (thumb ↔ index finger distance)
- Live volume bar and percentage display
- Smooth and intuitive UI overlay
- Works with built-in or external webcams

---

## 🛠️ Tech Stack

- **Python 3.9+**
- **OpenCV** – webcam capture & drawing
- **MediaPipe** – hand landmark detection
- **NumPy** – interpolation and math
- **pycaw** – Windows system volume control

> ⚠️ Note: This project works on **Windows only** due to pycaw.

---

## 📦 Installation

Install the required dependencies:

```bash
pip install opencv-python mediapipe numpy pycaw comtypes
```

---

## 🚀 How It Works

1. Webcam captures video frames using OpenCV
2. MediaPipe detects the hand and extracts landmarks
3. Distance between:

   - **Thumb tip (landmark 4)**
   - **Index finger tip (landmark 8)**

4. This distance is mapped to:

   - System volume range
   - On-screen volume bar

5. pycaw updates the system volume in real time

---

## 🖐️ Gesture Controls

| Gesture       | Action            |
| ------------- | ----------------- |
| Fingers close | Low / mute volume |
| Fingers apart | Increase volume   |
| Green dot     | Minimum threshold |
| Blue line     | Maximum threshold |

---

## 📁 Project Structure

```
Volume-Gesture-Control/
│
├── HandTrackingModule.py   # Custom reusable hand tracking module
├── main.py                 # Volume control application
├── README.md               # Project documentation
```

---

## ▶️ Running the Project

```bash
python main.py
```

- Press **`q`** to quit the application
- Ensure no other application is using the webcam

---

## 🧠 Key Learnings

- Building reusable CV modules
- Using MediaPipe hand landmarks effectively
- Mapping real-world gestures to system controls
- Handling OpenCV edge cases and UI stability

---

## 🧪 Common Issues

- **Camera not opening**: Check camera permissions or close other apps
- **No volume change**: Ensure pycaw is installed and Windows audio device is active
- **Laggy volume**: Can be improved using smoothing (future enhancement)

---

## 📌 Credits

Built from scratch using OpenCV & MediaPipe as a learning + portfolio project.

---

## 📜 License

This project is open-source and free to use for educational purposes.

---
