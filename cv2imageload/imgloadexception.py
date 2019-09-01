'''
/*
 * @Author: Shawn Zhang 
 * @Date: 2019-08-28 20:39:12 
 * @Last Modified by: Shawn Zhang
 * @Last Modified time: 2019-08-28 22:37:35
 */
'''

class ImageLoadError(Exception):
    """图片加载的异常"""
    def __init__(self, reason):
        self.reason=reason