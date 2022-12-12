from flask import Flask, request
import videoprocess as vp
import trainingsetprocess as tp
import videocapture as vc

app = Flask(__name__)


@app.route('/upload/pushup', methods=['POST'])
def push_down_upload():
    video_path = request.files.get('video_path')
    flag = 3
    tp.trainset_process(flag)
    vp.video_process(video_path, flag)


@app.route('/camera/pushup', methods=['POST'])
def push_down_upload():
    flag = 3
    tp.trainset_process(flag)
    vc.process(flag)