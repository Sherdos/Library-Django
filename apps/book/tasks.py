from celery import shared_task
import os
from LIB.settings import BASE_DIR

@shared_task
def delete_photos():
    # Logic to delete photos
    photos_directory = os.path.join(BASE_DIR, 'media/photo/')  # Replace this with your actual directory path
    for filename in os.listdir(photos_directory):
        if filename.endswith('.png'):  # Change the extension as per your photo format
            os.remove(os.path.join(photos_directory, filename))
    return 'succes'


# @shared_task
# def add(x, y):
#     return x + y

# @shared_task
# def multiply(x, y):
#     return x * y