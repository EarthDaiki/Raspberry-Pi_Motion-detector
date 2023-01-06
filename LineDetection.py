from datetime import datetime
import time
import RPi.GPIO as GPIO

from linebot import LineBotApi
from linebot.models import (TextSendMessage, ImageSendMessage)


INTERVAL = 1

SLEEPTIME = 3

GPIO_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.IN)

token = '****'
user_id = '****'

line_bot_api = LineBotApi(token)
messages = []


if __name__ == '__main__':
    try:
        print ("Running Stop：CTRL+C")
        cnt = 1
        while True:
            # sensor
            if(GPIO.input(GPIO_PIN) == GPIO.HIGH):
                print(datetime.now().strftime('%Y/%m/%d %H:%M:%S') +
                "：" + str("{0:05d}".format(cnt)) + "回目の人感知")
                text = TextSendMessage(text="検出")
                #messages = ImageSendMessage(original_content_url = 'https://i.pinimg.com/originals/8d/f6/39/8df639cd6f9624f3341da7e37e15d0af.jpg',
                                        #preview_image_url = 'https://i.pinimg.com/originals/8d/f6/39/8df639cd6f9624f3341da7e37e15d0af.jpg')
                line_bot_api.push_message(user_id, text)
                cnt = cnt + 1
                time.sleep(SLEEPTIME)
            else:
                print(GPIO.input(GPIO_PIN))
                time.sleep(INTERVAL)
    except KeyboardInterrupt:
        print("Stopping Running")
    finally:
        GPIO.cleanup()
        print("GPIO clean completed")