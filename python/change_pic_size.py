from PIL import Image
import os

def chang_pic_size(file_name,name):
    mypic = Image.open(file_name)
    print(mypic.size)
    resize = mypic.resize((int((mypic.width)-108),int((mypic.height)-67)))
    resize.save(name)
    print(resize.size)

#chang_pic_size()


filepath = 'C:/Users/Administrator/Desktop/pic_all/'


def changname():
    n=0
    changf = os.listdir(filepath)
    for i in changf:
        print(filepath+changf[n])
        chang_pic_size(filepath+changf[n],i)
        n+=1
changname()
