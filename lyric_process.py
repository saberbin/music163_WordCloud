#!/user/bin/Saberbin python
# -*- coding:utf-8 -*-
# Author:Saberbin

#creat a txt file ,name the 'all_lyric_eason'
import os

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

#主函数
if __name__=='__main__':
    path=os.getcwd()#获取当前文件夹（获取当前工作目录）
    lyric_file=path+'/'+'lyric-ch2'
    os.chdir(lyric_file)#将歌词文件夹定义为工作目录
    lyric_path=os.getcwd()#获取当前工作目录理论上lyric_path等于lyric_file，为了保险还是重新获取一下目录
    # print(lyric_path)
    lyric_list=os.listdir(lyric_path)#获取所有歌词文件的列表
    #print(lyric_list)
    with open('all_lyric.txt','w',encoding='utf-8') as fp:
        for lyric in lyric_list:
            write_lyric(lyric,fp)

    #print('end!!')








