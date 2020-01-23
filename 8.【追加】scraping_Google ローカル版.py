from google_images_download import google_images_download
response = google_images_download.googleimagesdownload()

response.download({
    "keywords": "イチゴ",
    "limit": 500,
    "no_numbering": True,
    "output_directory": "images",
    "image_directory": "strawberry",
    "format": "jpg" or "jpeg",
    "print_urls": False,
    "chromedriver": r"C:\\Users\\ykita\\python\\chromedriver.exe"  #chromedriverをダウンロードして指定の場所に置いておく
    })

"""
response.download({
    "keywords": "リンゴ",
    "limit": 500,
    "no_numbering": True,
    "output_directory": "images",
    "image_directory": "apple",
    "print_urls": False,
    "format": "jpg" or "jpeg",
    "chromedriver": r"C:\\Users\\ykita\\python\\chromedriver.exe"
    })
"""