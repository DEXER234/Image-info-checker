# -*- coding: utf-8 -*-
"""
Upload your image path or URL to check its information.
Usage:
    from image_info import check_image_information
    img_info = check_image_information('path_or_url')
    print(img_info)
    Developed by: Dex(Debanjan)
"""
from PIL import Image
import urllib.request

# Load image from URL
def load_image_by_url(url):
    try:
        temp_path, _ = urllib.request.urlretrieve(url)
        img = Image.open(temp_path)
        return img
    except Exception as e:
        raise ValueError(f"Could not load image from URL {url}: {e}")

# Load image from local file
def load_image(img_path):
    try:
        img = Image.open(img_path)
        return img
    except Exception as e:
        raise ValueError(f"Could not load image from {img_path}: {e}")

# Main function to check image info (supports both URL and file path)
def check_image_information(path_or_url):
    try:
        if path_or_url.lower().startswith("http://") or path_or_url.lower().startswith("https://"):
            img = load_image_by_url(path_or_url)
        else:
            img = load_image(path_or_url)

        img.verify()  # Check if image is corrupted

        # Reopen the image since verify() closes it
        if path_or_url.lower().startswith("http://") or path_or_url.lower().startswith("https://"):
            img = load_image_by_url(path_or_url)
        else:
            img = load_image(path_or_url)

        img_info = {
            'format': img.format,
            'size': img.size,
            'resolution': img.info.get('dpi', 'N/A'),
            'aspect_ratio': img.size[0] / img.size[1] if img.size[1] else 'N/A',
            'mode': img.mode,
            'is_animated': getattr(img, 'is_animated', False)
        }
        return img_info
    except Exception as e:
        return {f"Something went wrong with {path_or_url}": str(e)}

# Command line interface
if __name__ == "__main__":
    print("Welcome to our image information checker!")
    print("1. Check image information by path")
    print("2. Check image information by URL")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice (1, 2, or 3): "))
        match choice:
            case 1:
                img_path = input("Please enter the image path: ")
                print("Checking image information from path...")
                img_info = check_image_information(img_path)
                view = load_image(img_path)
                view.show()
                print("Image Information:")
                for key, value in img_info.items():
                    print(f"{key}: {value}")
            case 2:
                img_url = input("Enter your image URL: ")
                print("Checking image information from URL...")
                img_info = check_image_information(img_url)
                view = load_image_by_url(img_url)
                view.show()
                print("Image Information:")
                for key, value in img_info.items():
                    print(f"{key}: {value}")
            case 3:
                print("Exiting the program. Goodbye!")
            case _:
                print("Invalid choice. Please enter 1, 2, or 3.")
    except ValueError:
        print("Please enter a valid number.")


