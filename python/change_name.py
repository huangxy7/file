#读取txt文件然后重命名别的文件夹下的文件
import os
import re
filepath = 'C:/Users/Administrator/Desktop'
f=os.listdir(filepath)


changpath = 'E:/BaiduNetdiskDownload/book/C0021《工作没动力？你需要向职场倦怠说“NO”》/音频/'

file_handle = open('C:/Users/Administrator/Desktop/name.txt', mode='r')
content = file_handle.readlines( )
#print(content[:-1])


def changname():
    n=1
    changf = os.listdir(changpath)

    #print(changf)
    common_sort_list = sorted(changf)
    human_sort_list = sort_humanly(changf)

    for i in human_sort_list:
        #print(i)
        oldname = changpath+i
        os.rename(oldname,changpath+content[n-1][:-1]+".mp3")
        print(oldname+'--->'+changpath+content[n-1][:-1])
        n+=1

def tryint(s):                     #将元素中的数字转换为int后再排序
    try:
        return int(s)
    except ValueError:
        return s
 
def str2int(v_str):                #将元素中的字符串和数字分割开
    return [tryint(sub_str) for sub_str in re.split('([0-9]+)', v_str)]
 
def sort_humanly(v_list):    #以分割后的list为单位进行排序
    return sorted(v_list, key=str2int)
changname()
