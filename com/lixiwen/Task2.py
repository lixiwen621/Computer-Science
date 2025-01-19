"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv


def task2():
    # dict = {telephone number : Accumulated call duration }
    # 把电话号码和累加的通话时长放到字典中
    telephone_call_duration_dict = {}
    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        calls_list = list(reader)

    for call_list in calls_list:
        telephone_call_duration_dict[call_list[0]] = (
                telephone_call_duration_dict.get(call_list[0],0) + int(call_list[3]))
        telephone_call_duration_dict[call_list[1]] = (
                telephone_call_duration_dict.get(call_list[1],0) + int(call_list[3]))

    # dict sort
    # sort_telephone_call_duration_dict = dict(sorted(
    #     telephone_call_duration_dict.items(),
    #     key=lambda x:x[1],reverse=True
    #
    # ))
    #
    # telephone_number,call_total_duration = next(iter(sort_telephone_call_duration_dict.items()))
    max_call_telephone_number = max(telephone_call_duration_dict,key=telephone_call_duration_dict.get)

    print("{} spent the longest time, {} seconds, "
          "on the phone during September 2016."
          .format(max_call_telephone_number,telephone_call_duration_dict[max_call_telephone_number]))


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".

Calculate Big O
Time - Complexity: 2 * O(n) + O(n)
Space - complexity:  O(n)



任务 2：哪个电话号码拨打电话的时间最长
期间？不要忘记接听电话所花费的时间
还有打电话的时间。
打印一条消息：
“<电话号码> 在通话期间花费的最长时间，<总时间> 秒 
2016 年 9 月。”。
"""

if __name__ == "__main__":
    task2()
