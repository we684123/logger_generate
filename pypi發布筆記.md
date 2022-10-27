# 打包指令
可以看看要不要生 pyproject.toml 出來，pep517 會看  

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

# 如果裝的時候死了

嘗試重裝 python 可能有用  
https://www.youtube.com/watch?v=n76DOy-jbl4  
