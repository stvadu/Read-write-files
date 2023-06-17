def read_and_count_lines(text_file):

    with open(text_file, 'r', encoding='utf-8') as file:
        sum_lines = {}
        count = 0
        for lines in file.readlines():
            count += 1
            sum_lines[text_file] = count
        return sum_lines

dict_from_file1 = read_and_count_lines('1.txt')
dict_from_file2 = read_and_count_lines('2.txt')
dict_from_file3 = read_and_count_lines('3.txt')

dict_from_files = dict_from_file1 | dict_from_file2 | dict_from_file3
sorted_dict_from_files = dict(sorted(dict_from_files.items(), key=lambda item: item[1]))
# print(sorted_dict_from_files)

with open('result.txt', 'w+', encoding='utf-8') as file_result:
    for i in sorted_dict_from_files:
        file_result.write(i)
        file_result.write('\n')
        # print(i)
        file_result.write(str(sorted_dict_from_files[i]))
        file_result.write('\n')
        # print(sorted_dict_from_files[i])
        with open(i, 'r', encoding='utf-8') as file0:
            for line in file0:
                file_result.write(line)
                # print(line)
            file_result.write('\n')
            file_result.write('\n')