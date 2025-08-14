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
        cmd = ["python", f_name] + args
        # process_return (val) => execute file w/ python
        process_ret = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=True,
            timeout=30,
            text=True,
        )
    except Exception as e:
        val = f"Error: executing Python file: {e}"
        return val

    # check if chld process success
    if process_ret.returncode == 0:
        if process_ret.stdout.strip() == '':
            val = "No output produced"
        else:
            val = f"STDOUT:\n{process_ret.stdout}"
            if process_ret.stderr.strip() != '':
                val += f"\nSTDERR:\n{process_ret.stderr}"
        return val
    # child process failure
    else:
        val = f"STDOUT: {process_ret.stdout}\nSTDERR: {process_ret.stderr}\n"
        val += f"Process exited with code {process_ret.returncode}"

    return val
