from functions.get_files_info import get_files_info

return_data_test_1 = get_files_info("calculator", ".")

if "Error" in return_data_test_1:
    print(return_data_test_1)
else:
    print(f"Result for currrent directory:")
    [print(item) for item in return_data_test_1]

return_data_test_2 = get_files_info("calculator", "pkg")

if "Error" in return_data_test_2:
    print(return_data_test_2)
else:
    print(f"Result for 'pkg' directory:")
    [print(item) for item in return_data_test_2]

return_data_test_3 = get_files_info("calculator", "/bin")
if "Error" in return_data_test_3:
    print(return_data_test_3)
else:
    print(f"Result for 'pkg' directory:")
    [print(item) for item in return_data_test_3]

return_data_test_4 = get_files_info("calculator", "../")
if "Error" in return_data_test_4:
    print(return_data_test_4)
else:
    print(f"Result for 'pkg' directory:")
    [print(item) for item in return_data_test_4]
