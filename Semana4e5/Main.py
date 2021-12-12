# ppm https://github.com/nayuki/Reference-arithmetic-coding/tree/master/python
import bz2
import lzma
import pyppmd
import HuffmanCodec

import LZW as lzw
from Semana4e5 import Deflate


def huffman_encoding(data):
    encoded_text = HuffmanCodec.encode(data).encode()
    decompressed_data = HuffmanCodec.decode(encoded_text)
    print(decompressed_data == data, "Huffman")  # True
    return encoded_text, decompressed_data


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
    # decompressed_data = lzw.decompress(compressed_data)
    # print(decompressed_data == data)  # True
    # return compressed_data, decompressed_data
    return compressed_data


def ppmd_encoding(data):
    compressed_data = pyppmd.compress(data.encode())
    decompressed_data = pyppmd.decompress(compressed_data).decode()
    print(decompressed_data == data)  # True
    return compressed_data, decompressed_data


def deflate_encoding(data):
    compressed_data = Deflate.deflate(data.encode())
    decompressed_data = Deflate.inflate(compressed_data)
    str_decompressed_data = decompressed_data.decode()
    print(str_decompressed_data == data)  # True
    return compressed_data, decompressed_data


data_type = [".txt", ".csv", ".js", ".txt"]
filenames = ["bible", "finance", "jquery-3.6.0", "random"]
compression_type = [".bzip2", ".lzma", ".lzw", ".huffman", ".ppm", ".deflate"]
for i in range(len(filenames)):
    j = 0
    with open("..\dataset\\" + filenames[i] + data_type[i], "r") as file:
        data = file.read()
        write_path = "..\compressed_dataset\\" + filenames[i]
        compressed_data_bzip, decompressed_data_bzip = bzip(data)
        with open(write_path + compression_type[j], "wb") as write_file:
            write_file.write(compressed_data_bzip)
        compressed_data_lzma, decompressed_data_lzma = lzma_encoding(data)
        j += 1
        with open(write_path + compression_type[j], "wb") as write_file:
             write_file.write(compressed_data_lzma)
        # compressed_data_lzw, decompressed_data_lzw = lzw_encoding(data)
        #compressed_data_lzw = lzw_encoding(data)
        j += 1
        #with open(write_path + compression_type[j], "wb") as write_file:
        #    write_file.write(compressed_data_lzw.encode())
        compressed_data_huffman, decompressed_data_huffman = huffman_encoding(data)
        j += 1
        with open(write_path + compression_type[j], "wb") as write_file:
            write_file.write(compressed_data_huffman)
        compressed_data_ppmd, decompressed_data_ppmd = ppmd_encoding(data)
        j += 1
        with open(write_path + compression_type[j], "wb") as write_file:
            write_file.write(compressed_data_ppmd)
        compressed_data_deflate, decompressed_data_deflate = deflate_encoding(data)
        j += 1
        with open(write_path + compression_type[j], "wb") as write_file:
            write_file.write(compressed_data_deflate)
