#!/usr/bin/env python
# -*- coding:utf-8 -*-

from PIL import Image;
png1 = Image.open("vape_nation.png");

print "vape_nation starting ...."

#创建一个和现有图片大小一样的图片
png2 = Image.new("RGBA",(png1.width,png1.height))
 
#读取像素中的rgb值,并提取出green通道的最低位的值
for x in range(0,png1.height):
    for y in range(0,png1.width):
        r,g,b = png1.getpixel((x,y))
         
        #根据最低位的值生成一个黑白的图片
        if g&1 == 1:
            png2.putpixel((x,y),(255,255,255))
        else:
            png2.putpixel((x,y),(0,0,0))
 
png2.show()
