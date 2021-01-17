# 小说人物关系解析器

## 1、工程说明

此工程采用**python3.7.3**版本开发，编译请注意配套python版本

> 尽量解决linux与window脚本的差异化处理工作

## 2、研发说明

### 2.1、下载工程

```bash
git clone https://github.com/Clockcai/Entity_Relation_Parser.git
```

请参考[官方指南](https://pip.pypa.io/en/stable/installing/)

### 2.4、依赖

- Python 3.7.3
- pip 20.2.4
- 其余请看requirement.txt

### 2.2、安装pip包管理器

请参考[官方指南](https://pip.pypa.io/en/stable/installing/ "缺失pip则如此安装")

### 2.5 安装虚拟环境

本项目在研发环境下推荐使用venv作为虚拟环境运行

```bash
cd Entity_Relation_Parser
# 创建虚拟python环境，并把虚拟环境文件添加到venv目录下
python -m venv yourVenvName
# 如果是window系统，请执行：
cd yourVenvName
cd Scripts
activate.bat
# 如果是OSX Linux系统，请执行：
source ./yourVenvName/bin/activate
```

### 2.6、在线安装模块

```bash
pip install -r requirement.txt
```

### 