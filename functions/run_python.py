import os
import subprocess

def run_python_file(working_directory, file_path, args = []):
    cwd = os.path.abspath(working_directory)
    full_path = os.path.join(working_directory, file_path)
    fp = os.path.abspath(full_path)

    if not (fp.startswith(cwd + os.sep) or fp == cwd):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(fp):
        return f'Error: File "{file_path}" not found.'
    
    f_name = os.path.basename(fp)
    if not f_name.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        cmd = args
        cmd.insert(0, 'python')
        cmd.insert(1, f_name)
        # process_return (val) => execute file w/ python
        proc_ret = subprocess.run(
            cmd,
            capture_output=True,
            timeout=30,
            text=True,
        )
    except Exception as e:
        val = f"Error: executing Python file: {e}"
        return val

    if proc_ret.returncode == 0:
        if proc_ret.stdout == '':
            val = "No output produced"
        else:
            val = f"STDOUT: {proc_ret.stdout}\nSTDERR: {proc_ret.stderr}"
    else:
        val = f"STDOUT: {proc_ret.stdout}\nSTDERR: {proc_ret.stderr}\n"
        val += f"Process exited with code {proc_ret.returncode}"

    return val
