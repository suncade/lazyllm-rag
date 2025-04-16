# 快速开始

欢迎使用 **lazyllm-rag** 项目！本指南将帮助你快速设置并运行项目。

## 安装步骤

1. 克隆代码仓库：
    ```bash
    git clone https://github.com/suncade/lazyllm-rag.git
    cd lazyllm-rag
    ```
2. 前期准备：
    - 确保你的环境支持多线程的 SQLite3，若不支持，请参考以下步骤刷新环境：
    ```bash
    以 macbook 为例
    brew update
    brew install sqlite
    which sqlite3
    
    如果结果不是 homebrew 下的 sqlite，则需要设置如下环境变量，并重装 python
    brew uninstall python@3.10
    export PATH="/opt/homebrew/opt/sqlite/bin:$PATH"
    export LDFLAGS="-L/opt/homebrew/opt/sqlite/lib"
    export CPPFLAGS="-I/opt/homebrew/opt/sqlite/include"
    brew install python@3.10
    
    安装poetry
    例如mackbook: brew install poetry
    ```
3. 安装依赖：
    ```bash
    poetry env use /usr/local/Cellar/python@3.10/3.10.17/bin/python3.10
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

## 运行项目

1. 配置环境变量，设置 API 密钥：
    ```bash
    export LAZYLLM_<平台名称>_API_KEY=<你的-api-key>
    ```

2. 运行脚本样例：
    ```bash
    python src/rag/without_rag_retrieve.py
    python src/rag/rag_retrieve.py
    ```

3. 在终端中输入查询，与模型交互。

## 下一步

- 查看 [使用指南](usage.md) 了解更多功能。