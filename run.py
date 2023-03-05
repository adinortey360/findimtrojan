import os
import imghdr

directory_path = input("Enter directory path: ")

for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    if os.path.isfile(file_path):
        file_type = imghdr.what(file_path)
        if file_type:
            try:
                with open(file_path, 'rb') as f:
                    contents = f.read().decode('utf-8')
                if any(c.isprintable() for c in contents):
                    print(f"File {filename} appears to be an image but contains code.")
                    response = input(f"Do you want to delete {filename}? (y/n) ")
                    if response.lower() == 'y':
                        os.remove(file_path)
                        print(f"{filename} has been deleted.")
                    else:
                        print(f"{filename} has NOT been deleted.")
            except UnicodeDecodeError:
                continue
