'''/*
 * @Author: Shawn Zhang 
 * @Date: 2019-08-28 19:49:16 
 * @Last Modified by:   Shawn Zhang 
 * @Last Modified time: 2019-08-28 19:49:16 
 */
 '''
# 加载numpy
try:
    import numpy as np
except ImportError:
    print('导入numpy出错')
    np=None

# 导入urllib
try:
    import urllib
    from urllib import request
except ImportError:
    print('导入urllib出错')
    request=None
try:
    from urllib.error import URLError
except ImportError:
    URLError=None

#导入opencv
try:
    import cv2
except ImportError:
    print('导入cv2出错')
    cv2=None

import os

import base64
import binascii
try:
    import validators
except ImportError:
    print('导入validators出错')
    validators=None

from .imgloadexception import ImageLoadError

class ImageLoad():
    """image加载工具类"""
    # def __init__(self):
    #     pass

    @staticmethod
    def loadImgfromUrl(url):
        '''从url中加载图片
        :param url: 图像的url地址
        :return: 表示图像的numpy array
        :rtype: numpy array
        '''
        try :
            opener=request.build_opener()
            opener.open(url)
        except urllib.error.HTTPError:
            raise ImageLoadError('url指向的不是一个有效的图片链接')
        except urllib.error.URLError:
            raise ImageLoadError('url指向的不是一个有效的图片链接')
        try:
            resp=request.urlopen(url)
        except URLError as e:
            raise ImageLoadError(e.reason)
        image = np.asarray(bytearray(resp.read()), np.uint8)
        img = cv2.imdecode(image, cv2.IMREAD_UNCHANGED)
        if img is None:
            raise ImageLoadError('url指向的不是一个有效的图片链接')
        return img
    

    @staticmethod
    def loadImgfromFile(file):
        '''从request的file中加载图片
        :param file: request的file
        :return: 表示图像的numpy array
        :rtype: numpy array
        '''
        # with open(file, 'r') as f:
        #     try:
        #         fileStr=f.read()
        #     except:
        #         raise ImageLoadError('文件读取失败')
        #     f.close()
        # image = np.fromstring(fileStr, np.uint8)
        # image = cv2.imdecode(image,cv2.IMREAD_UNCHANGED)
        image = cv2.imread(file, cv2.IMREAD_UNCHANGED)
        if image is None:
            raise ImageLoadError('image文件不是一个有效的图片文件')
        return image
    
    @staticmethod
    def loadImgfromBase64String(base64_str):
        '''从base64字符串中加载图像
        :param base64_str: base64字符串
        :return: 表示图像的numpy array
        :rtype: numpy array
        '''
        # 有些转码工具会在base64字符前添加头信息如data:image/jpeg;base64，需要过滤掉
        if ',' in base64_str:
            base64_str=base64_str.split(',')[1]
        try:
            imageData=base64.b64decode(base64_str)
        except binascii.Error:
            raise ImageLoadError('不是一个有效的Base64字符串')
        image = np.fromstring(imageData, np.uint8)
        img = cv2.imdecode(image, cv2.IMREAD_UNCHANGED)
        if img is None:
            raise ImageLoadError('Base64字符串不是一个有效的图片')
        return img
    
    @staticmethod
    def checkifStringIsBase64Encode(base64_str):
        """检查string是否是base64"""
        if ',' in base64_str:
            base64_str=base64_str.split(',')[1]
        try:
            data = base64.b64decode(base64_str)
        except binascii.Error:
            return False
        return True
    
    @staticmethod
    def base64EncodeImage(image, with_base64_header=False, file_ext='jpg'):
        """将图像编码为base64的字符串
        @参数:
            image: 要进行编码的图片，numpy array
            file_ext: 文件后缀名，默认参数为jpg
            with_base64_header: 返回的字符串是否带base64的说明头
        @返回值
            图标进行base64编码之后的字符串
        """
        try:
            imageData = cv2.imencode('.'+file_ext, image)
        except cv2.error:
            raise ImageLoadError('文件后缀名不正确')            
        base64_str = imageData[1].tostring()
        base64_str = base64.b64encode(base64_str).decode()
        if with_base64_header:
            base64_str = "data:image/"+file_ext+";base64,"+base64_str
        return base64_str

    @staticmethod
    def loadImage(img_ref):
        """url、base64、file不做区分加载
        :param img_ref: 图片参数
        :return: 表示图像的numpy array
        :rtype: numpy array
        """
        image=None
        if os.path.isfile(img_ref):
            try:
               image = ImageLoad.loadImgfromFile(img_ref)
            except ImageLoadError as e:
                raise ImageLoadError(e.reason)
        elif isinstance(img_ref, str) and img_ref != '':
            if validators.url(img_ref):
                try:
                    image = ImageLoad.loadImgfromUrl(img_ref)
                except ImageLoadError as e:
                    raise ImageLoadError(e.reason)
            elif ImageLoad.checkifStringIsBase64Encode(img_ref):
                try:
                    image = ImageLoad.loadImgfromBase64String(img_ref)
                except ImageLoadError as e:
                    raise ImageLoadError(e.reason)
            else:
                raise ImageLoadError('参数既不是一个有效的url，也不是一个有效的base64字符')
        else:
            raise ImageLoadError('参数只能是图片文件、图片的base64编码字符串或者指向图片的url')
        return image

        



