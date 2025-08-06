import os
# from pkg.config import MAX_CHARS
MAX_CHARS = 10000

# print("===== TEST: STR =====")
# print(str)
# print("".join(str))
# print("===== TEST: END =====")

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
        return "".join(str)
    else:
        return f'Error: "{directory}" is not a directory\n'

def get_file_content(working_directory, file_path):
    cwd = os.path.abspath(working_directory)
    path = os.path.join(working_directory, file_path)
    full_path = os.path.abspath(path)
    if not full_path.startswith(cwd):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    # get content of file
    if os.path.isfile(full_path):
        # read content of file
        with open(full_path, "r") as f:
            file_contents = f.read(MAX_CHARS)
        if len(file_contents) >= MAX_CHARS:
            info = f'\n[...File "{file_path}" truncated at 10000 characters]'
            return file_contents + info
        return file_contents
    else:
        return f'Error: File not found or is not a regular file: "{file_path}"'
