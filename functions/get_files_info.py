import os


def get_files_info(working_directory, directory="."):

    target_path = os.path.join(working_directory, directory)
    target_path_abs = os.path.abspath(target_path)
    working_directory_abs = os.path.abspath(working_directory)

    # Check if directory is a valid directory, return error string otherwise
    if not os.path.isdir(target_path_abs):
        return f'Error: "{target_path_abs}" is not a directory'

    # Check if target path is in working dir. If it is, build the return string. Otherwise, reuturn error string
    if target_path_abs.startswith(working_directory_abs):
        return_list = []

        try:
            # List the content in the target directory, walk through each one, and built an ouput line, to be returned
            target_path_content = os.listdir(target_path_abs)
            for item in target_path_content:
                item_path_abs = os.path.join(target_path_abs, item)
                item_dir_status = os.path.isdir(item_path_abs)
                item_file_size = os.path.getsize(item_path_abs)
                item_detail_string = f"- {item}: file_size={item_file_size} bytes, is_dir={item_dir_status}"

                if item.startswith("__"):
                    continue
                else:
                    return_list.append(item_detail_string)

            return return_list

        except PermissionError:
            return f'Error: Permission denied accessing "{target_path_abs}"'
        except FileNotFoundError:
            return f'Error: Directory "{target_path_abs}" not found'
        except OSError as e:
            return f'Error: Unable to read directory "{target_path_abs}": {str(e)}'

    else:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
