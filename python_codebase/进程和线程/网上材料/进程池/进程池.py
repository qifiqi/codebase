import multiprocessing

def index_pool(data):
    res = data * data
    return res

if __name__ == "__main__":

    data =  list(range(100))#100个任务 
    pool = multiprocessing.Pool(processes = 4)#进程池大小为4

    pool_out_puts = pool.map(index_pool,data)#一次性提交大量任务
    # pool_out_puts = pool.apply(index_pool,args=(10,))#一个个提交
    pool.close()#关闭进程  不再创建进程
    pool.join()#堵塞进程
    
    print('Pool    {}'.format(pool_out_puts))
