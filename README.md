# YOLO Object Detection 🎯

A real-time object detection application using the YOLOv8 (You Only Look Once) architecture and OpenCV to process live webcam streams.

The script initializes a lightweight YOLOv8 Nano model, processes frames from your primary camera feed, and overlays multi-class detection bounding boxes alongside confidence percentages in real time.

## ✨ Features

* Real-time object detection across 80 common categories (COCO dataset).
* Automatic model weight caching (`yolov8n.pt` auto-downloads on initial execution).
* Direct bounding-box annotation extraction via Ultralytics plotting utilities.
* Interactive live camera frame window rendering.

## 🛠️ Technologies Used

* **Python** — Core runtime environment.
* **Ultralytics YOLOv8** — Deep learning framework running object detection inference.
* **OpenCV (cv2)** — Live peripheral video ingestion and desktop rendering window surface.

## 📋 Requirements

* Python 3.10 or later
* Active internet connection for the very first run (to fetch model tracking weights).

## 🚀 Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/YOLO-Object-Detection.git
cd YOLO-Object-Detection
```
*Note: Replace `YOUR_USERNAME` with your GitHub username.*

### 2. Create a Virtual Environment
**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```
**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
python -m pip install -r requirements.txt
```

### 4. Run the Program
```bash
python Object_Detection.py
```
*If your primary python script uses a different filename, change the command accordingly.*

## 💻 Example Output
```text
Downloading https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8n.pt to 'yolov8n.pt'...
100%|████████████████████████████████████████| 6.23M/6.23M [00:00<00:00, 75.3MB/s]

0: 480x640 1 person, 1 backpack, 1 cell phone, 118.4ms
Speed: 3.2ms preprocess, 118.4ms inference, 1.5ms postprocess per frame at shape (1, 3, 480, 640)
```
*An interactive window titled "YOLO Object Detection" will spawn displaying high-confidence bounding boxes overlaying target entities.*

## 🧠 How It Works

1. **Model Loading:** The script creates a YOLOv8 Nano (`yolov8n.pt`) pipeline. If weights are missing locally, it safely caches them from remote Ultralytics releases.
2. **Webcam Capture:** OpenCV references index `0` to lock onto your default video ingestion input.
3. **Inference Cycle:** The current frame array passes directly down to the deep learning detector architecture.
4. **Overlay Extraction:** Bounding masks, object classifications, and confidence parameters are plotted right back onto the frame vector matrix.
5. **Release Interface:** Pressing the **ESC** key (ASCII 27) safely unlocks camera resources and destroys rendering frame pipelines.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
