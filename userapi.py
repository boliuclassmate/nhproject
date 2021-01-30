# -*- coding: UTF-8 -*-
from runner.extapi import *
# 添加用户封装
# from userlib.demo_lib import *
# TODO: write your code

def dianji():
    # 针对不同分辨率设备的点击点击处理
    sleep(2.56)
    click((186, 552))
    sleep(2.80)
    click((196, 517))
    sleep(2.58)
    click((196, 517))
    sleep(2.14)
    click((196, 517))
    sleep(2.23)
    multiTouch('1611200741.3071668.json')
    sleep(1.27)
    multiTouch('1611200742.5797331.json')
    sleep(1.02)
    multiTouch('1611200743.603225.json')
    sleep(1.18)
    multiTouch('1611200744.7724543.json')
    sleep(1.07)
    multiTouch('1611200745.8537383.json')
    sleep(0.97)
    multiTouch('1611200746.8204262.json')
    sleep(2.43)
    click((203, 523))
    sleep(2.93)
    click((203, 523))
    sleep(2.93)
    click((203, 523))
    sleep(2.73)
    click((203, 523))
    sleep(3.15)
    click((203, 523))
    sleep(2.50)
    click((203, 523))
    sleep(2.72)
    click((203, 523))
    sleep(3.34)
    sleep(5)

def kai_shi(*args, **kwargs):

    #TODO: 拉起QQ等待隐私确认
    sleep(30)
    try:
        # 同意
        click('obj_1610682590554.jpg', position=(0.544, 0.64, 0.906, 0.696), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        click_text('同意', pic = 'obj_1610682590554.jpg', xOffset = 0, yOffset = 0)
    sleep(8)

    loginByQQ('obj_1610682172721.jpg', acc = '', pwd = '')
    sleep(8)

    try:
        # 联系人
        click('/text="联系人" && type="android.widget.TextView"', xOffset=0, yOffset=0, by=DriverType.UIAUTOMATOR, timeOut=20)
    except: 
        click('obj_1610683050735.jpg', position=(0.307, 0.934, 0.444, 0.996), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        logger.info('联系人')
    sleep(12)

    try:
        # 设备
        click('/text="设备" && type="android.widget.TextView"', xOffset=0, yOffset=0, by=DriverType.UIAUTOMATOR, timeOut=20)
    except:
        click('obj_1610683108649.jpg', position=(0.69, 0.345, 0.86, 0.388), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        logger.info('设备')
    sleep(12)

    try:
        # 我的电脑
        click('|resourceid="com.tencent.mobileqq:id/f99" && type="android.widget.LinearLayout" && instance="0"', xOffset=0, yOffset=0, by=DriverType.UIAUTOMATOR, timeOut=20)
    except:
        click('obj_1610683185760.jpg', position=(0.015, 0.407, 0.465, 0.474), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    sleep(12)

    try:
        # 拉起输入框 输入URL

        click('|resourceid="com.tencent.mobileqq:id/input" && type="android.widget.EditText"', xOffset=0, yOffset=0, by=DriverType.UIAUTOMATOR, timeOut=20)
    except:
        click('obj_1610683262455.jpg', xOffset=-0.257,yOffset=-0.001, position=(0.815, 0.907, 0.945, 0.945))
    sleep(8)

    try:
        # 输入url
        # 嘉宾
        #https://nba2k2.qq.com/act/a20210105fxxyqh/index.html?p=%7B%22code%22%3A0%2C%22msg%22%3A%22%22%2C%22data%22%3A%7B%22ename%22%3A%22mmliu%22%2C%22guest%22%3A1%2C%22desk%22%3A1%2C%22seat%22%3A1%2C%22desc_t%22%3A%22%E5%A5%94%E6%B6%8C%E4%B9%8B%E5%8A%BF%22%2C%22desc_c%22%3A%22%E5%89%8D%E6%B5%AA%E4%B9%8B%E5%8B%87%EF%BC%8C%E5%90%8E%E6%B5%AA%E4%B9%8B%E5%9F%BA%5Cn%E5%90%8E%E6%B5%AA%E4%B9%8B%E9%80%90%EF%BC%8C%E5%89%8D%E6%B5%AA%E4%B9%8B%E7%BB%AD%5Cn%E5%A5%94%E6%B6%8C%E6%98%AF%E9%9D%92%E6%98%A5%E6%9C%80%E7%BE%8E%E7%9A%84%E5%A7%BF%E6%80%81%5Cn2021%EF%BC%8C%E5%A5%94%E6%B6%8C%E5%90%A7%E5%8B%87%E5%A3%AB%22%2C%22role_s%22%3A%22game_role5_png%22%2C%22role_x%22%3A42%2C%22role_y%22%3A393%2C%22title_c%22%3A%22%E5%87%86%E5%A4%87%E5%A5%BDC%E4%BD%8D%E5%87%BA%E9%81%93%22%7D%7D

 
        inputText(text='https://nba2k2.qq.com/act/a20210105fxxyqh/index.html?p=%7B%22code%22%3A0%2C%22msg%22%3A%22%22%2C%22data%22%3A%7B%22ename%22%3A%22mmliu%22%2C%22guest%22%3A1%2C%22desk%22%3A1%2C%22seat%22%3A1%2C%22desc_t%22%3A%22%E5%A5%94%E6%B6')
        sleep(6)
        inputText(text='%8C%E4%B9%8B%E5%8A%BF%22%2C%22desc_c%22%3A%22%E5%89%8D%E6%B5%AA%E4%B9%8B%E5%8B%87%EF%BC%8C%E5%90%8E%E6%B5%AA%E4%B9%8B%E5%9F%BA%5Cn%E5%90%8E%E6%B5%AA%E4%B9%8B%E9%80%90%EF%BC%8C%E5%89%8D%E6%B5%AA%E4%B9%8B%E7%BB%AD%5Cn%E5%A5%94%E6%B6%8C%E6%98%AF%E9%9D%92%E6%98%A5%E6%9C%80%E7%BE%8E%E7%9A%84%E5%')
        sleep(6)
        inputText(text='A7%BF%E6%80%81%5Cn2021%EF%BC%8C%E5%A5%94%E6%B6%8C%E5%90%A7%E5%8B%87%E5%A3%AB%22%2C%22role_s%22%3A%22game_role5_png%22%2C%22role_x%22%3A42%2C%22role_y%22%3A393%2C%22title_c%22%3A%22%E5%87%86%E5%A4%87%E5%A5%BDC%E4%BD%8D%E5%87%BA%E9%81%93%22%7D%7D')
    except:
        logger.info('输入活动url')
    sleep(24)

    try:
        # 点击发送
        click('/text="发送" && type="android.widget.Button"', xOffset=0, yOffset=0, by=DriverType.UIAUTOMATOR, timeOut=20)
    except:
        click_text('发送')
    sleep(8)

    try:
        click('obj_1611232250969.jpg', xOffset=-0.008,yOffset=0.112, position=(0.395, 0.043, 0.593, 0.083))
    except:
        click((0.498, 0.165), position=None)
    sleep(18)

    
def IEG(*args, **kwargs):
    
    #TODO: 进入指定活动界面
    try:
        # 滑动界面
        swipe('1611198153.8167605.json')
    except:
        pass
    sleep(12)

    try:
        # 感谢信
        swipe('1611198184.2759895.json')
    except:
        pass
    sleep(4)

    try:
        # 2021 
        dianji()
    except:
        pass
    sleep(18)

    try:
        # 滑动至奖池
        swipe('1611199036.4902825.json')
        sleep(2.04)
        swipe('1611199038.5320208.json')
    except:
        pass
    sleep(5)

    try:
        # 再看一次
        click('obj_1611199088311.jpg', position=(0.131, 0.902, 0.465, 0.951), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        click_text('再看一次')
    sleep(5)

    try:
        # 再看一次
        dianji()
    except:
        pass

    try:
        # 领取门票
        click('obj_1611199388609.jpg', position=(0.605, 0.903, 0.939, 0.951), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        click_text('领取门票')
    sleep(12)

    try:
        # 保存本地
        longClick('obj_1611199509407.jpg', longClickTime=4)
    except:
        longClick((0.523, 0.585), longClickTime=4, position=None)

    sleep(6)

    if exists('obj_1611199579745.jpg', timeOut=20, by=DriverType.CV):
        try:
            click('obj_1611199534407.jpg', position=(0.328, 0.799, 0.669, 0.856), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            click_text('保存到本地')
    sleep(12)

    try:
        # 立即解锁年会
        click('obj_1611219348387.jpg', position=(0.66, 0.777, 0.891, 0.799), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        click_text('立即预约年会')
    sleep(4)

    try:
        # 关闭
        click('obj_1611219396711.jpg', position=(0.471, 0.788, 0.535, 0.822), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        click((0.498, 0.788), position=None)
    sleep(5)
    
    try:
        # 扫描二维码
        longClick('obj_1611199509407.jpg', longClickTime=4)
    except:
        longClick((0.523, 0.585), longClickTime=4, position=None)

    sleep(6)  

    if exists('obj_1611201376401.jpg', timeOut=20, by=DriverType.CV):
        try:
            # 扫描二维码
            click('obj_1611201335729.jpg', position=(0.356, 0.868, 0.653, 0.917), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            click_text('扫描二维码')
    sleep(12)
    
'''
        inputText(text='https://nba2k2.qq.com/act/a20210105fxxyqh/index.html?p=%7B%22code%22%3A0%2C%22msg%22%3A%22%22%2C%22data%22%3A%7B%22ename%22%3A%22mmliu%22%2C%22guest%22%3A1%2C%22desk%22%3A1%2C%22seat%22%3A1%2C%22desc_t%22%3A%22%E5%A5%94%E6%B6%8C%E4%B9%8B%E5%8A%BF%22%2C%22desc_c%22%3A%22%E5%89%8D')
        sleep(6)
        inputText(text='%E6%B5%AA%E4%B9%8B%E5%8B%87%EF%BC%8C%E5%90%8E%E6%B5%AA%E4%B9%8B%E5%9F%BA%5Cn%E5%90%8E%E6%B5%AA%E4%B9%8B%E9%80%90%EF%BC%8C%E5%89%8D%E6%B5%AA%E4%B9%8B%E7%BB%AD%5Cn%E5%A5%94%E6%B6%8C%E6%98%AF%E9%9D%92%E6%98%A5%E6%9C%80%E7%BE%8E%E7%9A%84%E5%A7%BF%E')
        sleep(6)
        inputText(text='6%80%81%5Cn2021%EF%BC%8C%E5%A5%94%E6%B6%8C%E5%90%A7%E5%8B%87%E5%A3%AB%22%2C%22role_s%22%3A%22game_role5_png%22%2C%22role_x%22%3A42%2C%22role_y%22%3A393%2C%22title_c%22%3A%22%E5%87%86%E5%A4%87%E5%A5%BDC%E4%BD%8D%E5%87%BA%E9%81%93%22%7D%7D')
'''

'''
def wzry(*args, **kwargs):
    """
    这里填写函数定义
    """
    #TODO: 这里编写具体代码
    try:
        # 活动规则
        click('obj_1611038667703.jpg', position=(0.447, 0.374, 0.553, 0.397), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        click_text('活动规则')
    sleep(4)

    try:
        # 关闭活动规则
        click('obj_1611038781410.jpg', position=(0.465, 0.752, 0.535, 0.784), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        click((0.505, 0.769), position=None)
    sleep(4)

    try:
        # 向下滑动
        slide((0.274, 0.731), (0.28, 0.156))
        slide((0.243, 0.736), (0.267, 0.562))
    except:
        slide('obj_1611038936692.jpg', 'obj_1611038945498.jpg')
    sleep(4)


    try:
        # 曲池坊
        click('obj_1611038976995.jpg', position=(0.386, 0.266, 0.611, 0.302), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        click_text('曲池坊')
    sleep(4)

    try:
        # 郢酒坊
        click('obj_1611039404544.jpg', position=(0.684, 0.251, 0.897, 0.286), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        try:
            click('obj_1611039487801.jpg', position=(0.948, 0.617, 1, 0.676), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            click_text('郢酒坊')
    sleep(4)

    try:
        # 进入游戏
        click('obj_1611039037721.jpg', position=(0.325, 0.935, 0.66, 0.985), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        click_text('进入游戏')
    sleep(12)

    try:
        # 允许拉起游戏
        if exists('obj_1611039089505.jpg', timeOut=20, by=DriverType.CV):
            try:
                click('obj_1611039112623.jpg', position=(0.55, 0.554, 0.906, 0.596), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
            except:
                click_text('允许')
    except:
        pass
    sleep(12)



def huodong1(*args, **kwargs):
    
    # 组队预约新服集结
    #TODO: 这里编写具体代码
    try:
        click('obj_1610684169197.jpg', position=(0.313, 0.603, 0.684, 0.649), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        click_text('查看我的礼包池')
    sleep(5)
    try:
        # 预约角色信息
        click('/text="请选择系统" && type="android.widget.Spinner"', xOffset=0, yOffset=0, by=DriverType.UIAUTOMATOR, timeOut=20)
    except:
        logger.info('选择系统')
    try:
        click('obj_1610685207732.jpg', position=(0.131, 0.578, 0.505, 0.627), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        pass
    sleep(3)
    try:
        click('/text="请选择大区" && type="android.widget.Spinner"', xOffset=0, yOffset=0, by=DriverType.UIAUTOMATOR, timeOut=20)
    except:
        logger.info('选择大区')
    sleep(6)

    # 滑动至122 服务器
    while True:
        if exists('obj_1610685850412.jpg', timeOut=8, by=DriverType.CV):
            break
        else:
            slide((0.638, 0.607), (0.602, 0.262))
            slide((0.59, 0.727), (0.596, 0.56))
            sleep(2)
    try:
        # 122区
        click('obj_1610685850412.jpg', position=(0.106, 0.815, 0.617, 0.879), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:   
        click((0.435, 0.851), position=None)
    sleep(4)

    try:
        # 预约新服
        click('/text="请选择新区服" && type="android.widget.Spinner"', xOffset=0, yOffset=0, by=DriverType.UIAUTOMATOR, timeOut=20)
    except:
        click('obj_1610685661693.jpg', position=(0.31, 0.505, 0.568, 0.54), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)   
    sleep(4)

    try:
        # 124 新服
        click('obj_1610685718949.jpg', position=(0.109, 0.536, 0.584, 0.589), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        click('/text="124互通区-缥缈" && type="android.widget.TextView"', xOffset=0, yOffset=0, by=DriverType.UIAUTOMATOR, timeOut=20)
    sleep(12)
    try:
        # 关闭弹窗
        click('/text="关闭" && type="android.view.View"', xOffset=0, yOffset=0, by=DriverType.UIAUTOMATOR, timeOut=20)
    except:
        click('obj_1610694356594.jpg', xOffset=-0.003,yOffset=-0.042, position=(0.921, 0.269, 0.988, 0.303))
    sleep(3)


    try:
        slide((0.638, 0.607), (0.602, 0.262))
        sleep(2)
        slide((0.59, 0.727), (0.596, 0.56))
        sleep(2)
    except:
        pass
    sleep(4)
    
    try:
    # 立即预约
        click('obj_1610700786994.jpg', position=(0.34, 0.404, 0.653, 0.454), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        click_text('立即预约')
    sleep(4)


    try:
        # 关闭弹窗
        click('/text="关闭" && type="android.view.View"', xOffset=0, yOffset=0, by=DriverType.UIAUTOMATOR, timeOut=20)
    except:
        click('obj_1610694356594.jpg', xOffset=-0.003,yOffset=-0.042, position=(0.921, 0.269, 0.988, 0.303))
    sleep(3)
    

    try:
        slide((0.766, 0.835), (0.805, 0.369))
    except:
        logger.info('滑动')
    sleep(4)

    try:
        click('obj_1610698118723.jpg', position=(0.438, 0.342, 0.544, 0.39), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        click((0.489, 0.358), position=None)
    sleep(4)

    try:
        # 关闭弹窗
        click('/text="关闭" && type="android.view.View"', xOffset=0, yOffset=0, by=DriverType.UIAUTOMATOR, timeOut=20)
    except:
        click('obj_1610694356594.jpg', xOffset=-0.003,yOffset=-0.042, position=(0.921, 0.269, 0.988, 0.303))
    sleep(3)

    try:
        slide((0.638, 0.607), (0.602, 0.262))
        sleep(2)
        slide((0.59, 0.727), (0.596, 0.56))
        sleep(2)
    except:
        pass
    sleep(4)    
    
    try:
        # 未完成
        click('obj_1610698210796.jpg', position=(0.693, 0.656, 0.957, 0.696), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        click_text('未完成')
    sleep(4)
    try:
        # 关闭弹窗
        click('/text="关闭" && type="android.view.View"', xOffset=0, yOffset=0, by=DriverType.UIAUTOMATOR, timeOut=20)
    except:
        click('obj_1610694356594.jpg', xOffset=-0.003,yOffset=-0.042, position=(0.921, 0.269, 0.988, 0.303))
    sleep(3)
    
    try:
        click((0.948, 0.245), position=None)
        click((0.985, 0.279), position=None)
    except:
        click('obj_1610704004775.jpg', position=(0.927, 0.269, 0.988, 0.303), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    sleep(5)

    try:
        # 滑动至活动规则
        slide((0.653, 0.815), (0.729, 0.1))
        slide((0.653, 0.815), (0.729, 0.1))
        slide((0.653, 0.815), (0.729, 0.1))
        slide((0.653, 0.815), (0.729, 0.1))
    except:
        logger.info('滑动至活动规则')
    sleep(18)

    try:
        slide((0.632, 0.248), (0.556, 0.927))
        slide((0.596, 0.369), (0.559, 0.822))
        slide((0.578, 0.283), (0.62, 0.891))
        slide((0.608, 0.386), (0.605, 0.564))
    except:
        pass
    sleep(12)
'''