import os
import pathlib
from datetime import datetime

import ppmd


def ppmd_encoding(data, name_data):
    targetfile = pathlib.Path(data)
    fname = name_data
    ftime = datetime.utcfromtimestamp(targetfile.stat().st_mtime)
    archivefile = name_data + ".ppmd"
    order = 6
    mem_in_mb = 8
    with archivefile.open('wb') as target:
        with targetfile.open('rb') as src:
            with ppmd.PpmdCompressor(target, fname, ftime, order, mem_in_mb, version=8) as compressor:
                compressor.compress(src)
    return archivefile


def ppmd_decoding(name_compressed_data):
    targetfile = pathlib.Path(name_compressed_data)
    target_size = os.path.getsize(name_compressed_data)
    with targetfile.open('rb') as target:
        with ppmd.PpmdDecompressor(target, target_size) as decompressor:
            extractedfile = pathlib.Path(targetfile.joinpath(decompressor.filename))
    with extractedfile.open('wb') as ofile:
        decompressor.decompress(ofile)
    timestamp = ppmd.datetime_to_timestamp(decompressor.ftime)
    os.utime(str(extractedfile), times=(timestamp, timestamp))
