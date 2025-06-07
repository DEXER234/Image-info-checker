
---

````markdown
# 📸 Image Info Checker

A Python tool to fetch and display detailed information about an image from either a **local path** or **URL**. Handy for checking image format, size, resolution, and more!

---

## 🚀 Features

- 📂 Load image from local file path  
- 🌐 Load image from image URL  
- 🧠 Detect image information:
  - Format (JPEG, PNG, etc.)
  - Size (width × height)
  - Resolution (DPI)
  - Aspect Ratio
  - Color Mode (RGB, L, etc.)
  - Animation support (e.g. GIFs)
- 🔍 Verify image integrity (detect corruption)
- 🖼 Automatically preview image
- 🛡 Robust error handling

---

## 🧠 How It Works

```python
from image_info import check_image_information

img_info = check_image_information('path_or_url')
print(img_info)
````

---

## 📤 Sample Output

```
Image Information:
format: JPEG
size: (1280, 720)
resolution: (72, 72)
aspect_ratio: 1.78
mode: RGB
is_animated: False
```

---

## 🖥 Command Line Interface (CLI)

When run directly, the script offers a simple terminal menu:

```bash
$ python image_info.py

Welcome to our image information checker!
1. Check image information by path
2. Check image information by URL
3. Exit
```

---

## 📦 Dependencies

* Python 3.x
* [Pillow (PIL)](https://pillow.readthedocs.io/en/stable/)
* Standard `urllib` module

Install with:

```bash
pip install pillow
```

---

## 🛠 File Structure

```
image_info.py
```

This single file includes:

* Image loading functions
* Information extractor
* CLI interface

---

## ⚠️ Error Handling

* Gracefully handles:

  * Corrupted or unreadable images
  * Invalid URLs
  * Unsupported formats

---

## 🌱 Future Improvements

* 📸 Add EXIF metadata support (camera info, date, etc.)
* 📁 Batch image processing
* 💾 Export info to JSON or CSV
* 🖼 GUI with Tkinter or PyQt

---

## 👨‍💻 Author

**Debanjan Halder (Dex)**
🔧 Python Developer | 🌐 Open Source Contributor

---

## 📄 License

This project is open source and free to use.
Feel free to fork, improve, and share!

---

```

Would you like a downloadable `README.md` file or help setting this up on GitHub too?
```
