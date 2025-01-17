"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

def task1():
    # Add the phone number to the Set and get the number of phone numbers based on the Set's non-repeatable property
    # 根据Set的不可重复性来得到 电话号码的个数
    telephone_sets = set()
    with open('texts.csv', 'r') as f:
        reader = csv.reader(f)
        texts_list = list(reader)

    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        calls_list = list(reader)

    for text_list in texts_list:
        telephone_sets.add(text_list[0])
        telephone_sets.add(text_list[1])

    for call_list in calls_list:
        telephone_sets.add(call_list[0])
        telephone_sets.add(call_list[1])

    print(len(telephone_sets))

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."

telephone_sets.add(text_list[0])
telephone_sets.add(text_list[1])  in texts_list  = 2 * O(n)

telephone_sets.add(call_list[0])
telephone_sets.add(call_list[1])  in calls_list  = 2 * O(n)


Calculate Big O
Time - Complexity: 2 * O(n) + 2 * O(n) ≈ O(n)
Space - complexity: O(n) + O(m) ≈ O(n)

记录中有多少个不同的电话号码？ 
打印一条消息：
“记录中有 <count> 个不同的电话号码。”
"""

if __name__ == "__main__":
    task1()