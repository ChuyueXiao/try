import requests
res=requests.get('https://www.shanbay.com/api/v1/vocabtest/category/')
info=res.json()
print('1.GMAT 2.考研 3.高考 4.四级 5.六级 6.英专 7.托福 8.GRE 9.雅思 10.任意')
test=int(input('请输入你选择的词库编号，按Enter确认: '))
words =info['data'][test-1][0]
#利用用户输入的数字编号，获取题库的代码。
# 如果以输入“高考”的编号“3”为例，那么ciku的值就是，在字典js_link中查找data的值，
# data是一个list，查找它的第bianhao-1，也就是第2个元素（高考），得到的依然是一个list，
# 再查找该list的第0个元素。最后得到的就是我们想要的 NCEE（URL中控制'高考'变量的内容）。

print(info)

# 请求（获取）用于测试的50个单词。
test_ = requests.get('https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category='+words)
# 对响应test进行解析。
word = test_.json()
# 新增一个list，用于统计用户认识的单词 只包括单词本身 因为元素本身信息太多
danci = []
# 创建一个空的列表，用于记录用户认识的单词 包括网页中和此单词相关的所有内容 （选项 rank值等等）
words_knows = []
# 创建一个空的列表，用于记录用户不认识的单词。
not_knows = []

n=0
for x in word['data']:
    n=n+1
    # 加一个\n，用于换行。
    print("\n第"+str(n)+'个：'+x['content'])
    answer = input('认识请敲Y，否则敲Enter：')
    if answer == 'Y':
        # 把用户认识的单词，追加进danci这个list。
        danci.append(x['content'])
        words_knows.append(x)
    else:
        not_knows.append(x)

print('\n在上述'+str(len(word['data']))+'个单词当中，有'+str(len(danci))+'个是你觉得自己认识的，它们是：')
print(danci)

print('现在我们来检测一下，你有没有真正掌握它们：')
wrong_words = []
right_num = 0
for y in words_knows:
    # 选择单词意思 不再用rank值
    print('\n\n'+'A:'+y['definition_choices'][0]['definition'])
    print('B:'+y['definition_choices'][1]['definition'])
    print('C:'+y['definition_choices'][2]['definition'])
    print('D:'+y['definition_choices'][3]['definition'])
    xuanze = input('请选择单词\"'+y['content']+'\"的正确翻译：')
    # 我们创建一个字典，搭建起A、B、C、D和四个rank值的映射关系。
    dic = {'A':y['definition_choices'][0]['rank'],'B':y['definition_choices'][1]['rank'],'C':y['definition_choices'][2]['rank'],'D':y['definition_choices'][3]['rank']}
    # 此时dic[xuanze]的内容，其实就是rank值，此时的代码含义已经和之前的版本相同了。
    if dic[xuanze] == y['rank']:
        right_num += 1
    else:
        wrong_words.append(y)
#print(wrong_words)
print('现在，到了公布成绩的时刻:')
# 以下是句蛮复杂的话，对照前面的代码和json文件你才能理解它。
print('在'+str(len(word['data']))+'个'+info['data'][test-1][1]+'词汇当中，你认识其中'+str(len(danci))+'个，实际掌握'+str(right_num)+'个，错误'+str(len(wrong_words))+'个。')

# 询问用户，是否要打印并保存错题集。
save = input('是否打印并保存你的错词集？填入Y或N： ')
# 如果用户说是：
if save == 'Y':
    # 在当前目录下，创建一个错题集.txt的文档。
    f = open('错题集.txt', 'a+')
    print('你记错的单词有：')
    # 写入"你记错的单词有：\n"
    f.write('你记错的单词有：\n')

    # 启动一个循环，循环的次数等于，用户的错词数：
    m=0  # 单词个数记录
    for z in wrong_words:
        m = m+1
        # 打印每一个错词。
        print(z['content'])
        f.write(str(m) +'. '+ z['content']+'\n')
        # 写入序号，写入错词。
    print('你不认识的单词有：')
    f.write('你没记住的单词有：\n')
    s=0
    for x in not_knows:
    # 启动一个循环，循环的次数等于，用户不认识的单词数。
        s=s+1
        print(x['content'])
        # 打印每一个不认识的单词。
        f.write(str(s) +'. '+ x['content']+'\n')
        # 写入序号，写入用户不认识的词汇。
    print('错词和没记住的词已保存至当前文件目录下，下次见！')

# 如果用户不想保存：
else:
    # 输出“下次见！”
    print('下次见！')