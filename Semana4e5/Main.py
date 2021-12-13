# ppm https://github.com/nayuki/Reference-arithmetic-coding/tree/master/python
import bz2
import lzma
import os

import pyppmd
import HuffmanCodec

import LZW as lzw
from Semana4e5 import Deflate


def huffman_encoding(data):
    encoded_text = HuffmanCodec.encode(data)
    compressed_data = bytearray()
    for i in range(0, len(encoded_text), 8):
        compressed_data.append(int(encoded_text[i:i + 8], 2))
    decompressed_data = HuffmanCodec.decode(encoded_text)
    print("Huffman:", decompressed_data == data)  # True
    return compressed_data, decompressed_data


def bzip(data):
    compressed_data = bz2.compress(data.encode())
    decompressed_data = bz2.decompress(compressed_data)
    str_decompressed_data = decompressed_data.decode()
    # print(str_decompressed_data)
    print("Bzip2:", str_decompressed_data == data)  # True
    return compressed_data, decompressed_data


def lzma_encoding(data):
    compressed_data = lzma.compress(str.encode(data))
    decompressed_data = lzma.decompress(compressed_data)
    str_decompressed_data = decompressed_data.decode()
    # print(str_decompressed_data)
    print("LZMA:", str_decompressed_data == data)  # True
    return compressed_data, decompressed_data


def lzw_encoding(data):
    compressed_data = lzw.compress(data)
    # decompressed_data = lzw.decompress(compressed_data)
    # print(decompressed_data == data)  # True
    # return compressed_data, decompressed_data
    return compressed_data


def ppm_encoding(data):
    compressed_data = pyppmd.compress(data.encode())
    decompressed_data = pyppmd.decompress(compressed_data).decode()
    print("PPM:", decompressed_data == data)  # True
    return compressed_data, decompressed_data


def deflate_encoding(data):
    compressed_data = Deflate.deflate(data.encode())
    decompressed_data = Deflate.inflate(compressed_data)
    str_decompressed_data = decompressed_data.decode()
    print("Deflate:", str_decompressed_data == data)  # True
    return compressed_data, decompressed_data


def get_ratio(original, compressed):
    original_size = os.path.getsize(original)
    compressed_size = os.path.getsize(compressed)
    compression_percent = round(100 - compressed_size / original_size * 100, 2)
    print(f"Tamanho do original: {original_size} bytes / Tamanho do comprimido: {compressed_size} bytes / "
          f"Ratio de compressão: {compression_percent}%")


data_type = [".txt", ".csv", ".js", ".txt"]
filenames = ["bible", "finance", "jquery-3.6.0", "random"]
compression_type = [".bzip2", ".lzma", ".lzw", ".huffman", ".ppm", ".deflate"]
for i in range(len(filenames)):
    j = 0
    read_path = "..\dataset\\" + filenames[i] + data_type[i]
    with open(read_path, "r") as file:
        data = file.read()
        write_path = "..\compressed_dataset\\" + filenames[i]
        compressed_data_bzip, decompressed_data_bzip = bzip(data)
        with open(write_path + compression_type[j], "wb") as write_file:
            write_file.write(compressed_data_bzip)
        get_ratio(read_path, write_path + compression_type[j])
        compressed_data_lzma, decompressed_data_lzma = lzma_encoding(data)
        j += 1
        with open(write_path + compression_type[j], "wb") as write_file:
             write_file.write(compressed_data_lzma)
        get_ratio(read_path, write_path + compression_type[j])
        # compressed_data_lzw, decompressed_data_lzw = lzw_encoding(data)
        #compressed_data_lzw = lzw_encoding(data)
        j += 1
        #with open(write_path + compression_type[j], "wb") as write_file:
        #    write_file.write(compressed_data_lzw.encode())
        compressed_data_huffman, decompressed_data_huffman = huffman_encoding(data)
        j += 1
        with open(write_path + compression_type[j], "wb") as write_file:
            write_file.write(compressed_data_huffman)
        get_ratio(read_path, write_path + compression_type[j])
        compressed_data_ppm, decompressed_data_ppm = ppm_encoding(data)
        j += 1
        with open(write_path + compression_type[j], "wb") as write_file:
            write_file.write(compressed_data_ppm)
        get_ratio(read_path, write_path + compression_type[j])
        compressed_data_deflate, decompressed_data_deflate = deflate_encoding(data)
        j += 1
        with open(write_path + compression_type[j], "wb") as write_file:
            write_file.write(compressed_data_deflate)
        get_ratio(read_path, write_path + compression_type[j])