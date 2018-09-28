# -*- coding: utf8 -*-
import struct


def decode(x):  # 如果按照正常算法得到的synchsafe integer，解析成 真正的整数大小
    a = x & 0xff
    b = (x >> 8) & 0xff
    c = (x >> 16) & 0xff
    d = (x >> 24) & 0xff
    x_final = 0x0
    x_final = x_final | a
    x_final = x_final | (b << 7)
    x_final = x_final | (c << 14)
    x_final = x_final | (d << 21)
    return x_final


def encode(x):  # 和上边相反
    a = x & 0x7f
    b = (x >> 7) & 0x7f
    c = (x >> 14) & 0x7f
    d = (x >> 21) & 0x7f

    x_final = 0x0
    x_final = x_final | a
    x_final = x_final | (b << 8)
    x_final = x_final | (c << 16)
    x_final = x_final | (d << 24)
    return x_final


def addImage(path, image):
    print("123")

    fp = open(path, 'rb')
    head = fp.read(10)
    try:
        id3, ver, revision, flag, length = struct.unpack("!3sBBBI", head)
    except:
        return False
    if id3 != 'ID3':
        return False
    # 新建立个文件
    fpNew = open(path + '.bak', "wb")
    fpImage = open(image, "rb")
    imageData = fpImage.read()  # 待用
    originLength = decode(length)  # 真实长度
    length = 0

    imageDataPre = struct.pack("!B10s2BB", 0, 'image/jpeg', 0, 0, 0)
    imageData = imageDataPre + imageData
    apicLen = len(imageData)  # 图片数据区域长度
    imageDataHead = struct.pack("!4sI2B", 'APIC', apicLen, 0, 0)
    imageData = imageDataHead + imageData

    # 新长度
    length += len(imageData)

    header = head[0:3]
    header += struct.pack('!B', 3)
    header += struct.pack('!H', 0)
    # 1字节留白
    header += struct.pack("!I", encode(length + 1))

    fpNew.write(header)
    print("ok")
    fpNew.write(imageData)
    fpNew.write(struct.pack('!B', 0))

    fp.seek(originLength, 1)  # 跳
    fpNew.write(fp.read())
    fpNew.close()
    fp.close()
    fpImage.close()


if __name__ == '__main__':
    addImage("D:\\code\\python\\python_study\\pyQT\\李荣浩 - 年少有为.mp3",
             "D:\\code\\python\\python_study\\pyQT\\李荣浩 - 年少有为.jpg")
