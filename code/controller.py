from flask import Flask, request
import videoprocess as vp
import trainingsetprocess as tp
import videocapture as vc

app = Flask(__name__)


@app.route('/upload/pushdown', methods=['POST'])
def push_up_upload():
    video_path = request.files.get('video_path')
    flag = 1
    tp.trainset_process(flag)
    vp.video_process(video_path, flag)

@app.route('/camera/pushdown', methods=['POST'])
def push_up_camera():
    flag = 1
    tp.trainset_process(flag)
    vc.process(flag)


@app.route('/upload/squatdown', methods=['POST'])
def squat_down_upload():
    video_path = request.files.get('video_path')
    flag = 2
    tp.trainset_process(flag)
    vp.video_process(video_path, flag)


@app.route('/camera/squatdown', methods=['POST'])
def squat_down_camera():
    flag = 2
    tp.trainset_process(flag)
    vc.process(flag)


@app.route('/upload/pushup', methods=['POST'])
def pull_down_upload():
    video_path = request.files.get('video_path')
    flag = 3
    tp.trainset_process(flag)
    vp.video_process(video_path, flag)


@app.route('/camera/pushup', methods=['POST'])
def pull_down_camera():
    flag = 3
    tp.trainset_process(flag)
    vc.process(flag)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

