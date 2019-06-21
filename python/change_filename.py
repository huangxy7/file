import os
import re

changpath = 'D:/file_test/书单(专题)/B0082《五本沟通圣经，告诉你打动人心的说话之道》/音频/'
#print(content[:-1])


def changname():
    n=1
    changf = os.listdir(changpath)
    common_sort_list = sorted(changf)
    human_sort_list = sort_humanly(changf)
    for i in human_sort_list:
        oldname = changpath+i
        os.rename(oldname,changpath+str(n)+"_"+i)
        print(oldname+'--->'+changpath+str(n)+"_"+i)
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
