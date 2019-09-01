import pytest
from cv2imageload import ImageLoad, ImageLoadError

@pytest.mark.parametrize('files',[
    # 'files/th-108.jpeg',
    'files/th-108.jpg',
    'files/th-108.png',
    'files/th-109.jpeg',
    # 'files/face.obj',
])

def test_load_image_successfully(files):
    image = ImageLoad.loadImage(files)
    assert image !=None