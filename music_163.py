#!/user/bin/Saberbin python
# -*- coding:utf-8 -*-
# Author:Saberbin

import re
import requests
import os
import json
from bs4 import BeautifulSoup
import jieba
import jieba.analyse
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#请求网易云api获取html文件
def get_html(url):
    header={'User-Agent':'Mozilla/5.0(Windows NT 6.1; Win64; x64) AppleWebkit/537.36(KHTML,like Gecko) Chrome/67.0.3396.87 Safari/537.36','Referer':'http://music.163.com/','Host':'music.163.com'}
    # header= {
    #     'User-Agent': 'Mozilla/5.0(Windows NT 6.1; Win64; x64) AppleWebkit/537.36(KHTML,like Gecko) Chrome/67.0.3396.87 Safari/537.36'
    # }
    try:
        r=requests.get(url,headers=header)
        r.encoding=r.apparent_encoding
        html=r.text
        return html
    except:
        print('requsts error!!')
        #return None
        pass
#获取歌词
def get_lyric(song_id):
    url='http://music.163.com/api/song/lyric?'+'id='+str(song_id)+'&lv=1&kv=1&tv=-1'
    html=get_html(url)
    json_obj=json.loads(html)
    try:
        initial_lyric = json_obj['lrc']['lyric']
    except KeyError:
        return None
    regex=re.compile(r'\[.*\]')
    final_lyric=re.sub(regex,'',initial_lyric).strip()
    #print(final_lyric)
    return final_lyric
#创建文件夹，保存歌词等文件
def creat_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    else:
        print('该文件夹已被创建')

#保存歌词文件
def write_text(song_name,lyric,folder_path):
    print('Now writing song:{}'.format(song_name))#打印正在保存的歌词文件
    with open(folder_path+'{}.txt'.format(song_name),'w',encoding='utf-8') as fp:
        fp.write(lyric)
#从html中提取歌曲信息
def get_singer_info(html):
    soup=BeautifulSoup(html,'html.parser')
    links=soup.find('ul',class_='f-hide').find_all('a')
    song_IDs=[]
    song_names=[]
    for link in links:
        song_ID=link.get('href').split('=')[-1]
        song_name=link.get_text()
        song_IDs.append(song_ID)
        song_names.append(song_name)
    return zip(song_names,song_IDs)


#将读取的歌词写入到all_lyric文件中，并删除歌词的空行
def write_lyric(lyric,fp):
    i=1
    with open(lyric, 'r', encoding='utf-8') as f:
        for line in f:
            i += 1
            if i > 3:
                if len(line)==1:
                    continue
                fp.write(line)
            else:
                continue
#对所有的歌词文件拼成一个文件，方便后续的处理
def all_lyric(folder_path):
    os.chdir(foler_path)
    print(foler_path)
    lyric_list = os.listdir(foler_path)  # 获取所有歌词文件的列表
    print(lyric_list)
    with open('all_lyric.txt','w',encoding='utf-8') as fp:
        for lyric in lyric_list:
            write_lyric(lyric,fp)



if __name__=='__main__':
    singer_id=input('please enter the songer id:')
    path = os.getcwd()
    f_path= path + '/' + 'lyric-ch4'
    creat_folder(f_path)
    lyric_path=f_path
    foler_path=f_path+'/'
    #singer_id=2116#eason
    start_url='http://music.163.com/artist?id={}'.format(singer_id)
    html=get_html(start_url)
    singer_infos=get_singer_info(html)
    #获取歌词，同时判断是否有歌词（纯音乐没有歌词），没有歌词会导致程序异常停止（没有歌词就没有必要获取歌词了）
    for singer_info in singer_infos:
        lyric=get_lyric(singer_info[1])
        if lyric==None:
            continue
        write_text(singer_info[0],lyric,foler_path)
    all_lyric(lyric_path)
    os.chdir(lyric_path)
    text = ''
    #将所有的歌词拼成一个字符串，方便后面进行分词
    with open('all_lyric.txt', 'r', encoding='utf-8')as f:
        for line in f:
            text += line
    words_ls = jieba.cut(text, cut_all=True)#利用jieba进行分词
    words_split = ' '.join(words_ls)
    wc = WordCloud(width=1980, height=1680)
    wc.font_path = "simhei.ttf"
    my_wordcloud = wc.generate(words_split)#生成词云
    plt.imshow(my_wordcloud)
    plt.axis("off")#关闭坐标轴
    plt.savefig('lyric')#save image
    plt.show()
    # print('end')









