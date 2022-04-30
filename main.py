from flask import Flask, request
import json
import httpx
import urllib.parse
app = Flask(__name__)


@app.route("/", methods=['POST'])
async def recvMsg():
    data = request.get_data()
    json_data = json.loads(data.decode("utf-8"))
    if json_data["type"] == "LiveBeganEvent":
        username = json_data["data"]["user_info"]["name"]
        msg = username + '开播了'
        senddata = {"chat_id": TG_ID, "text": msg, "disable_web_page_preview": "false"}
        url = f"https://api.telegram.org/bot{KEY}/sendMessage"
        await httpx.AsyncClient().post(url=url, data=senddata)
    elif json_data["type"] == "LiveEndedEvent":
        username = json_data["data"]["user_info"]["name"]
        msg = username + '下播了'
        senddata = {"chat_id": TG_ID, "text": msg, "disable_web_page_preview": "false"}
        url = f"https://api.telegram.org/bot{KEY}/sendMessage"
        await httpx.AsyncClient().post(url=url, data=senddata)
    return "200 OK"


if __name__ == '__main__':
    TOKEN = ''
    UID = ''
    app.run(host="0.0.0.0", port=5000)
