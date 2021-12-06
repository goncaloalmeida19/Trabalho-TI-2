import bz2
import lzma

from HuffmanCodec import HuffmanCodec as huffman


def huffman_coding(data):
    codec = huffman.from_data(data)
    # Code table is dictionary mapping symbol to (bitsize, value)
    code_table = huffman.get_code_table(codec)
    # print(code_table)


def bzip(data):
    compressed_data = bz2.compress(data.encode())
    with open("..\compressed_dataset\\bible.bzip2", "wb") as write_file:
        write_file.write(compressed_data)
    decompressed_data = bz2.decompress(compressed_data)
    str_decompressed_data = decompressed_data.decode()
    # print(str_decompressed_data)
    print(str_decompressed_data == data)  # True


def lzma_encoding(data):
    compressed_data = lzma.compress(str.encode(data))
    with open("..\compressed_dataset\\bible.lzma", "wb") as write_file:
        write_file.write(compressed_data)
    decompressed_data = lzma.decompress(compressed_data)
    str_decompressed_data = decompressed_data.decode()
    # print(str_decompressed_data)
    print(str_decompressed_data == data)  # True


filenames = ["bible.txt", "finance.csv", "jquery-3.6.0.js", "random.txt"]
for i in filenames:
    with open("..\dataset\\" + i, "r") as file:
        data = file.read()
        bzip(data)
        lzma_encoding(data)

        huffman_coding(data)