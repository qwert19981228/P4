import threading,time,copy

def download(task1,task2):
    # 下载每一个文件
    newlist = copy.copy(task1)
    for i in newlist:
        # print(i,'-----')
        # print(task1,'-----')

        print('开始下载任务%s'%i)
        time.sleep(1)
        # 将下载好的文件从 下载任务列表删除
        task1.remove(i)
        # 将下载好的文件 写入到 进度列表
        task2.append(i)
        print('资源%s下载完成'%i)


if __name__ == '__main__':
    # 下载任务列表
    task1_list = ['无码高清校园春色','番号11111','金刚葫芦娃','大娃','二娃','蛇妖','葫芦小金刚']
    total= len(task1_list)
    #  进度列表
    task2_list = []
    # 开启线程去下载
    t1 = threading.Thread(target=download,args=(task1_list,task2_list))
    t1.start()

    # 实时监听下载进度（实时获取列表的变化）
    while True:
        time.sleep(1)
        # print(task1_list,'下载任务列表')
        # print(task2_list,'完成任务列表')

        # 进度 使用完成任务的个数 / 总任务的个数
        res = len(task2_list)/total
        print('下载进度%s'%int(res*100))

        if int(res*100) == 100:
            print('下载完成')
            break

