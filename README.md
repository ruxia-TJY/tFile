# tFile

[![](https://img.shields.io/badge/language-Python-blue)](https://www.python.org/) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ruxia-TJY/tFile) ![windows](https://img.shields.io/badge/-Windows-blue?logo=windows) [![PyPI - License](https://img.shields.io/pypi/l/tFile)](https://github.com/ruxia-TJY/tFile/blob/master/LICENSE) ![PyPI](https://img.shields.io/pypi/v/tFile?logo=pypi&logoColor=ffffff&label=PyPI&labelColor=blue)

[*转到中文版*](https://github.com/ruxia-TJY/tFile/blob/master/README_cn.md)

## Overview
Encapsulate common file processing functions。

## Examples

delete all files with specified extensions under the folder

```python
from tFile import tFile

if tFile.removeFileByExtFromDir('Directory Path you want to delete',['list of file extensions you want to delets']):
    print(f'specified extension file delete successfully!')
```

## License
The source code is licensed unser MIT license。
Thanks for use!