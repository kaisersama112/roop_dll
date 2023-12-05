#!/usr/bin/env python3

from roop import core

if __name__ == '__main__':
    core.run()



"""
只用CPU处理视频:python run.py
使用GPU处理视频:python run.py --execution-provider cuda  
图片保存jpg格式:python run.py --execution-provider cuda --temp-frame-format jpg
视频高清化处理:python run.py --execution-provider cuda --temp-frame-format jpg --frame-processor face_swapper face_enhancer 
处理脸部跳闪:python run.py --execution-provider cuda --temp-frame-format jpg --frame-processor face_swapper face_enhancer --similar-face-distance 1.5
"""
