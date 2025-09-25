import os

def get_files_info(working_directory, directory="."):

    target_path = os.path.join(working_directory, directory)
    target_path_abs = os.path.abspath(target_path)
    working_directory_abs = os.path.abspath(working_directory)

    # Check if directory is a valid directory
    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'
    
    # If the path of directory is outside the working_directory, throw an error
    if target_path_abs in working_directory_abs:
        return_list = []

        target_path_content = os.listdir(target_path_abs)
        for item in target_path_content:
            item_dir_status = os.path.isdir(item)
            item_file_size = os.path.getsize(item)
            item_detail_string = f"- {item}: file_size={item_file_size} bytes, is_dir={item_dir_status}"

        pass

    else:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'