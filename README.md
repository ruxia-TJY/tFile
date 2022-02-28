# tFile

Encapsulate common file processing functions。

For example, delete all files with specified extensions under the folder
```python
from tFile import tFile

if tFile.removeFileByExtFromDir('Directory Path you want to delete',['list of file extensions you want to delets']):
    print(f'specified extension file delete successfully!')
```