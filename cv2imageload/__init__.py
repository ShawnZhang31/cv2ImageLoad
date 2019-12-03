'''
/*
 * @Author: Shawn Zhang
 * @Date: 2019-09-01 10:18:54
 * @Last Modified by: Shawn Zhang
 * @Last Modified time: 2019-09-01 11:09:18
 */
 '''
__version__ = '1.0.5'
name = 'cv2ImageLoad'

from .imgload import ImageLoad
from .imgloadexception import ImageLoadError

__all__=[ImageLoad, ImageLoadError]
