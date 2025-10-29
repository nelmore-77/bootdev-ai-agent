import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.abspath(os.path.join(working_directory, directory))

    #if abs path dir not in working dir
    #return error string below:
    if full_path.startswith(os.path.abspath(working_directory)) == False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    #if directory not actually a directory
    #return error string below
    if os.path.isdir(full_path) == False:
        return f'Error: "{directory}" is not a directory'

    #final function should return string in this format:
    # - README.md: file_size=1032 bytes, is_dir=False
    # - src: file_size=128 bytes, is_dir=True
    # - package.json: file_size=1234 bytes, is_dir=False
    file_info = ""
    Directory_Contents = os.listdir(full_path)
    print(Directory_Contents)
    for item in Directory_Contents:
        item_path = os.path.join(full_path, item)
        size = os.path.getsize(item_path)
        dir_check = os.path.isdir(item_path)
        output = f"- {item}: file_size={size}, is_dir={dir_check}"
        file_info += f"{output}\n"

    return file_info