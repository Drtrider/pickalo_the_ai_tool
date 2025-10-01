import os


def get_file_content(working_directory, file_path):

    target_path = os.path.join(working_directory, file_path)
    target_path_abs = os.path.abspath(target_path)
    working_directory_abs = os.path.abspath(working_directory)

    # Check if file_path is a file
    if not os.path.isfile(target_path_abs):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    # Check if file_path is outside the working directory
    if target_path_abs.startswith(working_directory_abs):
        max_chars = 10000

        with open(target_path_abs, "r") as f:
            file_content_string = f.read(max_chars)

        if len(file_content_string) == max_chars:
            return f'{file_content_string}\n[...File "{file_path}" truncated at {str(max_chars)} characters]'
        else:
            return file_content_string
    else:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
