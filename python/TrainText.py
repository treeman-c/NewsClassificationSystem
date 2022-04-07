import os.path
import re
import jieba
import joblib
import pandas as pd
from sklearn import svm
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsRestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier as knn
from sklearn import neural_network

import NewsSpider as ns
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer  # TF-IDF向量转换类


def TrainModel(dt):
    dt = ns.DelStopword(dt)
    type = dt['文本类别']
    keyword = dt['keyword']
    count = CountVectorizer()
    x, x_test, y, y_test = train_test_split(keyword, type, test_size=0.2, random_state=0)
    x = count.fit_transform(x)
    tfidf_transformer = TfidfTransformer()
    x = tfidf_transformer.fit_transform(x)
    model = MultinomialNB().fit(x, y)
    if not os.path.exists('./model'):
        os.mkdir('./model')
    if not os.path.exists('./model/newsmodel.pkl'):
        f = open('./model/newsmodel.pkl', 'wb')
        f.close()
    if not os.path.exists('./model/vocab.pkl'):
        f = open('./model/vocab.pkl', 'wb')
        f.close()
    joblib.dump(model, './model/newsmodel.pkl')
    joblib.dump(count.vocabulary_, 'model/vocab.pkl')
    print("分类准确率:", accuracy_score(y_test, model.predict(count.transform(x_test))) * 100)
    print("分类评估报告如下:\n")
    print(classification_report(y_test, model.predict(count.transform(x_test))))
    return classification_report(y_test, model.predict(count.transform(x_test)))


# 测试文本
def testmodel(text):
    delOrther = re.compile(r"[^a-zA-Z0-9\u4E00-\u9FA5]")
    text = delOrther.sub('', text)  # 去除非汉字字母数字的符号
    stopworlds = ns.GetStopword()
    text = " ".join([w for w in list(jieba.cut(text)) if w not in stopworlds])
    if not os.path.exists('./model'):
        os.mkdir('./model')
    if not os.path.exists('./model/newsmodel.pkl'):
        f = open('./model/newsmodel.pkl', 'wb')
        f.close()
    model = joblib.load('./model/newsmodel.pkl')
    vob = joblib.load('./model/vocab.pkl')
    count = CountVectorizer(ngram_range=(1, 4), min_df=1, vocabulary=vob)
    count._validate_vocabulary()
    text = [text]
    print(model.predict(count.transform(text))[0])
    return model.predict(count.transform(text))[0]


##svm支持向量机相关代码##
def train_svm_model(dt):
    dt = ns.DelStopword(dt)
    type = dt['文本类别']
    keyword = dt['keyword']
    count = CountVectorizer()
    x, x_test, y, y_test = train_test_split(keyword, type, test_size=0.2, random_state=0)
    x = count.fit_transform(x)
    tfidf_transformer = TfidfTransformer()
    x = tfidf_transformer.fit_transform(x)
    constructor = OneVsRestClassifier(svm.SVC(kernel='linear', probability=True, random_state=0))
    model = constructor.fit(x, y)
    if not os.path.exists('./model'):
        os.mkdir('./model')
    if not os.path.exists('./model/svm_model.pkl'):
        f = open('./model/svm_model.pkl', 'wb')
        f.close()
    if not os.path.exists('./model/svm_vocab.pkl'):
        f = open('./model/svm_vocab.pkl', 'wb')
        f.close()
    joblib.dump(model, './model/svm_model.pkl')
    joblib.dump(count.vocabulary_, 'model/svm_vocab.pkl')
    print("分类准确率:", accuracy_score(y_test, model.predict(count.transform(x_test))) * 100)
    print("分类评估报告如下:\n")
    print(classification_report(y_test, model.predict(count.transform(x_test))))
    return classification_report(y_test, model.predict(count.transform(x_test)))


def test_svm_model(text):
    delOrther = re.compile(r"[^a-zA-Z0-9\u4E00-\u9FA5]")
    text = delOrther.sub('', text)  # 去除非汉字字母数字的符号
    stopworlds = ns.GetStopword()
    text = " ".join([w for w in list(jieba.cut(text)) if w not in stopworlds])
    if not os.path.exists('./model'):
        os.mkdir('./model')
    if not os.path.exists('./model/svm_model.pkl'):
        f = open('./model/svm_model.pkl', 'wb')
        f.close()
    model = joblib.load('./model/svm_model.pkl')
    vob = joblib.load('./model/svm_vocab.pkl')
    count = CountVectorizer(ngram_range=(1, 4), min_df=1, vocabulary=vob)
    count._validate_vocabulary()
    text = [text]
    print(model.predict(count.transform(text))[0])
    return model.predict(count.transform(text))[0]


##k最近邻knn相关代码##
def train_knn_model(dt):
    dt = ns.DelStopword(dt)
    type = dt['文本类别']
    keyword = dt['keyword']
    count = CountVectorizer()
    x, x_test, y, y_test = train_test_split(keyword, type, test_size=0.2, random_state=0)
    x = count.fit_transform(x)
    tfidf_transformer = TfidfTransformer()
    x = tfidf_transformer.fit_transform(x)
    constructor = knn(n_neighbors=5, weights="distance", algorithm="auto", n_jobs=1)
    model = constructor.fit(x, y)
    if not os.path.exists('./model'):
        os.mkdir('./model')
    if not os.path.exists('./model/knn_model.pkl'):
        f = open('./model/knn_model.pkl', 'wb')
        f.close()
    if not os.path.exists('./model/knn_vocab.pkl'):
        f = open('./model/knn_vocab.pkl', 'wb')
        f.close()
    joblib.dump(model, './model/knn_model.pkl')
    joblib.dump(count.vocabulary_, 'model/knn_vocab.pkl')
    print("分类准确率:", accuracy_score(y_test, model.predict(count.transform(x_test))) * 100)
    print("分类评估报告如下:\n")
    print(classification_report(y_test, model.predict(count.transform(x_test))))
    return classification_report(y_test, model.predict(count.transform(x_test)))


def test_knn_model(text):
    delOrther = re.compile(r"[^a-zA-Z0-9\u4E00-\u9FA5]")
    text = delOrther.sub('', text)  # 去除非汉字字母数字的符号
    stopworlds = ns.GetStopword()
    text = " ".join([w for w in list(jieba.cut(text)) if w not in stopworlds])
    if not os.path.exists('./model'):
        os.mkdir('./model')
    if not os.path.exists('./model/knn_model.pkl'):
        f = open('./model/knn_model.pkl', 'wb')
        f.close()
    model = joblib.load('./model/knn_model.pkl')
    vob = joblib.load('./model/knn_vocab.pkl')
    count = CountVectorizer(ngram_range=(1, 4), min_df=1, vocabulary=vob)
    count._validate_vocabulary()
    text = [text]
    print(model.predict(count.transform(text))[0])
    return model.predict(count.transform(text))[0]


#########神经网络训练模型###########
def train_bp_model(dt):
    dt = ns.DelStopword(dt)
    type = dt['文本类别']
    keyword = dt['keyword']
    count = CountVectorizer()
    x, x_test, y, y_test = train_test_split(keyword, type, test_size=0.2, random_state=0)
    x = count.fit_transform(x)
    tfidf_transformer = TfidfTransformer()
    x = tfidf_transformer.fit_transform(x)
    model = neural_network.MLPClassifier(
        hidden_layer_sizes=5,
        activation="relu",
        solver="adam",
        alpha=0.0001,
        batch_size="auto",
        learning_rate="constant",
        learning_rate_init=0.001,
        power_t=0.5,
        max_iter=250,
        tol=1e-4
    )
    model.fit(x, y)
    if not os.path.exists('./model'):
        os.mkdir('./model')
    if not os.path.exists('./model/bp_model.pkl'):
        f = open('./model/bp_model.pkl', 'wb')
        f.close()
    if not os.path.exists('./model/bp_vocab.pkl'):
        f = open('./model/bp_vocab.pkl', 'wb')
        f.close()
    joblib.dump(model, './model/bp_model.pkl')
    joblib.dump(count.vocabulary_, 'model/bp_vocab.pkl')
    print("分类准确率:", accuracy_score(y_test, model.predict(count.transform(x_test))) * 100)
    print("分类评估报告如下:\n")
    print(classification_report(y_test, model.predict(count.transform(x_test))))
    return classification_report(y_test, model.predict(count.transform(x_test)))


def test_bp_model(text):
    delOrther = re.compile(r"[^a-zA-Z0-9\u4E00-\u9FA5]")
    text = delOrther.sub('', text)  # 去除非汉字字母数字的符号
    stopworlds = ns.GetStopword()
    text = " ".join([w for w in list(jieba.cut(text)) if w not in stopworlds])
    if not os.path.exists('./model'):
        os.mkdir('./model')
    if not os.path.exists('./model/bp_model.pkl'):
        f = open('./model/bp_model.pkl', 'wb')
        f.close()
    model = joblib.load('./model/bp_model.pkl')
    vob = joblib.load('./model/bp_vocab.pkl')
    count = CountVectorizer(ngram_range=(1, 4), min_df=1, vocabulary=vob)
    count._validate_vocabulary()
    text = [text]
    print(model.predict(count.transform(text))[0])
    return model.predict(count.transform(text))[0]


def intelligent_classification(text):
    """
    智能预测
    使用现有的所有训练模型，进行预测
    参数：待预测文本数据
    过程：使用现有预测模型，对文本数据进行预测，返回预测结果最多的一个结果
    返回：预测结果 字符串
    """
    dict = {'军事': 0, '体育': 0, '航空': 0, '政治': 0, '国际': 0}
    type = testmodel(text)  # bayes模型
    dict[type] = dict.get(type) + 1
    type = test_svm_model(text)  # 支持向量机模型
    dict[type] = dict.get(type) + 1
    type = test_knn_model(text)  # k最近邻模型
    dict[type] = dict.get(type) + 1
    type = test_bp_model(text)  # bp神经网络模型
    dict[type] = dict.get(type) + 1
    rel_type = type
    rel_max = dict[type]
    for type in dict.keys():
        if rel_max < dict.get(type):
            rel_type = type
            rel_max = dict.get(type)
    # print("最大概率为：", rel_max, "类型为:", rel_type)
    return rel_type


def get_chart():
    """
    获取训练数据
    返回某一个训练器的训练数据，就是准确率和召回率以及f1得分的数据
    """
    ns.GetData()
    dt = pd.read_csv('newdata.csv', encoding='utf-8', engine='python')
    precisionlist = []
    recalllist = []
    f1list = []
    data = getscore(TrainModel(dt), 'bayes')  # bayes
    precisionlist.append(data[0])
    recalllist.append(data[1])
    f1list.append(data[2])
    data = getscore(train_svm_model(dt), 'svm')  # svm
    precisionlist.append(data[0])
    recalllist.append(data[1])
    f1list.append(data[2])
    data = getscore(train_knn_model(dt), 'knn')  # knn
    precisionlist.append(data[0])
    recalllist.append(data[1])
    f1list.append(data[2])
    data = getscore(train_bp_model(dt), 'bp')  # bp
    precisionlist.append(data[0])
    recalllist.append(data[1])
    f1list.append(data[2])
    index = ['1', '2', '3', '4']
    columns = ['分类器', '体育', '军事', '国际', '政治', '航空']
    pre = pd.DataFrame(precisionlist, index=index, columns=columns)
    rel = pd.DataFrame(recalllist, index=index, columns=columns)
    f1 = pd.DataFrame(f1list, index=index, columns=columns)
    if os.path.exists('./precision.csv'):
        os.remove('./precision.csv')
    pre.to_csv('./precision.csv', encoding='utf-8-sig')
    if os.path.exists('./recall.csv'):
        os.remove('./recall.csv')
    rel.to_csv('./recall.csv', encoding='utf-8-sig')
    if os.path.exists('./f1.csv'):
        os.remove('./f1.csv')
    f1.to_csv('./f1.csv', encoding='utf-8-sig')


def getscore(score, str):
    list = score.split(' ')
    lists = []
    for item in list:
        if item != '':
            lists.append(item)
    list = []
    for num in range(1, 4):
        list1 = []
        num -= 1
        list1 = []
        list1.append(str)
        for item in range(1, 6):
            num = num + 5
            s = lists[num].replace('\n', '')
            list1.append(float(s))
        list.append(list1)
    # print(lists)
    # print(list)
    return list


def get_ch_data():
    """
    提供给网页对应的数据
    """
    map = {}
    pre = pd.read_csv('./precision.csv')
    temp = pre.T.axes[0]
    lt = []
    for item in pre.T.values:
        lt.append(list(item))
    map['pre'] = [list(temp)[1:],lt[1:]]
    pre = pd.read_csv('./recall.csv')
    temp = pre.T.axes[0]
    lt = []
    for item in pre.T.values:
        lt.append(list(item))
    map['rel'] = [list(temp)[1:], lt[1:]]
    pre = pd.read_csv('./f1.csv')
    temp = pre.T.axes[0]
    lt = []
    for item in pre.T.values:
        lt.append(list(item))
    map['f1'] = [list(temp)[1:], lt[1:]]
    return map


if __name__ == '__main__':
    get_ch_data()
