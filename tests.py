from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

# Tests for get_files_info
files_info_test_1 = get_files_info("calculator", ".")

if "Error" in files_info_test_1:
    print(files_info_test_1)
else:
    print(f"Result for currrent directory:")
    [print(item) for item in files_info_test_1]

files_info_test_2 = get_files_info("calculator", "pkg")

if "Error" in files_info_test_2:
    print(files_info_test_2)
else:
    print(f"Result for 'pkg' directory:")
    [print(item) for item in files_info_test_2]

files_info_test_3 = get_files_info("calculator", "/bin")
if "Error" in files_info_test_3:
    print(files_info_test_3)
else:
    print(f"Result for 'pkg' directory:")
    [print(item) for item in files_info_test_3]

files_info_test_4 = get_files_info("calculator", "../")
if "Error" in files_info_test_4:
    print(files_info_test_4)
else:
    print(f"Result for 'pkg' directory:")
    [print(item) for item in files_info_test_4]


# Tests for get file_content
files_content_test_1 = get_file_content("calculator", "main.py")
if "Error" in files_info_test_1:
    print(files_content_test_1)
else:
    print(files_content_test_1)

files_content_test_2 = get_file_content("calculator", "pkg/calculator.py")
if "Error" in files_info_test_2:
    print(files_content_test_2)
else:
    print(files_content_test_2)

files_content_test_3 = get_file_content("calculator", "/bin/cat")
if "Error" in files_info_test_3:
    print(files_content_test_3)
else:
    print(files_content_test_3)

files_content_test_4 = get_file_content("calculator", "pkg/does_not_exist.py")
if "Error" in files_info_test_4:
    print(files_content_test_4)
else:
    print(files_content_test_4)

files_content_test_5 = get_file_content("calculator", "lorem.txt")
if "Error" in files_content_test_5:
    print(files_content_test_5)
else:
    print(files_content_test_5)