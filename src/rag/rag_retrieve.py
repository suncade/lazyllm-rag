import lazyllm
from lazyllm import Retriever, Reranker, OnlineEmbeddingModule

# 使用商汤的在线向量模型
online_embed = lazyllm.OnlineEmbeddingModule(source="sensenova")

# 加载本地文档
documents = lazyllm.Document(
    dataset_path="/Users/cadesun/work/lazyllm-rag/data", embed=online_embed
)

# 以\n为分隔符，将文档切分为块
documents.create_node_group(name="block", transform=(lambda d: d.split("\n")))
# 定义检索器1，通过cosine相似度进行一次检索
retriever1 = lazyllm.Retriever(
    documents, group_name="CoarseChunk", similarity="cosine", topk=3
)
# 定义检索器2，通过bm25_chinese相似度进行一次检索
retriever2 = Retriever(documents, group_name="block", similarity="bm25_chinese", topk=3)

# 如果您要使用在线重排模型
# 目前 LazyLLM 支持 qwen和glm 在线重排模型，使用前请指定相应的 API key。
online_rerank = OnlineEmbeddingModule(source="qwen", type="rerank")
reranker = Reranker("ModuleReranker", model=online_rerank, similarity="bm25", topk=3)

# 定义大模型
llm = lazyllm.OnlineChatModule(source="sensenova")

# prompt 设计
prompt = "你是一个友好的 AI 问答助手，你需要根据给定的上下文和问题提供答案。\
        根据以下资料回答问题：\
        {context_str} \n "
llm.prompt(lazyllm.ChatPrompter(instruction=prompt, extro_keys=["context_str"]))


def multiway_reranker_test(query):
    """
    1. 执行多路检索
    2. 执行重排序
    3. 大模型推理
    4. 返回大模型的回答
    注意：
        1. 多路检索的结果是一个列表，每个元素是一个字典，包含了检索到的节点和对应的分数
    Args:
        query: 用户输入的问题
    Returns:
        res: 大模型的回答

    """
    # 第一路检索结果
    result1 = retriever1(query=query)
    # 第二路检索结果
    result2 = retriever2(query=query)
    # 将第一路和第二路的检索结果进行合并，并进行重排序
    result = reranker(result1 + result2, query=query)

    # 将query和召回节点中的内容组成dict，作为大模型的输入
    res = llm(
        {
            "query": query,
            "context_str": "".join([node.get_content() for node in result]),
        }
    )

    # print(f'Answer: {res}')
    return res


def communicate_test():
    """
    1. 交互测试
    2. 输入exit退出
    """
    while True:
        # 获取用户输入
        user_input = input("\n请输入您的问题（输入 exit 退出）：").strip()

        # 退出条件
        if user_input.lower() == "exit":
            print("程序已退出。")
            break

        # 处理非空输入
        if user_input:
            try:
                # 处理查询并打印结果
                result = multiway_reranker_test(user_input)
                print("大模型输出结果：")
                print(result)
            except Exception as e:
                print(f"处理查询时发生错误：{str(e)}")
        else:
            print("输入不能为空，请重新输入。")


if __name__ == "__main__":
    communicate_test()
