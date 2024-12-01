import numpy as np
import re,json
import pandas as pd
from fuzzywuzzy import fuzz
from DrissionPage import Chromium
from playwright.sync_api import sync_playwright


'''利用drissionpage来登录保存cookie到本地'''
# tab=Chromium().latest_tab
# tab.get('https://www.modelscope.cn/studios/qwen/Qwen2-72B-Instruct-demo')
# a=input('登录好就回车')
# cookies_list = tab.cookies()
# for subdic in cookies_list:
#     if subdic.get('path')==None:
#         subdic['path']='/'
# with open(f"./playwright_cookie.json",'w',encoding='utf-8') as f1:
#     file=json.dumps({'cookies_list':cookies_list},indent=True,ensure_ascii=False)
#     f1.write(file)
# tab.close()


'''在原始页面locator到iframe后直接操作'''
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context()
    with open('./modelscope_cookie.json','r',encoding='utf-8') as f1:
        cookies_list=json.load(f1)['cookies_list']
    context.add_cookies(cookies_list)
    page=context.new_page()
    page.goto('https://www.modelscope.cn/studios/qwen/Qwen2-72B-Instruct-demo')
    
    frame=page.frame_locator('#iFrameResizer0')
    frame.locator('#component-11 > label > textarea').fill('你好')
    frame.locator('#component-14').click() #发送按钮

    page.wait_for_load_state('networkidle')
    reply=frame.locator('#component-10 > div.wrapper.svelte-nab2ao > div > div > div.message-row.bubble.bot-row.svelte-1lcyrx4 > div > button').text_content()
    print(reply)
    a=input('等待')
    frame.locator('#component-13').click() #清空按钮

    a=input('等待')

    frame.locator('#component-11 > label > textarea').fill('帮我写一首诗')
    frame.locator('#component-14').click() #发送按钮
    page.wait_for_load_state('networkidle')
    reply=frame.locator('#component-10 > div.wrapper.svelte-nab2ao > div > div > div.message-row.bubble.bot-row.svelte-1lcyrx4 > div > button').text_content()
    print(reply)
    a=input('等待')

# ==============================================================================================



'''将iframe里的链接拿出来单独操作'''
# with sync_playwright() as p:
#     browser=p.chromium.launch(headless=False)
#     page=browser.new_page()
#     page.goto('https://s5k.cn/inner/studio/gradio?backend_url=/api/v1/studio/Qwen/Qwen2-72B-Instruct-demo/gradio/&sdk_version=4.19.1&t=1732497080626&__theme=dark&studio_token=f5b338dc-7cc0-4fec-badc-e84c14883f0e')
#     page.locator("#component-11 > label > textarea").fill('你好')
#     page.locator("#component-14").click()

#     page.wait_for_load_state('networkidle')
#     item=page.locator("#component-10 > div.wrapper.svelte-nab2ao > div > div > div.message-row.bubble.bot-row.svelte-1lcyrx4 > div > button")
#     reply=item.text_content()
#     print(reply)

#     b=input('等待')
#     page.click("#component-13")
#     b=input('等待')
#     page.fill("#component-11 > label > textarea",'给我作一首诗')
#     page.click("#component-14")
#     b=input('等待')
#     page.wait_for_load_state('networkidle')
#     item=page.locator("#component-10 > div.wrapper.svelte-nab2ao > div > div > div.message-row.bubble.bot-row.svelte-1lcyrx4 > div > button")
#     reply=item.text_content()
#     print(reply)

#     b=input('等待')



