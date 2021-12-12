# ppm https://github.com/nayuki/Reference-arithmetic-coding/tree/master/python

import bz2
import lzma
import pyppmd

from HuffmanCodec import HuffmanCodec as huffman
import LZW as lzw
from Semana4e5 import PPM, Deflate


def huffman_coding(data):
    codec = huffman.from_data(data)
    # Code table is dictionary mapping symbol to (bitsize, value)
    code_table = huffman.get_code_table(codec)
    # print(code_table)


def bzip(data):
    compressed_data = bz2.compress(data.encode())
    decompressed_data = bz2.decompress(compressed_data)
    str_decompressed_data = decompressed_data.decode()
    # print(str_decompressed_data)
    print(str_decompressed_data == data)  # True
    return compressed_data, decompressed_data


def lzma_encoding(data):
    compressed_data = lzma.compress(str.encode(data))
    decompressed_data = lzma.decompress(compressed_data)
    str_decompressed_data = decompressed_data.decode()
    # print(str_decompressed_data)
    print(str_decompressed_data == data)  # True
    return compressed_data, decompressed_data


def lzw_encoding(data):
    compressed_data = lzw.compress(data)
    decompressed_data = lzw.decompress(compressed_data)
    print(decompressed_data == data)  # True
    return compressed_data, decompressed_data


def ppmd_encoding(data):
    compressed_data = pyppmd.compress(data.encode())
    decompressed_data = pyppmd.decompress(compressed_data).decode()
    print("ppmd", decompressed_data == data)  # True
    return compressed_data, decompressed_data


def deflate_encoding(data):
    compressed_data = Deflate.deflate(data.encode())
    decompressed_data = Deflate.inflate(compressed_data)
    str_decompressed_data = decompressed_data.decode()
    print(str_decompressed_data == data)  # True
    return compressed_data, decompressed_data


data_type = [".txt", ".csv", ".js", ".txt"]
filenames = ["bible", "finance", "jquery-3.6.0", "random"]
for i in range(len(filenames)):
    with open("..\dataset\\" + filenames[i] + data_type[i], "r") as file:
        data = file.read()
        compressed_data_bzip, decompressed_data_bzip = bzip(data)
        with open("..\compressed_dataset\\" + filenames[i] + ".bzip2", "wb") as write_file:
            write_file.write(compressed_data_bzip)
        compressed_data_lzma, decompressed_data_lzma = lzma_encoding(data)
        with open("..\compressed_dataset\\" + filenames[i] + ".lzma", "wb") as write_file:
            write_file.write(compressed_data_lzma)
        compressed_data_lzw, decompressed_data_lzw = lzw_encoding(data)
        with open("..\compressed_dataset\\" + filenames[i] + ".lzw", "w") as write_file:
            listToStr = ' '.join([str(elem) for elem in compressed_data_lzw])
            write_file.write(listToStr)
        # compressed_data_hf, decompressed_data_hf = huffman_coding(data)
        # with open("..\compressed_dataset\\" + filenames[i] + ".hf", "wb") as write_file:
        #     write_file.write(compressed_data_hf)
        compressed_data_ppmd, decompressed_data_ppmd = ppmd_encoding(data)
        with open("..\compressed_dataset\\" + filenames[i] + ".ppmd", "wb") as write_file:
            write_file.write(compressed_data_ppmd)
        compressed_data_deflate, decompressed_data_deflate = deflate_encoding(data)
        with open("..\compressed_dataset\\" + filenames[i] + ".deflate", "wb") as write_file:
            write_file.write(compressed_data_deflate)
