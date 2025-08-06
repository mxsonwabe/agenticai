from functions.get_files_info import get_file_content, get_files_info

subject = "lorem.txt"
print(f"Results for '{subject}' directory: calculator")
# print(get_files_info("calculator", "."))
print(get_file_content("calculator", subject))

subject = "main.py"
print(f"\nResults for '{subject}' directory: calculator")
# print(get_files_info("calculator", subject))
print(get_file_content("calculator", "main.py"))

# subject = "/bin"
subject= "pkg/calculator.py"
print(f"\nResults for '{subject}' directory: pkg/calculator")
# print(get_files_info("calculator", subject))
print(get_file_content("calculator", "pkg/calculator.py"))

subject = "/bin/cat"
print(f"\nResults for '{subject}' directory: /bin/cat")
# print(get_files_info("calculator", subject))
print(get_file_content("calculator", "/bin/cat"))

subject = "pkg/does_not_exist"
print(f"\nResults for '{subject}' directory: pkg/does_not_exist")
print(get_file_content("calculator", "pkg/does_not_exist.py"))
