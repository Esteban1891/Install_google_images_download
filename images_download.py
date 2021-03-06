from google_images_download import google_images_download # pip install google_images_download

response = google_images_download.googleimagesdownload()


def download_images(query, image_format, limit, size='medium', ratio='panoramic'):
    """
    :param query: keywords for download
    :param image_format: image format. Ex: png, jpg...
    :param limit: the maximum number of images to be downloaded
    :param size: image size: large, medium, icon
    :param ratio: the height width ratio: tall, square, wide, panoramic
    """
    arguments = {"keywords": query,
                 "format": image_format,
                 "limit": limit,
                 "print_urls": True,
                 "size": size,
                 "aspect_ratio": ratio
                 }
    try:
        response.download(arguments)
    except Exception as e:
        print('Error:', e)
