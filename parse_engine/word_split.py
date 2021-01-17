import jieba
import os
import jieba.analyse


# 创建停用词list
def stopwords_list():
    filePath = '../data/stop_words/user_define_stop_words.txt'
    stopwords = [line.strip() for line in open(filePath, 'r', encoding='utf-8').readlines()]
    return stopwords

def load_dict():
    filePath = '../data/dictionary'
    paths = os.listdir(filePath)
    # 加载词库
    for path in paths:
        if (path.endswith('.txt')):
            print(filePath + '/' + path)
            jieba.load_userdict(filePath + '/' + path)

def load_doc(filePath):
    with open(filePath, errors='ignore', encoding='utf-8') as fp:
        return fp.readlines()


# 对句子进行分词
def seg_sentence(sentence, stopwords):
    sentence_seged = jieba.cut(sentence.strip(), use_paddle=True)
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr


def split():
    load_dict()
    stopwords = stopwords_list()
    lines = load_doc("../data/novels/天龙八部.txt")
    for line in lines:
        segments = seg_sentence(line, stopwords)
        yield segments


if __name__ == '__main__':
    segments = split()
    for segment in segments:
        print(segment)




