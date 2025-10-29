import os

def get_file_content(working_directory, file_path):

    try:
            
        full_file_path = os.path.abspath(os.path.join(working_directory, file_path))

        #if the filepath is outside current directory, return error string
        if full_file_path.startswith(os.path.abspath(working_directory)) == False:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        #if filepath not a file, return error code
        if os.path.isfile(full_file_path) == False:
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        #Read File, convert contents to string, truncate to 10000, store limit in config file
        MAX_CHARACTERS = 10000
        with open(full_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARACTERS)
        
        with open(full_file_path, "r") as f:
            full_content = f.read()
            full_content_length = len(full_content)
        
        if full_content_length >= MAX_CHARACTERS:
                return f'{file_content_string}\n[...File "{file_path}" truncated at 10000 characters]'
        
        else:
            return file_content_string
        
    except Exception as e:
         return f"Error: {str(e)}"