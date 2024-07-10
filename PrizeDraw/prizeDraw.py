"""
抽奖 点赞
让我们的电脑可以支持服务访问
需要一个web框架
pip install Flask
"""
# 从 Flask 模块中导入 Flask 类和 render_template 函数
from flask import Flask, render_template
# 从 random 模块中导入 randint 函数，用于生成随机整数
from random import randint

# 创建一个 Flask 应用实例
# __name__ 是一个特殊的变量，表示当前 Python 模块的名称
# 在这里，将当前模块的名称传递给 Flask 应用实例
# Flask 使用这个参数来决定应用的根目录，从而可以方便地找到应用的资源文件，例如模板和静态文件
app = Flask(__name__)

# 定义一个包含英雄名称的列表
heroes = [
    "黑暗之女",
    "狂战士",
    "正义巨像",
    "卡牌大师",
    "德邦总管",
    "无畏战车",
    "诡术妖姬",
    "猩红收割者",
    "远古恐惧",
    "正义天使",
    "无极剑圣"
]


# 定义一个路由和视图函数
# @app.route('/index') 是一个装饰器，用于将 URL 路径 '/index' 绑定到以下的视图函数 index
@app.route('/index')
def index():
    # render_template 函数用于渲染模板，并将数据传递给模板
    # 这里将英雄列表传递给模板 'index.html'
    return render_template('index.html', hero=heroes)


# 定义另一个路由和视图函数
# @app.route('/draw') 是一个装饰器，用于将 URL 路径 '/draw' 绑定到以下的视图函数 draw
@app.route('/draw')
def draw():
    # 使用 randint 函数生成一个随机整数，范围从 0 到英雄列表的长度减 1
    num = randint(0, len(heroes) - 1)
    # render_template 函数用于渲染模板，并将数据传递给模板
    # 这里将英雄列表和随机选中的英雄传递给模板 'index.html'
    return render_template('index.html', hero=heroes, h=heroes[num])




# 运行 Flask 应用
# app.run() 启动 Flask 开发服务器并开始监听传入的请求
# debug=True 启用了调试模式，这样在代码更改时服务器会自动重新启动，并提供详细的错误信息
if __name__ == '__main__':
    app.run(debug=True)
