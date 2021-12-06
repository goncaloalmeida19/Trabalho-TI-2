import bz2
import lzma

from HuffmanCodec import HuffmanCodec as huffman
import LZW as lzw


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
    compressed_data = lzw.compress(data.encode)
    decompressed_data = lzw.decompress(compressed_data)
    str_decompressed_data = decompressed_data.join()
    print(str_decompressed_data == data)  # True
    return compressed_data, decompressed_data


data_type = [".txt", ".csv", ".js", ".txt"]
filenames = ["bible", "finance", "jquery-3.6.0", "random"]
for i in range(len(filenames)):
    with open("..\dataset\\" + filenames[i] + data_type[i], "r") as file:
        data = file.read()
        compressed_data, decompressed_data = bzip(data)
        with open("..\dataset\\" + filenames[i] + ".bzip", "wb") as write_file:
            write_file.write(compressed_data)
        lzma_encoding(data)
        with open("..\dataset\\" + filenames[i] + ".lzma", "wb") as write_file:
            write_file.write(compressed_data)
        lzw_encoding(data)
        with open("..\dataset\\" + filenames[i] + ".lzw", "wb") as write_file:
            write_file.write(compressed_data)
        huffman_coding(data)