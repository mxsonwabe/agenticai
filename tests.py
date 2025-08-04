from functions.get_files_info import get_files_info

subject = "."
print(f"Results for '{subject}' directory:")
print(get_files_info("calculator", "."))

subject = "pkg"
print(f"Results for '{subject}' directory:")
print(get_files_info("calculator", subject))

subject = "/bin"
print(f"Results for '{subject}' directory:")
print(get_files_info("calculator", subject))

subject = "../"
print(f"Results for '{subject}' directory:")
print(get_files_info("calculator", subject))
