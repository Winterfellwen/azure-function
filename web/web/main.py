from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        
        # 在这里添加连接到 Azure 的代码
        if connect_azure(user, password):
            return redirect('/success')
        else:
            error = '连接失败，请确认用户名和密码是否正确。'
            return render_template('login.html', error=error)

    return render_template('login.html')

@app.route('/success')
def success():
    return '成功连接到 Azure！'

def connect_azure(user, password):
    # 在这里编写连接到 Azure 的逻辑
    # 如果连接成功，返回 True，否则返回 False
    return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute():
    script_path = './powershell_script.ps1'  # 替换为你的 PowerShell 脚本路径
    result = subprocess.check_output(['pwsh', script_path]).decode('utf-8')
    return result

if __name__ == '__main__':
    app.run()
