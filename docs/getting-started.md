# 快速开始

欢迎了解 **lazyllm-rag** 项目！本指南将帮助你快速设置并运行该项目。
本项目基于LazyLLM V0.4.1版本搭建。
[LazyLLM](https://github.com/LazyAGI/LazyLLM)是一款低代码构建**多Agent**大模型应用的开发工具，协助开发者用极低的成本构建复杂的AI应用，并可以持续的迭代优化效果。LazyLLM提供了便捷的搭建应用的workflow，并且为应用开发过程中的各个环节提供了大量的标准流程和工具。
基于LazyLLM的AI应用构建流程是​**原型搭建 -> 数据回流 -> 迭代优化**​，即您可以先基于LazyLLM快速跑通应用的原型，再结合场景任务数据进行bad-case分析，然后对应用中的关键环节进行算法迭代和模型微调，进而逐步提升整个应用的效果。
​**用户文档**​： [https://docs.lazyllm.ai/](https://docs.lazyllm.ai/)

## 安装步骤

1. 克隆代码仓库：

    ```
    git clone https://github.com/suncade/lazyllm-rag.git
    cd lazyllm-rag
    ```

2. 前期准备：
    - 确保你的环境支持多线程的 SQLite3，若不支持，请参考以下步骤刷新环境：

    ```
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

    ```
    poetry env use /usr/local/Cellar/python@3.10/3.10.17/bin/python3.10
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

## 运行项目

1. 配置环境变量，设置 API 密钥：
    ```
    export LAZYLLM_SENSENOVA_API_KEY=<你的-api-key>
    export LAZYLLM_SENSENOVA_SECRET_KEY=<你的-secret-key>
    export LAZYLLM_QWEN_API_KEY=<你的-api-key>
    export LAZYLLM_<平台名称>_API_KEY=<你的-api-key>
    ```

2. 运行脚本样例：

    ```
    python src/rag/without_rag_retrieve.py
    python src/rag/rag_retrieve.py
    ```

3. 在终端中输入查询，与模型交互。

## 下一步

- 查看 [使用指南](usage.md) 了解更多细节。