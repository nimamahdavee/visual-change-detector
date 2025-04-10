# 🔍 Visual Regression Detector with OpenCV

A simple Python tool to detect visual differences between two screenshots of a webpage.  
Perfect for automating UI tests or spotting layout issues across deploys.

## 🛠 Tech Stack
- Python 3
- Selenium
- OpenCV
- ChromeDriver

## 🚀 What it does
- Opens the desired webpage
- Takes two screenshots at different times
- Compares them pixel-by-pixel using OpenCV
- Highlights visual differences with red bounding boxes

## 💡 Use Cases
- UI testing for front-end changes
- Monitoring visual integrity of production websites
- Regression testing for design updates

## 📸 Example
Check the `output_sample.jpg` for a red-box diff between screenshots.

## 🧠 Author
[Nima Mahdavi](mailto:nimamahdavi91@gmail.com) – Automation Engineer, QA Specialist, Python Developer

## 📁 How to run
```bash
pip install opencv-python selenium
python compare.py
