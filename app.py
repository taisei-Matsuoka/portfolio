import json

import gspread

from oauth2client.service_account import ServiceAccountCredentials 
#---------------------line bot ------------------------------------
import datetime
import os
import random
import time 

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import FollowEvent, MessageEvent, TextMessage, TextSendMessage,imagemap,ImagemapSendMessage,ImagemapAction,ImagemapArea,ImageSendMessage,TemplateSendMessage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credential = ServiceAccountCredentials.from_json_keyfile_name('linedatekey.json', scope)
gc = gspread.authorize(credential)
SPREADSHEET_KEY = 'キー'
workbook=gc.open_by_key(SPREADSHEET_KEY)
worksheet1 = workbook.worksheet('sheet1')
worksheet3 = workbook.worksheet('sheet3')
tarotto =workbook.worksheet('タロット')
follow = workbook.worksheet('追加時')

app = Flask(__name__)

line_bot_api = LineBotApi('チャンネルアクセストークン')
handler = WebhookHandler('ID')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'



@handler.add(MessageEvent)
def Message_event(event):
    #--------------------- USER INFO ------------------------------------
    profile = line_bot_api.get_profile(event.source.user_id)
    
    user_info = (
        profile.display_name,
        datetime.datetime.today().strftime("%Y/%m/%d"),
        profile.user_id
    )

    worksheet1.append_row(user_info)
    #--------------------- Text Info ------------------------------------
    # text_info=(
    #     profile.display_name,
    #     profile.user_id,
    #     event.message.text
    #     )
    # worksheet3.append_row(text_info)
    text_content = event.message.text 
    content = text_content .translate(str.maketrans({chr(0xFF01 + i): chr(0x21 + i) for i in range(94)}))
    #--------------------- Tarotto(usually) ------------------------------------
    if content=='1':
        tarot2 = tarotto.cell(2,1).value
        imagemes1 = ImageSendMessage(
          original_content_url=tarot2,
          preview_image_url=tarot2
        )
        message = tarotto.cell(10,3).value
        text_content = TextSendMessage(text=message)
        time.sleep(2)
        line_bot_api.reply_message(event.reply_token,imagemes1)
        time.sleep(2)
        profile = line_bot_api.get_profile(event.source.user_id)
        user_id = profile.user_id
        time.sleep(2)
        line_bot_api.push_message(user_id,text_content)
        
 
    elif content=='2':
        tarot2 = tarotto.cell(3,1).value
        imagemes1 = ImageSendMessage(
          original_content_url=tarot2,
          preview_image_url=tarot2
        )
        message = tarotto.cell(10,3).value
        text_content = TextSendMessage(text=message)
        time.sleep(2)
        line_bot_api.reply_message(event.reply_token,imagemes1)
        time.sleep(2)
        profile = line_bot_api.get_profile(event.source.user_id)
        user_id = profile.user_id
        time.sleep(2)
        line_bot_api.push_message(user_id,text_content)

    elif content=='3':
        tarot2 = tarotto.cell(4,1).value
        imagemes1 = ImageSendMessage(
          original_content_url=tarot2,
          preview_image_url=tarot2
        )
        message = tarotto.cell(10,3).value
        text_content = TextSendMessage(text=message)
        time.sleep(2)
        line_bot_api.reply_message(event.reply_token,imagemes1)
        time.sleep(2)
        profile = line_bot_api.get_profile(event.source.user_id)
        user_id = profile.user_id
        time.sleep(2)
        line_bot_api.push_message(user_id,text_content)

    elif content=='4':
        tarot2 = tarotto.cell(5,1).value
        imagemes1 = ImageSendMessage(
          original_content_url=tarot2,
          preview_image_url=tarot2
        )
        message = tarotto.cell(10,3).value
        text_content = TextSendMessage(text=message)
        time.sleep(2)
        line_bot_api.reply_message(event.reply_token,imagemes1)
        time.sleep(2)
        profile = line_bot_api.get_profile(event.source.user_id)
        user_id = profile.user_id
        time.sleep(2)
        line_bot_api.push_message(user_id,text_content)
      
    elif content=='5':
        tarot2 = tarotto.cell(6,1).value
        imagemes1 = ImageSendMessage(
          original_content_url=tarot2,
          preview_image_url=tarot2
        )
        message = tarotto.cell(10,3).value
        text_content = TextSendMessage(text=message)
        time.sleep(2)
        line_bot_api.reply_message(event.reply_token,imagemes1)
        time.sleep(2)
        profile = line_bot_api.get_profile(event.source.user_id)
        user_id = profile.user_id
        time.sleep(2)
        line_bot_api.push_message(user_id,text_content)
      
    elif content=='6':
        tarot2 = tarotto.cell(7,1).value
        imagemes1 = ImageSendMessage(
          original_content_url=tarot2,
          preview_image_url=tarot2
        )
        message = tarotto.cell(10,3).value
        text_content = TextSendMessage(text=message)
        time.sleep(2)
        line_bot_api.reply_message(event.reply_token,imagemes1)
        time.sleep(2)
        profile = line_bot_api.get_profile(event.source.user_id)
        user_id = profile.user_id
        time.sleep(2)
        line_bot_api.push_message(user_id,text_content)
    
    #--------------------- tarotto(follow) ------------------------------------
    elif content=='A':
        tarot2 = tarotto.cell(2,1).value
        imagemes1 = ImageSendMessage(
          original_content_url=tarot2,
          preview_image_url=tarot2
        )
        line_bot_api.reply_message(event.reply_token,imagemes1)
        time.sleep(2)
        qusetion = {
            "type": "template",
            "altText": "アンケート",
            "template": {
                "type": "buttons",
                "thumbnailImageUrl": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Tao_Tsuchiya_IMG_0919-30_20181111.jpg/250px-Tao_Tsuchiya_IMG_0919-30_20181111.jpg",
                "imageAspectRatio": "rectangle",
                "title": "初回登録アンケート",
                "text": "アンケート回答後「回答しました」のボタンを押してください",
                "actions": [
                {
                    "type": "uri",
                    "label": "アンケート",
                    "uri": "https://liff.line.me/1655971201-7JvVADVj"
                },
                {
                    "type": "message",
                    "label": "アンケート回答しました",
                    "text": "アンケート回答しました"
                }
                ]
            }
            }
        question1 = TemplateSendMessage.new_from_json_dict(qusetion)
        time.sleep(2)
        profile = line_bot_api.get_profile(event.source.user_id)
        user_id = profile.user_id
        message = follow.cell(2,3).value
        text_content = TextSendMessage(text=message)
        line_bot_api.push_message(user_id,text_content)
        time.sleep(2)
        line_bot_api.push_message(user_id,question1)

    elif content=='B':
        tarot2 = tarotto.cell(3,1).value
        imagemes1 = ImageSendMessage(
          original_content_url=tarot2,
          preview_image_url=tarot2
        )
        line_bot_api.reply_message(event.reply_token,imagemes1)
        time.sleep(2)
        qusetion = {
            "type": "template",
            "altText": "アンケート",
            "template": {
                "type": "buttons",
                "thumbnailImageUrl": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Tao_Tsuchiya_IMG_0919-30_20181111.jpg/250px-Tao_Tsuchiya_IMG_0919-30_20181111.jpg",
                "imageAspectRatio": "rectangle",
                "title": "初回登録アンケート",
                "text": "アンケート回答後「回答しました」のボタンを押してください",
                "actions": [
                {
                    "type": "uri",
                    "label": "アンケート",
                    "uri": "https://liff.line.me/1655971201-7JvVADVj"
                },
                {
                    "type": "message",
                    "label": "アンケート回答しました",
                    "text": "アンケート回答しました"
                }
                ]
            }
            }
        time.sleep(2)
        question1 = TemplateSendMessage.new_from_json_dict(qusetion)
        profile = line_bot_api.get_profile(event.source.user_id)
        user_id = profile.user_id
        message = follow.cell(2,3).value
        text_content = TextSendMessage(text=message)
        line_bot_api.push_message(user_id,text_content)
        time.sleep(2)
        line_bot_api.push_message(user_id,question1)
    
    elif content=='C':
        tarot2 = tarotto.cell(4,1).value
        imagemes1 = ImageSendMessage(
          original_content_url=tarot2,
          preview_image_url=tarot2
        )
        time.sleep(2)
        line_bot_api.reply_message(event.reply_token,imagemes1)
        qusetion = {
            "type": "template",
            "altText": "アンケート",
            "template": {
                "type": "buttons",
                "thumbnailImageUrl": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Tao_Tsuchiya_IMG_0919-30_20181111.jpg/250px-Tao_Tsuchiya_IMG_0919-30_20181111.jpg",
                "imageAspectRatio": "rectangle",
                "title": "初回登録アンケート",
                "text": "アンケート回答後「回答しました」のボタンを押してください",
                "actions": [
                {
                    "type": "uri",
                    "label": "アンケート",
                    "uri": "https://liff.line.me/1655971201-7JvVADVj"
                },
                {
                    "type": "message",
                    "label": "アンケート回答しました",
                    "text": "アンケート回答しました"
                }
                ]
            }
            }
        time.sleep(2)
        question1 = TemplateSendMessage.new_from_json_dict(qusetion)
        profile = line_bot_api.get_profile(event.source.user_id)
        user_id = profile.user_id
        message = follow.cell(2,3).value
        text_content = TextSendMessage(text=message)
        line_bot_api.push_message(user_id,text_content)
        time.sleep(2)
        line_bot_api.push_message(user_id,question1)

    elif content=='D':
        tarot2 = tarotto.cell(5,1).value
        imagemes1 = ImageSendMessage(
          original_content_url=tarot2,
          preview_image_url=tarot2
        )
        time.sleep(2)
        line_bot_api.reply_message(event.reply_token,imagemes1)
        qusetion = {
            "type": "template",
            "altText": "アンケート",
            "template": {
                "type": "buttons",
                "thumbnailImageUrl": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Tao_Tsuchiya_IMG_0919-30_20181111.jpg/250px-Tao_Tsuchiya_IMG_0919-30_20181111.jpg",
                "imageAspectRatio": "rectangle",
                "title": "初回登録アンケート",
                "text": "アンケート回答後「回答しました」のボタンを押してください",
                "actions": [
                {
                    "type": "uri",
                    "label": "アンケート",
                    "uri": "https://liff.line.me/1655971201-7JvVADVj"
                },
                {
                    "type": "message",
                    "label": "アンケート回答しました",
                    "text": "アンケート回答しました"
                }
                ]
            }
            }
        time.sleep(2)
        question1 = TemplateSendMessage.new_from_json_dict(qusetion)
        profile = line_bot_api.get_profile(event.source.user_id)
        user_id = profile.user_id
        message = follow.cell(2,3).value
        text_content = TextSendMessage(text=message)
        line_bot_api.push_message(user_id,text_content)
        time.sleep(2)
        line_bot_api.push_message(user_id,question1)
        
    elif content=='E':
        tarot2 = tarotto.cell(6,1).value
        imagemes1 = ImageSendMessage(
          original_content_url=tarot2,
          preview_image_url=tarot2
        )
        time.sleep(2)
        line_bot_api.reply_message(event.reply_token,imagemes1)
        qusetion = {
            "type": "template",
            "altText": "アンケート",
            "template": {
                "type": "buttons",
                "thumbnailImageUrl": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Tao_Tsuchiya_IMG_0919-30_20181111.jpg/250px-Tao_Tsuchiya_IMG_0919-30_20181111.jpg",
                "imageAspectRatio": "rectangle",
                "title": "初回登録アンケート",
                "text": "アンケート回答後「回答しました」のボタンを押してください",
                "actions": [
                {
                    "type": "uri",
                    "label": "アンケート",
                    "uri": "https://liff.line.me/1655971201-7JvVADVj"
                },
                {
                    "type": "message",
                    "label": "アンケート回答しました",
                    "text": "アンケート回答しました"
                }
                ]
            }
            }
        time.sleep(2)
        question1 = TemplateSendMessage.new_from_json_dict(qusetion)
        profile = line_bot_api.get_profile(event.source.user_id)
        user_id = profile.user_id
        message = follow.cell(2,3).value
        text_content = TextSendMessage(text=message)
        line_bot_api.push_message(user_id,text_content)
        time.sleep(2)
        line_bot_api.push_message(user_id,question1)

    elif content=='F':
        tarot2 = tarotto.cell(7,1).value
        imagemes1 = ImageSendMessage(
          original_content_url=tarot2,
          preview_image_url=tarot2
        )
        time.sleep(2)
        line_bot_api.reply_message(event.reply_token,imagemes1)
        qusetion = {
            "type": "template",
            "altText": "アンケート",
            "template": {
                "type": "buttons",
                "thumbnailImageUrl": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Tao_Tsuchiya_IMG_0919-30_20181111.jpg/250px-Tao_Tsuchiya_IMG_0919-30_20181111.jpg",
                "imageAspectRatio": "rectangle",
                "title": "初回登録アンケート",
                "text": "アンケート回答後「回答しました」のボタンを押してください",
                "actions": [
                {
                    "type": "uri",
                    "label": "アンケート",
                    "uri": "https://liff.line.me/1655971201-7JvVADVj"
                },
                {
                    "type": "message",
                    "label": "アンケート回答しました",
                    "text": "アンケート回答しました"
                }
                ]
            }
            }
        time.sleep(2)
        question1 = TemplateSendMessage.new_from_json_dict(qusetion)
        profile = line_bot_api.get_profile(event.source.user_id)
        user_id = profile.user_id
        time.sleep(2)
        message = follow.cell(2,3).value
        text_content = TextSendMessage(text=message)
        line_bot_api.push_message(user_id,text_content)
        time.sleep(2)
        line_bot_api.push_message(user_id,question1)
        
    
    elif content=='アンケート回答しました':
        profile = line_bot_api.get_profile(event.source.user_id)
        name =profile.display_name
        message = name+'さん \n ありがとうございます'
        text_content = TextSendMessage(text=message)
        line_bot_api.reply_message(event.reply_token,text_content)
        time.sleep(120)


@handler.add(FollowEvent)
def follow_event(event):

    profile = line_bot_api.get_profile(event.source.user_id)
    
    user_info = (
        profile.display_name,
        datetime.datetime.today().strftime("%Y/%m/%d"),
        profile.user_id
    )

    worksheet1.append_row(user_info)
    user_id = profile.user_id
    user_name = profile.display_name
    
    #最初のメッセージ①
    message1 = user_name +"さん 始めまして \nスピリチュアルカウンセラー武蔵です。\nお友だち追加ありがとうございます！\n \nこちらのLINEでは、\n♦️毎週日曜配信 心にブッ刺さるタロット！\n♦️お役立て頂けるコラム配信！\n♦️各種イベント・サービスのご案内\nなどを配信してます \n👇公式ＨＰはコチラ\n https://pearch-634.com \n プロフィール・セッションメニュー・各種リンク\n\n🏵愛と調和と感謝を込めて🏵\n(本)お願い(本)ご連絡頂き、既読済みでも、すぐに返信出来ない場合もあります。\n気長にお待ち下さいね☺️" 
    text_content1 = TextSendMessage(text=message1)
    time.sleep(2)
    #最初のメッセージ②
    message2= follow.cell(2,2).value
    text_content2 = TextSendMessage(text=message2)
    time.sleep(2)

    imagemap ={
      "type": "imagemap",
      "baseUrl": "https://pearch-634.com/wp-content/themes/musashi-wp/images/tarot",
      "altText": "初めての武蔵タロットコーナー",
      "baseSize": {
          "width": 1040,
          "height": 1040
      },
      "actions": [
          {
          "type": "message",
          "area": {
              "x": 56,
              "y": 126,
              "width": 255,
              "height": 370
          },
          "text": "A"
          },
          {
          "type": "message",
          "area": {
              "x": 404,
              "y": 128,
              "width": 242,
              "height": 365
          },
          "text": "B"
          },
          {
          "type": "message",
          "area": {
              "x": 722,
              "y": 120,
              "width": 253,
              "height": 367
          },
          "text": "C"
          },
          {
          "type": "message",
          "area": {
              "x": 71,
              "y": 569,
              "width": 251,
              "height": 363
          },
          "text": "D"
          },
          {
          "type": "message",
          "area": {
              "x": 390,
              "y": 549,
              "width": 258,
              "height": 375
          },
          "text": "E"
          },
          {
          "type": "message",
          "area": {
              "x": 738,
              "y": 557,
              "width": 237,
              "height": 357
          },
          "text": "F"
      }
      ]
      }
    time.sleep(2)
    ima = ImagemapSendMessage.new_from_json_dict(imagemap)
    time.sleep(2)
    line_bot_api.push_message(user_id,text_content1)
    time.sleep(2)
    line_bot_api.push_message(user_id,text_content2)
    time.sleep(2)
    line_bot_api.push_message(user_id,ima) 


@app.route('/')
def index():
    return 'Hello World!'

if __name__ == "__main__":
    app.run()
