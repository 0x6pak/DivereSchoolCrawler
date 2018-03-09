import SQL
import json
'''
此程序把爬虫爬出来的json数据 储存到SQL里
'''

class DiverSQL():

    def __init__(self):
        self.Table = "DiverQuestions"
        self.TableValues = "(id int, Question text, answer text, bestAnswer text, image text,a text, b text, c text, d text,type int )"
        self.createSQL()

    def createSQL(self):

        if ezSQL.likeSQL(self.Table) == False:
            # print(False)
            ezSQL.createSQL(self.Table, self.TableValues)

    def textToSQL(self):
        questionsNum = 528
        for i in range(questionsNum):
            i += 1

            with open("DiverJSON/{id}/{id}.json".format(id=i), "r") as f:
                jsonText = f.read()

            with open("DiverJSON/{id}/answer.txt".format(id=i), "r") as f:
                answer = f.read()

            # try:
            #
            # except:
            #     pass
            jsonOBJ = json.loads(jsonText.replace("\\","\\\\"))
            id = jsonOBJ['id']
            question = jsonOBJ['question']
            a = jsonOBJ['a']
            b = jsonOBJ['b']
            c = jsonOBJ['c']
            d = jsonOBJ['d']
            type = jsonOBJ['Type']
            # imageUrl = jsonOBJ['imageurl']
            bestAnswer = jsonOBJ['bestanswer']
            sinaimg = jsonOBJ['sinaimg']
            if a == "":
                a = "NULL"

            if b == "":
                b = "NULL"

            if c == "":
                c = "NULL"

            if d == "":
                d = "NULL"

            if sinaimg == "":
                sinaimg = "NULL"
            else:
                sinaimg = "https://ww2.sinaimg.cn/mw600/{}".format(sinaimg)
            print(a, b, c, d,i)
            del jsonText
            del jsonOBJ

            # del a
            # del b
            # del c
            # del d
            # del sinaimg

            # print(id, question, a, b, c, d, type, sinaimg, bestAnswer, answer)

            ezSQL.insSQL(self.Table,'({id}, "{question}", "{answer}", "{bestAnswer}", "{sinaimg}", "{a}", "{b}", "{c}", "{d}" , {type})'.format(
                id = i, question = question, answer = answer, bestAnswer = bestAnswer, sinaimg = sinaimg, a = a , b = b, c = c, d = d, type = type
            ))





if __name__ == "__main__":
    ezSQL = SQL.ezSQL()
    DiverSQL = DiverSQL()
    DiverSQL.textToSQL()
