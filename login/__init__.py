#带参数的装饰器函数
# Python也支持带参数的装饰器，比如刚刚的cost_time加入一个报警机制，如果函数执行耗时大于3秒，就发出警告。
import random
import time


#
# def cost_time(warn=3):
#     def wrap(func):
#         def in_wrap():
#             start_time = time.time()
#             result = func()
#             cost = time.time() - start_time
#             print("cost time: {}".format(cost))
#             if cost > warn:
#                 print("warning, cost time is {} !!!".format(cost))
#             return result
#         return in_wrap
#     return wrap
#
# @cost_time()
# def a_func():
#     time.sleep(random.randint(1, 5))
#
# a_func()




