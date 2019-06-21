# -*- coding: UTF-8 -*-
from PIL import Image
import os
#输入大小

#chang_pic_size()


print("欢迎使用seven（hxy）制作的截取图片程序")
print("Welcome to the use of \"seven\" (hxy) produced by the interception picture program")
print("教程：把这个程序放在要截取图片的目录下，输入宽和高。")
print("Tutorial: place the program in the directory where you want to capture the image, type width and height.")
print("弄好的图片会在这个程序的”is_me“这个文件夹下")
print("The finished image will be in the program's \"is_me\" folder")
print("Please enter the interception width：")
in_width = input("请输入截取后的宽：")

print("输入的宽为："+in_width+"px")
print("Please enter the truncated height：")
in_height = input("请输入截取后的高：")

print("输入的高为："+in_height+"px")
filepath = os.getcwd()
def chang_pic_size(width,height,name):
    mypic = Image.open(name)
    resize = mypic.resize((int(width),int(height)))
    resize.save('.\\is_me\\'+name)
    print("已修改保存"+name+"===>is_me/"+name)
    
def changname():
    n=0
    a= 0
    changf = os.listdir("./")
    isExists=os.path.exists("./is_me")
    if not isExists:
    # 如果不存在则创建目录
    # 创建目录操作函数
        os.makedirs("./is_me/") 
    for i in changf:
        try:
            chang_pic_size(in_width,in_height,i)
            a+=1
        except IOError:
            print("读取异常可能是脚本,跳过")
        n+=1
    print("文件数量为:"+str(n-1)+"已修改："+str(a)+"个")
changname()
