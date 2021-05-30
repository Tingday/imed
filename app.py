# save this as app.py
import json

from flask import Flask, render_template

app = Flask(__name__)


class imed_questions:
    def __init__(self, filepath, title):
        self.filepath = filepath
        self.all_json = self.__all_to_json()
        self.totalSize = self.all_json['totalSize']
        self.result = self.all_json['result']
        self.title = title

    def questions(self):
        return self.all_json['questions']

    def __all_to_json(self):
        file_res = open(self.filepath, "r", encoding="utf-8")
        json_res = file_res.read()
        return json.loads(json_res)  # 直接返回题目json文件

    def get_questions(self, page, max_file=50, index=1):
        no = index + (page - 1) * max_file -1
        no_max = no + max_file
        q_res = self.questions()[no:no_max]
        return q_res


@app.route("/test")
def test():
    username = "林煜凡"
    bio = "这是林煜凡的自我介绍，但是什么都没有。"
    return render_template("test.html", bio=bio, username=username)


@app.route("/")
def imed_print():
    json_file = "G:\\projects\\PythonProjects\\imed_printer\\X.js"
    questions_res = imed_questions(json_file, "普外真题X型题")
    title = questions_res.title
    page = 3
    some_questions = questions_res.get_questions(page=page)  # page是页码 返回值是列表
    total = len(some_questions)
    return render_template("imed.html", questions=some_questions, title=title, total=total,page=page)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
