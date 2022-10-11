
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor,as_completed
import time

#Python3.2以后带来了concurrent.futures模块
#这个模块具有线程池和进程池、管理并行编程任务、处理非确定性的执行流程、进程/线程同步等功能

#concurrent.futures.Executor 这是一个虚拟基类,提供了异步执行的方法
#submit(function,argument)   调度函数(可调用对象)的执行,将argument作为参数传入
#map(function,argument)      将argument作为参数执行函数,以异步的方式
#shutdown(Wait=True)         发出让执行者释放所有资源的信号
#concurrent.futures.Future   其中包括函数的异步执行,Future对象是submit任务(即带有参数的functions) 到executor的实例

#Executor是抽象类,可以通过子类访问,即线程或进程的ExecutorPools
#因为,线程或进程的实例时依赖于资源的任务,所以最好以"池"的形式将他们组织在一起,作为可以重用的launcher或executor

number_list = [1,2,3,4,5,6,7,8,9,10]

def add_number(data):#这个函数  只能消耗CPU资源  没啥意义

    item = count(data)
    return item

def count(number):#单纯计算  随便写

    for i in range(0,5000000):
        i = i + 1

    return i * number

if __name__ == "__main__":
    
    start_time = time.time()#程序启动时间



    #开启线程池  CPU密集型 慢     IO密集型  快
    # with ThreadPoolExecutor(max_workers = 5) as t:# max_workers参数为 你要开多少个线程

    #     for item in number_list:#提交任务 
    #         t.submit(add_number,item)

    #     reqs = [t.submit(add_number,item) for item in number_list]#提交任务 简洁写法
    #     for req in as_completed(reqs):# 转成 可迭代对象
    #         print(req.result())#打印信息



    #开启进程池  CPU密集型 快     IO密集型  快
    with ProcessPoolExecutor(max_workers = 5) as t:# max_workers参数为 你要开多少个线程

        for item in number_list:#提交任务 
            t.submit(add_number,item)

        # reqs = [t.submit(add_number,item) for item in number_list]#提交任务 简洁写法
        # for req in as_completed(reqs):# 转成 可迭代对象
        #     print(req.result())#打印信息

    print('程序总耗时：{}'.format(time.time() - start_time))#当前时间 减去 启动时间 = 程序过程耗时