from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/start-chat')
def start_chat():
    return render_template('start-chat.html')

@app.route('/call')
def call():
    return render_template('call.html')

@app.route('/video')
def video():
    return render_template('video.html')

@app.route('/video-call')
def video_call():
    return render_template('video-call.html')

@app.route('/find-user')
def find_user():
    return render_template('find-user.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)  # debug=False!