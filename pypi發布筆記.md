# 打包指令

標準：
```bash
python setup.py sdist
```

wheel：
```bash
python setup.py sdist bdist_wheel
```

easy_install：
```bash
python setup.py bdist_egg
```

all
```bash
python setup.py sdist;python setup.py sdist bdist_wheel;python setup.py bdist_egg
```
# 上傳指令

twine 要加入環境變數中
```
C:\Users\{user}\AppData\Roaming\Python\{Python38}\Scripts
```

```bash
twine upload dist/*
```

如果要上傳到 test-pypi
```bash
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

# setup readme注意
```
long_description_content_type='text/markdown',
```
