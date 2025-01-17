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
    texts_list = []
    calls_dict = {}
    with open('texts.csv', 'r') as f:
        reader = csv.reader(f)
        texts_list = list(reader)

    if texts_list:
        texts_list.sort(key=lambda x:(
            # 数字部分的排序
            int(x[0].replace(" ","")),
            # 时间部分
            datetime.strptime(x[2], "%d-%m-%Y %H:%M:%S")
        ))

    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        calls = list(reader)
        calls_dict = {item[0]: item for item in calls}

    for line in texts_list:
        call_list = calls_dict.get(line[0])
        print(f"First record of texts <{line[0]}> texts <{line[1]}> at time <{line[2]}>")
        if call_list:
            print(f"Last record of calls <{call_list[0]}> calls <{call_list[1]}> at time <{call_list[2]}>, lasting<{call_list[3]}> seconds")


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"

第一条短信记录是什么，最后一条通话记录是什么？
打印消息：
“第一条短信记录，<来电号码>短信<应答号码>，时间<时间>”
“最后的通话记录，<来电号码>在时间<时间>呼叫<应答号码>，持续<持续>秒”
"""

if __name__ == "__main__":
    task()