#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
import json
from flask import Flask, request
from web3 import Web3

w3 = Web3(Web3.HTTPProvider("http://foodchain-node1.etherhost.org:22001"))
f = open("food3.abi","r")
food3 = json.loads(f.read())
contract = w3.eth.contract(address='0xA4fafbE0ea4823e262b4916EF93CC5A6306A5DBc', abi=food3)

def uploadTweet(logno, loghash, logname, logorg, logdate):
    tx = contract.functions.FoodLog(8922153, "C-TEST-loghash", "C-TEST-logname", "C-TEST-logorg", "C-TEST-logdate") \
        .buildTransaction(
        {'gasPrice': 0, 'nonce': w3.eth.getTransactionCount('0x7CbEb723CA0788af6549110fb2a9816ED0BAa1a6')})
    print(tx)
    private_key = '0xab09158d9a817633c28c74b6e6c1bf34c26ffadc1a961870beaeef38b0753495'
    signed_txn = w3.eth.account.signTransaction(tx, private_key)
    res = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    print('res', res)

app = Flask(__name__, static_folder='./static', static_url_path="/")

# 账号Anne，密码AI@!Blockonomics
base_url = 'https://sm.ms/api/v2/'
token = 'xgj69AIyrnS8WaxPCBdujP10bmld9Yfb'

@app.route('/upload_image', methods=['POST'])
def upload_image():
    files = {'smfile': request.files.get('img_file')}
    headers = {'Authorization': token}
    res = requests.post(base_url + 'upload', files=files, headers=headers).json()

    if res['success']:
        return res['data']['url'], 200
    print(res)
    return 'upload failed', 400


@app.route('/')
def root():
    return app.send_static_file("tweet.html")


if __name__ == "__main__":
    app.run(debug=True)
