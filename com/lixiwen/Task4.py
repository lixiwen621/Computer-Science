"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

def task4():

    with open('texts.csv', 'r') as f:
        reader = csv.reader(f)
        texts_list = list(reader)

    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        calls_list = list(reader)

    telephone_marketing_set = set()

    # Never receive incoming calls
    # 得到没有接听来电的号码
    incoming_calls_list = [x[1] for x in calls_list]
    outgoing_calls_list = [x[0] for x in calls_list]
    for call_list in outgoing_calls_list:
        if call_list not in incoming_calls_list:
            telephone_marketing_set.add(call_list)

    # never send texts, receive texts
    # 找到从不发送短信、接收短信的号码
    telephone_marketing_set = {
        telephone_marketing
        for telephone_marketing in telephone_marketing_set
        if not any(
            telephone_marketing == text_list[0] or telephone_marketing == text_list[1]
            for text_list in texts_list
        )
    }

    # 号码排序
    telephone_marketing_list = sorted(telephone_marketing_set)
    print("These numbers could be telemarketers: \n"
          f"{telephone_marketing_list}\n" 
          "The list of numbers should be print out one per line in lexicographic order with no duplicates")
"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.





任务 4：
电话公司希望识别可能从事电话营销的号码。请创建一个可能的电话营销号码集合，这些号码满足以下条件：
	•	这些号码只拨打外呼电话，从不发送短信、接收短信或接听来电。

请输出一条消息：
“These numbers could be telemarketers:”
<号码列表>
号码列表需要按字典顺序逐行打印，且不能有重复项。
"""

if __name__ == "__main__":
    task4()