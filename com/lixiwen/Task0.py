"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv


def task0():
    # 读取短信数据
    with open('texts.csv', 'r') as f:
        reader = csv.reader(f)
        texts_list = list(reader)

    # 读取通话数据
    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        calls_list = list(reader)

    # Find the first text message
    # 找到第一条短信记录
    first_text = texts_list[0]

    # Find the last call
    # 找到最后一条通话记录
    last_call = calls_list[-1]

    # 打印结果
    print("First record of texts, {} texts {} at time {}".format(*first_text))

    print("Last record of calls, {} calls {} at time {}, lasting {} seconds"
          .format(*last_call))


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, 
lasting <during> seconds"


任务 0：
找出短信记录中的第一条记录和通话记录中的最后一条记录。

请输出以下消息：
“First record of texts, <发信号码> texts <收信号码> at time <时间>”
“Last record of calls, <主叫号码> calls <被叫号码> at time <时间>, lasting <时长> seconds”
"""


if __name__ == "__main__":
    task0()
