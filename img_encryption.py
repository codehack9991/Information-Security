# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 10:25:30 2019

"""

from PIL import Image
from Crypto.Cipher import DES

filename = "hp.bmp"
format = "BMP"
filenameout = "hp1"
key = "aabbccdd"

def pad(data):
    return data + b"\x00"*(8-len(data)%8)

def convert_to_RGB(data):

    r, g, b = tuple(map(lambda d: [data[i] for i in range(0,len(data)) if i % 3 == d], [0, 1, 2]))
    pixels = tuple(zip(r,g,b))
    return pixels

def process_image(filename):
    im = Image.open(filename)
    data = im.convert("RGB").tobytes()
    original = len(data)

    new = convert_to_RGB(des_cbc_encrypt(key, pad(data))[:original])
    im2 = Image.new(im.mode, im.size)
    im2.putdata(new)
    im2.save(filenameout+"_cbc."+format, format)

    new = convert_to_RGB(des_ecb_encrypt(key, pad(data))[:original])
    im2 = Image.new(im.mode, im.size)
    im2.putdata(new)
    im2.save(filenameout+"_ecb."+format, format)

# CBC
def des_cbc_encrypt(key, data):
    IV = b"A"*8
    des = DES.new(key)
    i=0
    new_data=b""
    while i<len(data):
        IV = bytes(x ^ y for x, y in zip(IV, data[i:i+8]))
        IV = des.encrypt(IV)
        new_data = new_data+IV
        i=i+8
    return new_data
# ECB
def des_ecb_encrypt(key, data):
    des = DES.new(key)
    new_data = des.encrypt(data)
    return new_data

process_image(filename)