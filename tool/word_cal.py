# -*- coding: utf-8 -*-
import string

def add_words(word, words_dict):
    """把单词添加到words_dict字典里，并计数"""
    if word in words_dict:
        words_dict[word]+=1
    else:
        words_dict[word]=1

def process_line(line,words_dict):
    """处理文件每行数据"""
    line=line.strip()
    words_list=line.split()
    for word in words_list:
        word=word.lower().strip(string.punctuation)
        add_words(word,words_dict)

def print_result( words_dict ):
    """按格式输出words_dict中的数据"""
    val_key_list=[]
    for key,val in words_dict.items():
        if len(key)>3 and val>2:
            val_key_list.append((val,key))
    val_key_list.sort(reverse=True)
    print "%-10s %-10s" %("Word","  Count")
    print "_"*30
    for val,key in val_key_list:
        print "%-12s   %d" %(key,val)

def main():
    words_dict={}
    file_name = raw_input('Enter file:')
    handle = open(file_name, 'r')
    for line in handle:
        process_line(line,words_dict)
    if len(words_dict):
        print "The length of the article:",len(words_dict)
        print_result(words_dict)
    else:
        print "This file is None!"
main()