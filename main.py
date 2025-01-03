# This is a sample Python script.
import json

import fitz
import pymupdf
from PIL import Image

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def main():
    # 新建一个PDF，用pymupdf
    doc = pymupdf.Document()
    # 顺序读取target目录内的所有图片，有序
    toc = []
    for i in range(1, 185):
        # 格式： 001.png，002.png，etc
        img = Image.open('target/' + str(i).zfill(3) + '.png')
        # 新建一页
        page = doc.new_page(width=img.width, height=img.height)
        img.close()
        # 将图片写入
        page.insert_image(page.rect, filename='target/' + str(i).zfill(3) + '.png')
    # 添加目录
    toc.append([1, '封面', 1])
    toc.append([1, '袁树珊序', 2])
    toc.append([1, '蒋清渠序', 7])
    toc.append([1, '韦千里序', 9])
    toc.append([1, '目录（旧）', 12])
    toc.append([1, '广告', 17])
    toc.append([1, '卷一：法', 18])
    toc.append([2, '看命总法一', 18])
    toc.append([2, '看命总法二', 19])
    toc.append([2, '看格局法', 20])
    toc.append([2, '看格局法二', 23])
    toc.append([2, '看用神法', 25])
    toc.append([2, '看生年法一', 26])
    toc.append([2, '看月令法二（疑似有误）', 27])
    toc.append([2, '看月令法二', 28])
    toc.append([2, '看日主法', 31])
    toc.append([2, '看生时法一', 32])
    toc.append([2, '看生时法二', 33])
    toc.append([2, '看运法一', 34])
    toc.append([2, '看运法二', 35])
    toc.append([2, '看流年法', 35])
    toc.append([2, '看正官法', 36])
    toc.append([2, '看偏官法', 38])
    toc.append([2, '看官杀去留法一', 39])
    toc.append([2, '看官杀去留法二', 41])
    toc.append([2, '看官杀去留法三', 43])
    toc.append([2, '看正偏印法', 44])
    toc.append([2, '看正偏财法', 46])
    toc.append([2, '看食神法', 47])
    toc.append([2, '看伤官法', 49])
    toc.append([2, '看食伤法', 51])
    toc.append([2, '看比劫禄刃法', 52])
    toc.append([2, '看拱夹法', 53])
    toc.append([2, '看杂气墓库法', 55])
    toc.append([2, '看从局法', 57])
    toc.append([2, '看化局法', 58])
    toc.append([2, '看一行得气法', 60])
    toc.append([2, '看两神成象法', 61])
    toc.append([2, '看暗冲法一', 62])
    toc.append([2, '看暗冲法二', 63])
    toc.append([2, '看暗合法', 64])
    toc.append([2, '看六亲法一', 64])
    toc.append([2, '看六亲法二', 67])
    toc.append([2, '看贵贱法', 68])
    toc.append([2, '看贫富法', 69])
    toc.append([2, '看吉凶法', 70])
    toc.append([2, '看寿夭法', 71])
    toc.append([2, '看富贵吉寿贫贱凶夭总法', 72])
    toc.append([2, '富贵吉寿诸局', 73])
    toc.append([2, '贫贱凶夭诸局', 74])
    toc.append([2, '看富贵吉寿贫贱凶夭要法', 75])
    toc.append([2, '看科第法', 76])
    toc.append([2, '看性情法', 77])
    toc.append([2, '看疾病法', 78])
    toc.append([2, '看女命法一', 78])
    toc.append([2, '看女命法二', 80])

    # 保存
    doc.set_toc(toc)
    doc.ez_save('output.pdf')
    doc.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
