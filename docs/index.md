# `基于商汤开源LazyLLM平台搭建一个简单的rag应用`
本项目是基于商汤开源的LazyLLM平台搭建的一个简单的rag应用。
[LazyLLM](https://github.com/LazyAGI/LazyLLM)是一款低代码构建**多Agent**大模型应用的开发工具，协助开发者用极低的成本构建复杂的AI应用，并可以持续的迭代优化效果。LazyLLM提供了便捷的搭建应用的workflow，并且为应用开发过程中的各个环节提供了大量的标准流程和工具。
基于LazyLLM的AI应用构建流程是​**原型搭建 -> 数据回流 -> 迭代优化**​，即您可以先基于LazyLLM快速跑通应用的原型，再结合场景任务数据进行bad-case分析，然后对应用中的关键环节进行算法迭代和模型微调，进而逐步提升整个应用的效果。
​**LazyLLM用户文档**​： [https://docs.lazyllm.ai/](https://docs.lazyllm.ai/)

项目运行和效果展示请参考[快速开始](getting-started.md)。


#### Mkdocs简介

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

##### Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

##### Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.