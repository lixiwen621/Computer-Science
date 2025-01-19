"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from decimal import Decimal, getcontext
getcontext().prec = 4

def task3():
    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        calls_list = list(reader)

    # taskA
    # 过滤出电话号码前缀包含(080)
    bangalore_numbers_call_list = list(filter(lambda x: x[0].startswith('(080)'),calls_list))
    # 创建一个Set
    area_code_set = set()
    for call_number in bangalore_numbers_call_list:
        number = call_number[1]
        if number[0] == "7" or number == "8" or number[0] == "9":
            area_code_set.add(number[0:4])
        elif number[0] == "(":
            end = number.find(")")
            area_code_set.add(number[1:end])
    area_code_list_sort = sorted(area_code_set)
    print(f"The numbers called by people in Bangalore have codes: {area_code_list_sort}")

    # taskB
    total_bangalore_calls = len(bangalore_numbers_call_list)
    bangalore_call_bangalore_number_list = list(filter(lambda x: x[1].startswith('(080)'),bangalore_numbers_call_list))
    bangalore_call_bangalore_length = len(bangalore_call_bangalore_number_list)
    percent = Decimal(bangalore_call_bangalore_length)/Decimal(total_bangalore_calls) * 100
    print(f"{percent} percent of calls from fixed lines in Bangalore are calls to other fixed lines in "
          f"Bangalore.")

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.


Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?


Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits

任务 3：
(080) 是班加罗尔固定电话的区号。固定电话号码包括括号，因此班加罗尔的电话号码格式为 (080)xxxxxxx。

第 A 部分：
找出所有由班加罗尔拨打的电话的区号和手机号码前缀。换句话说，这些电话是从 (080) 区号拨出，拨往以下区号和手机号码前缀的：
	•	固定电话：以括号括住的区号开头。区号长度不固定，但总是以 0 开头。
	•	手机号码：没有括号，但中间有一个空格以便于阅读。手机号码的前缀是其前四位数字，且总是以 7、8 或 9 开头。
	•	推销员号码：没有括号或空格，但以区号 140 开头。

将答案以以下消息的形式打印：
“The numbers called by people in Bangalore have codes:”
<代码列表>
代码列表按字典顺序逐行打印，并且没有重复项。

任务是从班加罗尔固定电话拨出的电话记录中提取所有被呼叫号码的区号或前缀，并将它们以有序且无重复的列表形式打印

第 B 部分：
从班加罗尔的固定电话拨出的电话中，有多少百分比是拨往班加罗尔其他固定电话的？换句话说，从以 (080) 开头的电话号码拨出的所有电话中，有多少是拨往同样以 (080) 开头的号码的？

将答案以以下消息的形式打印：
“<百分比> percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.”
百分比结果保留两位小数。

计算比例：
	•	总通话数：统计所有从 (080) 开头的电话拨出的记录。
	•	班加罗尔内部通话数：统计从 (080) 开头的电话拨往同样以 (080) 开头号码的记录。
	•	计算比例公式：拨往以 (080) 开头的号码/ 总通话数

"""


if __name__ == "__main__":
    task3()