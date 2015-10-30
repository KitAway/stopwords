'''
Created on Oct 27, 2015

@author: d038395
'''
def main():
    strList=list()
    inputfile=r'C:\Users\d038395\Desktop\stop-words_chinese_1_zh.txt'
    print('[',end='')
    with open(inputfile,'r',encoding='utf-8') as f:
        for line in f:
            s=line[0:-1].encode('unicode-escape').decode('unicode-escape')
            print(s)
    print("]")
if __name__ == '__main__':
    main()