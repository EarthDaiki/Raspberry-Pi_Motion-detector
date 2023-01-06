from datetime import datetime
import time
import RPi.GPIO as GPIO

from linebot import LineBotApi
from linebot.models import (TextSendMessage, ImageSendMessage)

# インターバル
INTERVAL = 1
# スリープタイム
SLEEPTIME = 3
# 使用するGPIO
GPIO_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.IN)

token = 'emgDnvJyowYjaRQP0U2FkATsXhMqSHb09kFaaVzOHX5QCN0paiBtHp/h8qekZttCSCyzlXMafRRh1zbmTWvPwCV+04QmzpCcQg4m5wJYB+U0fyoSQ8KBHMiUxf+gr16YXYlNgFA6hQ0q4Extgevs3gdB04t89/1O/w1cDnyilFU='
user_id = 'Ud257c5dbea255803d3a0529963c9699e'

line_bot_api = LineBotApi(token)
messages = []


if __name__ == '__main__':
    try:
        print ("処理キャンセル：CTRL+C")
        cnt = 1
        while True:
            # センサー感知
            if(GPIO.input(GPIO_PIN) == GPIO.HIGH):
                print(datetime.now().strftime('%Y/%m/%d %H:%M:%S') +
                "：" + str("{0:05d}".format(cnt)) + "回目の人感知")
                text = TextSendMessage(text=f"検出")
                messages = ImageSendMessage(original_content_url = 'https://drive.google.com/uc?id=0B7HEy-N0Aa6BODZTZVQ4VnZWb0U',
                                        preview_image_url = 'https://drive.google.com/uc?id=0B7HEy-N0Aa6BODZTZVQ4VnZWb0U')
                line_bot_api.push_message(user_id, messages=messages)
                cnt = cnt + 1
                time.sleep(SLEEPTIME)
            else:
                print(GPIO.input(GPIO_PIN))
                time.sleep(INTERVAL)
    except KeyboardInterrupt:
        print("終了処理中...")
    finally:
        GPIO.cleanup()
        print("GPIO clean完了")