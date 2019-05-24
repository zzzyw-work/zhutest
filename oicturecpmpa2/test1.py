from PIL import Image
import math
import operator
from functools import reduce

def image_contrast(img1, img2):
    image1 = Image.open(img1)
    image2 = Image.open(img2)

    # 把图像对象转换为直方图数据，存在list h1、h2 中
    h1=image1.histogram()
    h2=image2.histogram()


    result = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
    return result



if __name__ == '__main__':
    img1 = r"E:\codefile\workpic\androidtest.png"  # 指定图片路径
    img2 = r"E:\codefile\biaozhun\screenshot.png"
    result = image_contrast(img1, img2)
    print(result)
    if 1>result>=0.0:print("PASS"+"图片精度是"+"100%")
    else:print("FAIL"+"图片精度是 ",result)