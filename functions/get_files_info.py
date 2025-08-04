import os

def get_files_info(working_directory, directory="."):
    cwd = os.path.abspath(working_directory)
    path = os.path.join(working_directory, directory)
    full_path = os.path.abspath(path)
    if not full_path.startswith(cwd):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'    

    if os.path.isdir(full_path):
        contents = os.listdir(full_path)
        str = []
        for content in contents:
            obj_path = os.path.join(full_path, content)
            str.append(f"- {content}: ")
            str.append(f"file_size={os.path.getsize(obj_path)} bytes ")
            str.append(f"is_dir={not os.path.isfile(obj_path)}")
            str.append("\n")
        # print("===== TEST: STR =====")
        # print(str)
        # print("".join(str))
        # print("===== TEST: END =====")
        return "".join(str)
    else:
        return f'Error: "{directory}" is not a directory\n'
