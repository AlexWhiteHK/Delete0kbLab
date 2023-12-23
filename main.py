import os
import shutil
import argparse

def find_empty_lab_files(directory):
    empty_lab_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".lab"):
                file_path = os.path.join(root, file)
                if os.path.getsize(file_path) == 0:
                    empty_lab_files.append(file_path)
    return empty_lab_files

def delete_files(file_paths):
    for file_path in file_paths:
        try:
            os.remove(file_path)
            print(f"Deleted file: {file_path}")
            wav_file = os.path.splitext(file_path)[0] + ".wav"
            if os.path.isfile(wav_file):
                os.remove(wav_file)
                print(f"Deleted file: {wav_file}")
        except OSError as e:
            print(f"Error deleting file: {file_path}\n{str(e)}")

def main(directory, confirm):
    empty_lab_files = find_empty_lab_files(directory)
    count = len(empty_lab_files)
    for file in empty_lab_files:
        print(file)
    print(f"检索到 {count} 个大小为 0KB 的 .lab 文件:")
    if count > 0 and confirm:
        delete_files(empty_lab_files)
        print("文件已删除完毕")
    elif count > 0 and not confirm:
        print("附带confirm参与以删除以上文件")
    else:
        print("未找到大小为 0KB 的 .lab 文件.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="删除大小为0KB的.lab文件及其对应的.wav文件")
    parser.add_argument("directory", help="要检索的目录路径")
    parser.add_argument("--confirm", action="store_true", help="确认删除文件")
    args = parser.parse_args()

    directory_path = args.directory
    confirm_delete = args.confirm

    main(directory_path, confirm_delete)