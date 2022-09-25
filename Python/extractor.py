import os
import mmap

with open('bloodstone.spr', 'rb') as f:
    png_header = b'\x89\x50\x4E\x47\x0D\x0A\x1A'
    png_end = b'\x49\x45\x4E\x44\xAE\x42\x60\x82'

    mm = mmap.mmap(f.fileno(), length=0, access=mmap.ACCESS_READ)
    offset_start = mm.find(png_header)

    i = 1
    while offset_start >= 0:
        eof = mm.find(png_end, offset_start)

        if eof < 0:
            break

        with open(os.path.join('sprites', "{}.png".format(i)), "wb") as png_file:
            # Write data to .png file
            png_file.write(mm[offset_start:eof+len(png_end)])

        mm.seek(eof)
        offset_start = mm.find(png_header, eof)

        i += 1