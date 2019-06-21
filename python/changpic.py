import os, sys
import cv2

#按照指定图像大小调整尺寸
def resize_image(image, height, width):
     top, bottom, left, right = (0, 0, 0, 0)

     #获取图像尺寸
     h, w, _ = image.shape

     #对于长宽不相等的图片，找到最长的一边
     longest_edge = max(h, w)    

     #计算短边需要增加多上像素宽度使其与长边等长
     if h < longest_edge:
         dh = longest_edge - h
         top = dh // 2
         bottom = dh - top
     elif w < longest_edge:
         dw = longest_edge - w
         left = dw // 2
         right = dw - left
     else:
         pass 

     #RGB颜色
     BLACK = [0, 0, 0]

     #给图像增加边界，是图片长、宽等长，cv2.BORDER_CONSTANT指定边界颜色由value指定
     constant = cv2.copyMakeBorder(image, top , bottom, left, right, cv2.BORDER_CONSTANT, value = BLACK)

     #调整图像大小并返回
     return cv2.resize(constant, (height, width))

def resizeImg(path_name, newpath):    
     for dir_item in os.listdir(path_name):
         #从初始路径开始叠加，合并成可识别的操作路径
         full_path = os.path.abspath(os.path.join(path_name, dir_item))

         if os.path.isdir(full_path):    #如果是文件夹，继续递归调用
             read_path(full_path)
         else:   #文件
             if dir_item.endswith('.png'):
                 image = cv2.imread(full_path)                
                 image = resize_image(image, 100, 100)
                 cv2.imwrite(newpath + '/' + dir_item, image)

def main():
    # 调整图片大小
    f = 'C:/Users/Administrator/Desktop/name/'
    fnew = 'C:/Users/Administrator/Desktop/name/'
    resizeImg(f, fnew)

if __name__ == "__main__":
    main()
