from functions.get_files_info import write_file
write_file("calculator", "/tmp/temp.txt", "this should not be allowed")

write_file("calculator", "lorem.txt", "wwaaaait, this isn't lorem ipsum")

# write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
