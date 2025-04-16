import lazyllm

"""
测试不带RAG的模型
注意：需要先在平台注册一个账号，然后根据下面平台对应的获取 API key 的链接获取所需要的key(注意:sensenova需要获取两个key)，并设置对应的环境变量：
export LAZYLLM_<使用的平台环境变量名称，大写>_API_KEY=<申请到的api key>
"""
llm_without_rag = lazyllm.OnlineChatModule(source="sensenova")
while True:
    query = input("query(enter 'quit' to exit): ")
    if query == "quit":
        break
    res = llm_without_rag.forward(query)
    print(f"answer: {res}")
