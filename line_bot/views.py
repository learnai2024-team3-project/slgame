from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

# 引入 linebot SDK
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage, TextMessage

from linebot.models import URIAction, PostbackAction, MessageAction, TemplateSendMessage, CarouselTemplate,  CarouselColumn

# 建立 linebot classs 進行連線
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

line_bot_api.push_message(settings.LINE_USER_ID, TemplateSendMessage(
    alt_text='CarouselTemplate',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='https://steam.oxxostudio.tw/download/python/line-template-message-demo.jpg',
                title='難度選擇',
                actions=[
                    PostbackAction(
                        label='學習模式',
                    ),
                    MessageAction(
                        label='挑戰模式',
                    ),
                    MessageAction(
                        label='競賽',
                    ),
                ]
            )
        ]
    )
))

@csrf_exempt
def callback(request):
    if (request.method == "POST"):
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
       
        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    res_text = event.message.text
                    line_bot_api.reply_message(event.reply_token, TextSendMessage(text = res_text))
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
