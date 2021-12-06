import lzma

with open("..\dataset\\bible.txt", "r") as file:
    data = file.read()
    compressed_data = lzma.compress(str.encode(data))
    with open("..\compressed_dataset\\bible.lzma", "wb") as write_file:
        write_file.write(compressed_data)
    decompressed_data = lzma.decompress(compressed_data)
    str_decompressed_data = decompressed_data.decode()
    print(str_decompressed_data)
    print(str_decompressed_data == data)  # True