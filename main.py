import requests
from flask import Flask, request

app = Flask(__name__, static_folder='./static', static_url_path="/")

# 账号Anne，密码AI@!Blockonomics
base_url = 'https://sm.ms/api/v2/'
token = 'xgj69AIyrnS8WaxPCBdujP10bmld9Yfb'


@app.route('/upload_image', methods=['POST'])
def upload_image():
    files = {'smfile': request.files.get('imgup')}
    headers = {'Authorization': token}
    res = requests.post(base_url + 'upload', files=files, headers=headers).json()

    if res['success']:
        return res['data']['url']
    return 'upload failed'


@app.route('/')
def root():
    return app.send_static_file("tweet.html")


if __name__ == "__main__":
    app.run(debug=True)
