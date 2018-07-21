from pydub import AudioSegment
import uuid
import base64
import json
import requests
#将MP3格式先转成wav格式然后接到百度语音的接口识别文字返回

def return_vedio():
    sound = AudioSegment.from_mp3("1.mp3")
    sound.export("1.wav", format="wav")
    def get_token():
        url = "https://openapi.baidu.com/oauth/2.0/token"
        API_KEY = "lbGZzpOjbOmp845ITWUN8WeB"
        SECRET_KEY = "2d98dbac0f297e9406a14d9d0ddf168e"
        grant_type = "client_credentials"
        data = {'grant_type': grant_type, 'client_id': API_KEY, 'client_secret': SECRET_KEY}
        r = requests.post(url, data=data)
        token = json.loads(r.text).get("access_token")
        return token
    def recognize(sig, rate, token):
        url = "http://vop.baidu.com/server_api"
        speech_length = len(sig)
        speech = base64.b64encode(sig).decode("utf-8")
        mac_address = uuid.UUID(int=uuid.getnode()).hex[-12:]
        rate = rate
        data = {
            "format": "wav",
            "lan": "zh",
            "token": token,
            "len": speech_length,
            "rate": rate,
            "speech": speech,
            "cuid": mac_address,
            "channel": 1,
        }
        data_length = len(json.dumps(data).encode("utf-8"))
        headers = {"Content-Type": "application/json",
                   "Content-Length": data_length}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        result=json.dumps(r.text)
        return result
    filename="1.wav"
    signal = open(filename, "rb").read()
    rate = 16000
    token = get_token()
    return recognize(signal, rate, token)