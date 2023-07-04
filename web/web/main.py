from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute():
    script_path = './powershell_script.ps1'  # 替换为你的 PowerShell 脚本路径
    result = subprocess.check_output(['powershell', '-File', script_path]).decode('utf-8')
    return result

if __name__ == '__main__':
    app.run()
