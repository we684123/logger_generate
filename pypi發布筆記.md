# 打包注意

## 安裝上傳 package 的工具 twine

`twine` 是上傳用工具，必裝。

```bash
python -m pip install --user --upgrade twine
```

然後如果你是用 windows 的，`twine`指令可能不存在你的 "windows 環境 path" 中，要自己加入，路徑如下：

```
C:\Users\{user}\AppData\Roaming\Python\{Python_version}\Scripts
```

## setup.py 版本打包

這是古早版本(？)的打包方式，新版本的 pip 安裝時會跳 "警告"，說一些 XXX、OOO(忘了)，總之看起來不舒服，所以我後來跳去用符合 PEP517 標準的 pyproject.toml 來打包。

這裡有找到一篇教學 [打包 python module 到 pypi 上 by jack_DL](https://medium.com/%E8%B3%87%E5%B7%A5%E7%AD%86%E8%A8%98/%E6%89%93%E5%8C%85python-module-%E5%88%B0pypi-%E4%B8%8A-aef1f73e1774) 寫得蠻詳細的，可以參考看看。

setup.py 版本打包指令如下：

標準：

```bash
python setup.py sdist
```

wheel：

```bash
python setup.py bdist_wheel
```

easy_install：

```bash
python setup.py bdist_egg
```

ALL

```bash
python setup.py sdist;python setup.py bdist_wheel;python setup.py bdist_egg
```

## Poetry 版本打包

編寫完`pyproject.toml`後打包

```bash
poetry build
```

參考文章：  
[Publish a package on PyPi using Poetry](https://www.brainsorting.com/posts/publish-a-package-on-pypi-using-poetry/)  
[pyproject.toml poetry 官方參數說明](https://python-poetry.org/docs/pyproject/) (ps' `pyproject.toml` 是 PEP517 的產物，不是 poetry 的)

## 上傳指令

上傳到 pypi

```bash
twine upload dist/*
```

如果要上傳到 test-pypi

```bash
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

## 如果 pip 裝的時候死了

嘗試重裝 python 可能有用  
https://www.youtube.com/watch?v=n76DOy-jbl4
