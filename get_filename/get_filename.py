#coding:utf-8
import os

'''
当suffix = ''时，找到指定路径下所有的文件名，也可指定后缀寻找该路径下所有以该后缀结尾的文件名
'''
def get_filename(path, suffix, res):
    if os.path.isdir(path):
        files = os.listdir(path)
        for file in files:
            file_path = os.path.join(path, file)
            if os.path.isfile(file_path):
                if file.endswith(suffix):
                    res.append(file)
            elif os.path.isdir(file_path):
                get_filename(file_path, suffix, res)
    return res

if __name__ == '__main__':
    path = input("请输入路径名: ")
    suffix = input("请输入你要查找的后缀名: ")
    print(get_filename(path, suffix, []))

