import lzma


def compressor(s):
    t = lzma.LZMACompressor().compress(s)
    return t
