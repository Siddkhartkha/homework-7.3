import os

def rewrite_file(text_1=None, text_2=None, text_3=None):
    if text_1 or text_2 or text_3 is None:
        text_1 = '1.txt'
        text_2 = '2.txt'
        text_3 = '3.txt'
        os.chdir('sorted')
        output_file = "new_file.txt"
        file1_path = os.path.join(os.getcwd(), text_1)
        file2_path = os.path.join(os.getcwd(), text_2)
        file3_path = os.path.join(os.getcwd(), text_3)
        with open(file1_path, 'r', encoding='UTF8') as f1:
            file1 = f1.readlines()
        with open(file2_path, 'r', encoding='UTF8') as f2:
            file2 = f2.readlines()
        with open(file3_path, 'r', encoding='UTF8') as f3:
            file3 = f3.readlines()
        with open(output_file, 'w', encoding='UTF8') as f_total:

            if len(file1) < len(file2) and len(file1) < len(file3):
                f_total.write(text_1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
                f_total.write('\n')
            elif len(file2) < len(file1) and len(file2) < len(file3):
                f_total.write(text_2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
                f_total.write('\n')
            elif len(file3) < len(file1) and len(file3) < len(file2):
                f_total.write(text_3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)
                f_total.write('\n')

            if len(file2) > len(file1) > len(file3) or len(file2) < len(file1) < len(
                    file3):
                f_total.write(text_1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
                f_total.write('\n')
            elif len(file1) > len(file2) > len(file3) or len(file1) < len(file2) < len(
                    file3):
                f_total.write(text_2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
                f_total.write('\n')
            elif len(file1) > len(file3) > len(file2) or len(file1) < len(file3) < len(
                    file2):
                f_total.write(text_3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)
                f_total.write('\n')

            if len(file1) > len(file2) and len(file1) > len(file3):
                f_total.write(text_1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
            elif len(file2) > len(file1) and len(file2) > len(file3):
                f_total.write(text_2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
            elif len(file3) > len(file1) and len(file3) > len(file2):
                f_total.write(text_3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)
    else:
        print('Некорректный ввод')
    return

if __name__ == '__main__':
    rewrite_file()