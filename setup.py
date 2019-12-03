'''
/*
 * @Author: Shawn Zhang 
 * @Date: 2019-09-01 10:34:35 
 * @Last Modified by: Shawn Zhang
 * @Last Modified time: 2019-09-01 11:19:02
 */
'''
import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'cv2imageload',
    version = '1.0.5',
    author = 'Shawn Zhang',
    author_email = 'shawnzhang31@gmail.com',
    description = 'python cv2 load image from image file, url or base64 code of image',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/ShawnZhang31/cv2ImageLoad.git',
    packages = setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "opencv-contrib-python",
        "validators",
    ],
    python_requires='>=3.0',
)