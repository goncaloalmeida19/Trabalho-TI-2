from HuffmanCodec import HuffmanCodec as huffman
#tam da tabela - simbolos - comprimento - numero de bytes
with open("..\dataset\\bible.txt", "r") as file:
    linha = file.read()
    codec = huffman.from_data(linha)
    # Code table is dictionary mapping symbol to (bitsize, value)
    code_table = huffman.get_code_table(codec)
    print(code_table)
    #print(linha)
    #compresso = codec.encode(linha)
    #print(compresso)
    #print(codec.decode(compresso))
    #print(code_table)