# 点赞
from flask import Flask, render_template, request

app = Flask(__name__)

# 点赞功能
datas = [
    {'id': 0, 'name': '中秋节', 'num': 0},
    {'id': 1, 'name': '元旦节', 'num': 0},
    {'id': 2, 'name': '春节', 'num': 0},
]


@app.route('/like')
def like():
    return render_template('like.html', data=datas)


@app.route('/dz')
def dz():
    id = request.args.get('id')
    print(f"想要点赞的节日id为{id}")
    datas[int(id)]['num'] += 1
    return render_template('like.html', data=datas)


if __name__ == '__main__':
    app.run(debug=True)
