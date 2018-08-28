import os

resources_path_dir = os.path.abspath('.')


def config_dir(dir):
    index_file = dir + os.sep + "index.rst"
    if os.path.exists(index_file):
        with open(index_file, "r", encoding="utf-8") as file_read:
            read_lines = file_read.readlines()

        with open(index_file, 'w', encoding="utf-8") as file_write:
            for content in read_lines:
                if content == '':
                    break
                file_line_value = content
                file_write.write(file_line_value)
                if 'config_start' in content:
                    break

        current_path = os.path.abspath(dir)
        current_file_list = os.listdir(current_path)
        filter_file = [file for file in current_file_list
                       if os.path.isfile(dir + os.sep + file)
                       and file != 'index.rst'
                       and (file.endswith('.rst') or file.endswith('.md'))]

        for file in filter_file:
            name = '    ' + file.split('.')[0] + '\n'
            with open(index_file, 'a', encoding="utf-8") as file_write:
                file_write.write(name)


if __name__ == '__main__':
    files_list = os.listdir(resources_path_dir)
    filter_files = [file for file in files_list if os.path.isdir(file) and not file.startswith(".")]
    for file in filter_files:
        config_dir(file)
