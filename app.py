from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# 設定影片儲存資料夾
UPLOAD_FOLDER = 'uploads' #目錄
os.makedirs(UPLOAD_FOLDER, exist_ok=True) # exist_ok = true : 如果文件存在也不報錯
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/page3')
def page3():
    return render_template('page3.html')

@app.route('/final_page')
def final_page():
    return render_template('final_page.html')


@app.route('/analyze', methods=['POST'])
def analyze_video():#從前端抓取影片進行分析
    if 'video' not in request.files:
        return jsonify({'error': '沒有影片檔案'}), 400

    video = request.files['video'] #從前端收到的POST請求抓取video這個檔案欄位
    #用戶上傳的影片會被放在video這個變數
    if video.filename == '':
        return jsonify({'error': '未選擇檔案'}), 400

    filename = secure_filename(video.filename)
    video_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)#建立檔案的儲存路徑
    video.save(video_path)#實際儲存

    # 在這裡呼叫你的 AI 模型進行分析
    # 以下是模擬資料
    result = {
        "style": "鮮豔風格",
        "effect": "慢動作轉場",
        "music": "輕快背景音"
    }
    #以後可以寫成: result = your_model.analyze(video_path)

    # 可以選擇刪除檔案或暫存處理
    # os.remove(video_path)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
