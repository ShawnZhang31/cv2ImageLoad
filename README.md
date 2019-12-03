# cv2ImageLoad
python cv2通过图片文件、图片url、图片的base64编码加载图片。[cv2ImageLoad](https://github.com/ShawnZhang31/cv2ImageLoad/blob/master/README.md)

## 安装
```
pip install cv2imageload
```
## 使用
```
from cv2imageload import ImageLoad, ImageLoadError

file = 'th-108.jpg'
url = 'http://*.com/test.png'
base64_str = '图片的base64编码字符串'

# 加载图片文件
try:
    image = ImageLoad.loadImage(file)
except ImageLoadError as e:
    print(e.reason)

# 加载url图片
try:
    image = ImageLoad.loadImage(url)
except ImageLoadError as e:
    print(e.reason)

# 加载base64编码的图片
try:
    image = ImageLoad.loadImage(base64_str)
except ImageLoadError as e:
    print(e.reason)

# 将图片编码为base64字符串
try:
    base64_str = ImageLoad.base64EncodeImage(image, with_base64_header=True, file_ext='jpg')
except ImageLoadError as error:
    print(error.reason)
print(base64_str[:30])

```
