# tFile

[![](https://img.shields.io/badge/language-Python-blue)](https://www.python.org/) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ruxia-TJY/tFile) ![windows](https://img.shields.io/badge/-Windows-blue?logo=windows) [![PyPI - License](https://img.shields.io/pypi/l/tFile)](https://github.com/ruxia-TJY/tFile/blob/master/LICENSE) ![PyPI](https://img.shields.io/pypi/v/tFile?logo=pypi&logoColor=ffffff&label=PyPI&labelColor=blue)

[*English*](https://github.com/ruxia-TJY/tFile/blob/master/README.md)

## 概述

封装常用文件处理函数。

## 示例

删除文件夹下指定扩展名文件

```python
from tFile import tFile

if tFile.removeFileByExtFromDir('要删除的文件夹路径',['要删除扩展名列表']):
    print(f'删除成功!')
```

## 开源协议
使用MIT协议，感谢使用