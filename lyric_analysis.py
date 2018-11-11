#!/user/bin/Saberbin python
# -*- coding:utf-8 -*-
# Author:Saberbin

import os
import jieba
import jieba.analyse
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

if __name__=='__main__':
    path=os.getcwd()
    lyric_path=path+'/'+'lyric-ch'
    os.chdir(lyric_path)
    text=''
    with open('all_lyric.txt','r',encoding='utf-8')as f:
        for line in f:
            text+=line
    words_ls=jieba.cut(text,cut_all=True)
    words_split=' '.join(words_ls)
    wc=WordCloud(width=1980,height=1680)
    wc.font_path="simhei.ttf"
    my_wordcloud=wc.generate(words_split)
    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.savefig('lyric')
    plt.show()
    # print('end')

