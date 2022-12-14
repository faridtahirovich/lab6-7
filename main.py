#from flask import Flask, request, jsonify, render_template

#app = Flask(__name__)

#@app.route("/",methods=['GET'])
#def root():
    #return "<h1>Ответ на запрос GET</h1>"

#@app.route("/user",methods=['GET'])
#def user():
    #name = "Маша"
    #marks = [5,5,5,5,5,5]
    #return render_template('user.html',name = name,marks = marks)

#if __name__ == "main":
#    app.run(debug==True)
from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

studs = [
    { "name" : "Анна",
      "marks": [1,2,3,4,5],
      "group": "ИБМ7-18б"
    },
    { "name" : "Макс",
      "marks": [4,4,5,5,5,4],
      "group": "ИБМ7-22"
    },
    { "name" : "Володя",
      "marks": [3,4,3,4,3,5],
      "group": "ИБМ7-22"
    }
]

@app.route("/",methods=['GET'])
def root():
    a = json.loads('{"name":"ivan","hp":100}')
    print(a.keys())
    print(a['hp'])
    print(type(a))
    return "<h1>Ответ на запрос GET</h1>"

@app.route("/user",methods=['GET'])
def user():
    name = "Студент"
    marks = [5,4,3,4,5,5]
    return render_template('user.html',name = name,marks = marks)

@app.route("/student/<stud_name>/",methods=['GET'])
def student(stud_name):
    print("============================")
    for student in studs:
        if student["name"] == stud_name:
            print("Нашли", stud_name)
            return render_template("user.html",
                name = student["name"],
                group = student["group"],
                marks = student["marks"])
    print("============================")
    return "Никого не нашли с таким именем"

@app.route("/summ1/<x>/<y>",methods=['GET'])
def summ1(x,y):
    print("============================")
    x = int(x)
    y = int(y)
    return "Считаем сумму <br>" + str(x+y)


@app.route("/summ2",methods=['GET'])
def summ2():
    print("============================")
    print(request.args)
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))
    return "Считаем сумму <br>" + str(x+y)


@app.route("/student_create",methods=['GET'])
def student_create():
    if request.method == 'POST':
        new_std = request.get_json()
        print("Получили запрос пост")
        print(new_std)
        return render_template('student_create.html')
    if request.method == 'GET':
        print("Запрос GET")
        return render_template('student_create.html')