import bz2

with open("..\dataset\\bible.txt", 'rb') as file:
    data = file.read()
    compressed_data = bz2.compress(data)
    with open("..\compressed_dataset\\bible.bzip2", "wb") as write_file:
        write_file.write(compressed_data)
    decompressed_data = bz2.decompress(compressed_data)
    str_decompressed_data = decompressed_data.decode()
    print(str_decompressed_data)
    with open("..\compressed_dataset\\bible2.txt", "w") as write_file:
        write_file.write(str_decompressed_data)
    print(str_decompressed_data == data)  # True