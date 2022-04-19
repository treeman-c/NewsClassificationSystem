import tkinter as tk
import NewsSpider as ns
import TrainText as tt

#####################################


def urlm1():
    url = t_url.get('0.0', 'end')
    t_text.delete('1.0', 'end')
    try:
        temp = ns.GetText(url)
    except Exception as e:
        t_text.insert('end', '链接错误，请检查')
        return
    t_text.insert('end', temp)
    str_rstx.set(tt.testmodel(temp))


def textm1():
    text = t_text.get('0.0', 'end')
    try:
        classify = tt.testmodel(text)
    except Exception as e:
        str = '分类出现错误' + e.__str__()
        t_text.insert('end', str)
        return
    str_rstx.set(classify)


##svm支持向量机###
def url_svm_m1():
    url = t_url.get('0.0', 'end')
    t_text.delete('1.0', 'end')
    try:
        temp = ns.GetText(url)
    except Exception as e:
        t_text.insert('end', '链接错误，请检查')
        return
    t_text.insert('end', temp)
    str_rstx.set(tt.test_svm_model(temp))


def text_svm_m1():
    text = t_text.get('0.0', 'end')
    try:
        classify = tt.test_svm_model(text)
    except Exception as e:
        str = '分类出现错误' + e.__str__()
        t_text.insert('end', str)
        return
    str_rstx.set(classify)


##knn分类###
def url_knn_m1():
    url = t_url.get('0.0', 'end')
    t_text.delete('1.0', 'end')
    try:
        temp = ns.GetText(url)
    except Exception as e:
        t_text.insert('end', '链接错误，请检查')
        return
    t_text.insert('end', temp)
    str_rstx.set(tt.test_knn_model(temp))


def text_knn_m1():
    text = t_text.get('0.0', 'end')
    try:
        classify = tt.test_knn_model(text)
    except Exception as e:
        str = '分类出现错误' + e.__str__()
        t_text.insert('end', str)
        return
    str_rstx.set(classify)


##bp神经网络分类###
def url_bp_m1():
    url = t_url.get('0.0', 'end')
    t_text.delete('1.0', 'end')
    try:
        temp = ns.GetText(url)
    except Exception as e:
        t_text.insert('end', '链接错误，请检查')
        return
    t_text.insert('end', temp)
    str_rstx.set(tt.test_bp_model(temp))


def text_bp_m1():
    text = t_text.get('0.0', 'end')
    try:
        classify = tt.test_bp_model(text)
    except Exception as e:
        str = '分类出现错误' + e.__str__()
        t_text.insert('end', str)
        return
    str_rstx.set(classify)


##重置分类结果##
def norm(event):
    str_rstx.set('未执行')


#####################################


# 将tkinter 对象实例化
win = tk.Tk()
# 设置窗口标题
win.title('文本分类器')
# 设置窗口大小
win.geometry('700x400')
# 进入消息循环（检测到事件，就刷新组件）
# 定义一个label
l_url = tk.Label(win,
                 text='URL',
                 bg='white',
                 font=('Arial', 12),
                 width=5, height=1
                 )
l_url.place(x=10, y=10, anchor='nw')
turl = tk.StringVar()
turl.set('输入链接')
t_url = tk.Text(win, width=30, height=2)
t_url.bind('<Button-1>', norm)
t_url.place(x=20, y=50, anchor='nw')
b_url = tk.Button(win, text='URL_Bayes_分类', width=15, height=1, command=urlm1)
b_url.place(x=20, y=100, anchor='nw')
l_text = tk.Label(win,
                  text='文本',
                  bg='white',
                  font=('Arial', 12),
                  width=5, height=1
                  )
l_text.place(x=300, y=10, anchor='nw')
t_text = tk.Text(win, width=50, height=25)
t_text.bind('<B1-Motion>', norm)
t_text.place(x=300, y=50, anchor='nw')
b_text = tk.Button(win, text='文本_Bayes_分类', width=15, height=1, command=textm1)
b_text.place(x=150, y=100, anchor='nw')
l_result = tk.Label(win,
                    text='分类结果 ：',
                    bg='white',
                    font=('Arial', 12),
                    width=10, height=1
                    )
l_result.place(x=30, y=350, anchor='nw')
str_rstx = tk.StringVar()
str_rstx.set('未执行')
l_rstx = tk.Label(win,
                  textvariable=str_rstx,
                  bg='white',
                  font=('Arial', 12),
                  width=5, height=1
                  )
l_rstx.place(x=120, y=350, anchor='nw')

# svm按钮
b_url_svm = tk.Button(win, text='URL_svm_分类', width=15, height=1, command=url_svm_m1)
b_url_svm.place(x=20, y=150, anchor='nw')
b_text_svm = tk.Button(win, text='文本_svm_分类', width=15, height=1, command=text_svm_m1)
b_text_svm.place(x=150, y=150, anchor='nw')
# knn按钮
b_url_knn = tk.Button(win, text='URL_knn_分类', width=15, height=1, command=url_knn_m1)
b_url_knn.place(x=20, y=200, anchor='nw')
b_text_knn = tk.Button(win, text='文本_knn_分类', width=15, height=1, command=text_knn_m1)
b_text_knn.place(x=150, y=200, anchor='nw')
# bp神经网络
b_url_bp = tk.Button(win, text='URL_bp_分类', width=15, height=1, command=url_bp_m1)
b_url_bp.place(x=20, y=250, anchor='nw')
b_text_bp = tk.Button(win, text='文本_bp_分类', width=15, height=1, command=text_bp_m1)
b_text_bp.place(x=150, y=250, anchor='nw')
# 智能预测
b_text_it = tk.Button(win, text='智能分类', width=15, height=1, command=text_bp_m1)
b_text_it.place(x=85, y=300, anchor='nw')

win.mainloop()
