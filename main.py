#!/usr/bin/env python
import pymupdf
from PIL import Image


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
    toc.append([1, '卷一·法', 18])
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
    toc.append([2, '看小儿命法', 81])
    toc.append([1, '卷二·赋', 84])
    toc.append([2, '总纲赋', 84])
    toc.append([2, '格局赋', 85])
    toc.append([2, '行运赋', 86])
    toc.append([2, '流年赋', 88])
    toc.append([2, '正官赋', 89])
    toc.append([2, '偏官赋', 91])
    toc.append([2, '正印赋', 93])
    toc.append([2, '偏印赋', 94])
    toc.append([2, '正财赋', 95])
    toc.append([2, '偏财赋', 97])
    toc.append([2, '食神赋', 97])
    toc.append([2, '伤官赋', 99])
    toc.append([2, '比劫赋', 101])
    toc.append([2, '禄刃赋', 102])
    toc.append([2, '从局赋', 103])
    toc.append([2, '化局赋', 104])
    toc.append([2, '一行得气赋', 106])
    toc.append([2, '两神成象赋', 107])
    toc.append([2, '暗冲暗合赋', 108])
    toc.append([2, '女命赋', 109])
    toc.append([2, '陈按：女命生克之理，与男命同。若拘定男要刚女要柔之说，反不验矣。', 110])
    toc.append([1, '卷三·论', 112])
    toc.append([2, '天干论', 112])
    toc.append([2, '地支论', 113])
    toc.append([2, '干合论', 114])
    toc.append([2, '干冲论', 115])
    toc.append([2, '支三合论', 116])
    toc.append([2, '支六合论', 117])
    toc.append([2, '支方论', 118])
    toc.append([2, '支冲论', 118])
    toc.append([2, '支刑论', 120])
    toc.append([2, '支害论', 122])
    toc.append([2, '五行旺相休囚论', 123])
    toc.append([2, '十干生旺墓等位论', 124])
    toc.append([2, '十二支作用论', 129])
    toc.append([2, '支干覆载论', 130])
    toc.append([2, '诸神煞论一', 131])
    toc.append([2, '诸神煞论二', 132])
    toc.append([2, '太岁论', 133])
    toc.append([2, '月煞论', 134])
    toc.append([2, '天月二德论', 135])
    toc.append([2, '贵人论', 136])
    toc.append([2, '月将论', 137])
    toc.append([2, '驿马论', 138])
    toc.append([2, '空亡论', 139])
    toc.append([2, '劫煞论', 140])
    toc.append([2, '纳音论', 141])
    toc.append([2, '八法论', 142])
    toc.append([2, '小运论', 143])
    toc.append([2, '干支一气论', 144])
    toc.append([2, '双飞两干三朋论', 146])
    toc.append([2, '月日时禄论', 147])
    toc.append([2, '青龙伏形等格论', 148])
    toc.append([2, '福德秀气格论', 148])
    toc.append([2, '三奇论', 149])
    toc.append([2, '双美论', 150])
    toc.append([2, '十恶大败论', 151])
    toc.append([2, '壬骑龙背论', 152])
    toc.append([2, '六乙鼠贵论', 152])
    toc.append([2, '六乙鼠贵论', 152])
    toc.append([2, '六阴朝阳论', 153])
    toc.append([2, '金神论', 154])
    toc.append([2, '趋乾趋艮论', 155])
    toc.append([2, '合禄论（刑合附）', 156])
    toc.append([2, '时格论', 157])
    toc.append([2, '遥合论', 158])
    toc.append([2, '魁罡论（日德附）', 158])
    toc.append([2, '胞胎论（胎元附）', 159])
    toc.append([2, '学堂学馆论', 160])
    toc.append([2, '支属论', 161])
    toc.append([2, '字形论', 161])
    toc.append([1, '卷四·杂论', 164])
    toc.append([1, '封底', 184])
    # 保存
    doc.set_toc(toc)
    doc.ez_save('output.pdf')
    doc.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
