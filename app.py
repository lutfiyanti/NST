from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import requests, json


import errno
import os
import sys, random
import tempfile
import requests
import re

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent,
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('fZklMpUf7UueAqA1DtHj3V8+Udz9toJ1AEf/7iqchW3od8eoDfdi0/0UV5t/PqSfnHtVQZLtie3eOu6JgKKfpbUr40rMWj1RfmdyxNSIOGJm6Ppd7wZGGl0zfWKONWEBlifqBPiZcjoDWWai+MdnwAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('8d34f33a911c087bfa231108a614b282')
#===========[ NOTE SAVER ]=======================
notes = {}

#REQUEST DATA MHS
def carimhs(input):
    URLmhs = 
"https://www.aditmasih.tk/api_yemima/show.php?nrp=" + 
input
    irham = requests.get(URLmhs)
    data = irham.json()
    err = "data tidak ditemukan"
    
    flag = data['flag']
    if(flag == "1"):
        nrp = data['data_admin'][0]['nrp']
        nama = data['data_admin'][0]['nama']
        kos = data['data_admin'][0]['alamat']

        return nama + '\n' + nrp + '\n' + kos
    elif(flag == "0"):
        return err    

# Post Request
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text #simplify for receove message
    sender = event.source.user_id #get usesenderr_id
    gid = event.source.sender_id #get group_id
    profile = line_bot_api.get_profile(sender)
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=carimhs(text)))
    #line_bot_api.reply_message(event.reply_token,TextSendMessage(text="masuk"))
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
