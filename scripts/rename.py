import os
import exifread
import shutil
from datetime import datetime

SUBJECT = "TaylorSwift"  # Reemplaza con un subject

def get_date_taken(path):
    with open(path, 'rb') as f:
        tags = exifread.process_file(f)
        date_taken = tags.get('EXIF DateTimeOriginal')
        if date_taken:
            return datetime.strptime(str(date_taken), '%Y:%m:%d %H:%M:%S')
    return None

def rename_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1]
            date_taken = get_date_taken(file_path)
            
            if date_taken:
                date_str = date_taken.strftime('%Y-%m-%d_%H%M%S')
            else:
                # Use the file's modification date if EXIF date is not available
                date_modified = datetime.fromtimestamp(os.path.getmtime(file_path))
                date_str = date_modified.strftime('%Y-%m-%d_%H%M%S')
            
            new_filename = f"{date_str}_{SUBJECT}{file_extension}"
            new_file_path = os.path.join(directory, new_filename)
            
            shutil.move(file_path, new_file_path)

if __name__ == "__main__":
    directory = "/path" 
    rename_files(directory)
