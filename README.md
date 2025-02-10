# 环境配置

## python

```bash
# 安装管理包
brew install pyenv

# 安装版本
pyenv install 3.10.14

# 检查是否正确安装 Python 版本
pyenv versions

# 设置默认版本
pyenv global 3.10.14

# 查看版本
# 如果执行后提示command not found: python，则需要检查环境变量是否正确配置了 pyenv，如果没有则在~/.zshrc里面添加export PATH="$HOME/.pyenv/shims:$PATH"并执行source ~/.zshrc
python --version

# 指定项目使用的 Python 版本
pyenv local 3.10.14
```

## poetry 管理依赖

```bash
# 如果没有poetry则先安装
pip install poetry

# 初始化poetry配置
poetry init

# 创建虚拟环境
poetry install

# 激活虚拟环境
poetry shell

# 添加依赖，在add后面加上--dev表示添加开发依赖
poetry add <package-name>

# 移除依赖
poetry remove <package-name>
```

## poppler 工具包

如果你使用 MacOS，可以通过 Homebrew 安装：
```bash
brew install poppler
```

如果你使用 Ubuntu/Debian Linux：

```bash
sudo apt-get install poppler-utils
```

如果你使用 Windows，可以通过以下步骤：

```
下载 poppler for Windows
将解压后的 bin 目录添加到系统环境变量 PATH 中
```

安装完 poppler 后，代码就能正常运行了。poppler 是一个强大的 PDF 渲染引擎，它能帮助我们更好地处理 PDF 文件。

# 安装运行

## 安装依赖

```bash
poetry install
```

## 准备数据

将需要处理的pdf文件拷贝到pdf_folder里面

## 运行

```bash
sh start.sh
```

运行完成后，会在output_folder里面生成处理后的pdf文件。

