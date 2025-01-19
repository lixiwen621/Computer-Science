"""
Read file into texts and calls.
It's ok if you don't understand how to read files.

The text data (text.csv) has the following columns: sending telephone number (string),
receiving telephone number (string), timestamp of text message (string).

The call data (call.csv) has the following columns: calling telephone number (string), receiving telephone number (string),
start timestamp of telephone call (string), duration of telephone call in seconds (string)

文本数据（text.csv）有以下列：发送电话号码（字符串）、接收电话号码（字符串）、短信时间戳（字符串）。
通话数据（call.csv）包含以下列：呼叫电话号码（字符串）、接收电话号码（字符串）、电话呼叫开始时间戳（字符串）、电话呼叫时长（秒）（字符串）

 读取短信和电话的文件
"""
import csv
from datetime import datetime

def task():
    # 读取短信数据
    with open('texts.csv', 'r') as f:
        reader = csv.reader(f)
        texts_list = list(reader)

    # 读取通话数据
    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        calls_list = list(reader)

    # Find the first text message (sorted by time)
    # 找到第一条短信记录（按时间排序）
    texts_list.sort(key=lambda x: datetime.strptime(x[2], "%d-%m-%Y %H:%M:%S"))
    first_text = texts_list[0]

    # Find the last call (sorted by time)
    # 找到最后一条通话记录（按时间排序）
    calls_list.sort(key=lambda x: datetime.strptime(x[2], "%d-%m-%Y %H:%M:%S"))
    last_call = calls_list[-1]

    # 打印结果
    print(f"First record of texts, {first_text[0]} texts {first_text[1]} at time {first_text[2]}")
    print(f"Last record of calls, {last_call[0]} calls {last_call[1]} at time {last_call[2]}, lasting {last_call[3]} seconds")


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"


Calculate Big O
sort texts is O(n log n)
sort calls is O(m log m)
print(first_text)  O(1)
print(last_call)  O(1)

Time - Complexity: O(n log n) + O(m log m) + O(1) + O(1) ≈ O(n log n) 

Time - Complexity: O(n)
Space - complexity: O(n+m) ≈ O(n)


第一条短信记录是什么，最后一条通话记录是什么？
打印消息：
“第一条短信记录，<来电号码>短信<应答号码>，时间<时间>”
“最后的通话记录，<来电号码>在时间<时间>呼叫<应答号码>，持续<持续>秒”
"""

if __name__ == "__main__":
    task()