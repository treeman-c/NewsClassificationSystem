import json
import TrainText as tt
import NewsSpider as ns
from urllib import parse
from flask import Flask, Response, request, jsonify

app = Flask(__name__)


@app.route("/health")
def health():
    result = {'status': 'UP'}
    return Response(json.dumps(result), mimetype='application/json')


@app.route("/getUser")
def getUser():
    result = {'username': 'python', 'password': 'python'}
    return Response(json.dumps(result), mimetype='application/json')



##读网易新闻链接文本
@app.route("/python/urlToText", methods=['post'])
def urlToText():
    if not request.get_data():
        return "链接错误，请检查后重新输入（仅支持网易新闻）"
    map = parse.unquote(request.get_data()) #  获取restTemplate传送过来的参数并解码为文本
    list = map.split('=')[1:]
    print(map)
    url = list[0].replace('"','')
    print(url)
    try:
        text = ns.GetText(url)
    except Exception as e:
        text = "链接错误，请检查后重新输入（仅支持网易新闻）"
    print(text)
    return Response(json.dumps(text), mimetype='application/json')


##贝叶斯分类
@app.route("/python/bayes_text", methods=['post'])
def bayes_text_classify():
    if not request.get_data():
        return "链接错误，请检查后重新输入（仅支持网易新闻）"
    map = parse.unquote(request.get_data()) #  获取restTemplate传送过来的参数并解码为文本
    list = map.split('=')[1:]
    text  = list[0].replace('"','')
    # print("text = ", text)
    try:
        type = tt.testmodel(text)
    except Exception as e:
        type = ''
    result = type
    return Response(json.dumps(result), mimetype='application/json')


##svm分类
@app.route("/python/svm_text", methods=['post'])
def svm_text_classify():
    if not request.get_data():
        return "链接错误，请检查后重新输入（仅支持网易新闻）"
    map = parse.unquote(request.get_data()) #  获取restTemplate传送过来的参数并解码为文本
    list = map.split('=')[1:]
    text  = list[0].replace('"','')
    try:
        type = tt.test_svm_model(text)
    except Exception as e:
        type = ''
    result = type
    return Response(json.dumps(result), mimetype='application/json')


##knn分类
@app.route("/python/knn_text", methods=['post'])
def knn_text_classify():
    if not request.get_data():
        return "链接错误，请检查后重新输入（仅支持网易新闻）"
    map = parse.unquote(request.get_data()) #  获取restTemplate传送过来的参数并解码为文本
    list = map.split('=')[1:]
    text  = list[0].replace('"','')
    try:
        type = tt.test_knn_model(text)
    except Exception as e:
        type = ''
    result = type
    return Response(json.dumps(result), mimetype='application/json')


##分类bp
@app.route("/python/bp_text", methods=['post'])
def bp_text_classify():
    if not request.get_data():
        return "链接错误，请检查后重新输入（仅支持网易新闻）"
    map = parse.unquote(request.get_data()) #  获取restTemplate传送过来的参数并解码为文本
    list = map.split('=')[1:]
    text  = list[0].replace('"','')
    try:
        type = tt.test_bp_model(text)
    except Exception as e:
        type = ''
    result = type
    return Response(json.dumps(result), mimetype='application/json')


@app.route("/python/intelligent_type", methods=['post'])
def intelligent_text_classify():
    if not request.get_data():
        return "链接错误，请检查后重新输入（仅支持网易新闻）"
    map = parse.unquote(request.get_data()) #  获取restTemplate传送过来的参数并解码为文本
    list = map.split('=')[1:]
    text  = list[0].replace('"','')
    try:
        type = tt.intelligent_classification(text)
    except Exception as e:
        type = ''
    result = type
    return Response(json.dumps(result), mimetype='application/json')


@app.route("/python/get_ch_data", methods=['get'])
def get_ch_data():
    result = tt.get_ch_data()
    return Response(json.dumps(result), mimetype='application/json')


@app.route("/python/train_model", methods=['get'])
def train_model():
    tt.get_chart()


if __name__ == '__main__':
    app.run(port=3000, host='0.0.0.0')
