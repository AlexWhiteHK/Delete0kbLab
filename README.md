# 删除空的 .lab 文件

这个 Python 程序用于删除指定目录下大小为 0KB 的 `.lab` 文件及其对应的 `.wav` 文件。

## 使用方法
1.安装所需的依赖项：`pip install pydub`。
2.在命令行中运行以下命令：
python main.py 目录路径 --confirm
如果不附带--confirm,将仅输出0kb对应的文件，推荐第一次先核对防止其他不必要问题。
