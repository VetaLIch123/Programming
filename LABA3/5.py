import struct

filename = 'bmp_20.bmp'

with open(filename, 'rb') as f:
    file_header = f.read(14)
    bfType, bfSize, bfReserved1, bfReserved2, bfOffBits = struct.unpack('<2sIHHI', file_header)

    print("=== BITMAPFILEHEADER ===")
    print(f"bfType: {bfType.decode()}")  # має бути 'BM'
    print(f"bfSize: {bfSize} байт")
    print(f"bfReserved1: {bfReserved1}")
    print(f"bfReserved2: {bfReserved2}")
    print(f"bfOffBits: {bfOffBits} (зміщення до пікселів)")

    info_header = f.read(40)
    (
        biSize, biWidth, biHeight, biPlanes, biBitCount,
        biCompression, biSizeImage, biXPelsPerMeter,
        biYPelsPerMeter, biClrUsed, biClrImportant
    ) = struct.unpack('<IIIHHIIIIII', info_header)

    print("\n=== BITMAPINFOHEADER ===")
    print(f"biSize: {biSize} байт")
    print(f"biWidth: {biWidth} пікселів")
    print(f"biHeight: {biHeight} пікселів")
    print(f"biPlanes: {biPlanes}")
    print(f"biBitCount: {biBitCount} бітів на піксель")
    print(f"biCompression: {biCompression}")
    print(f"biSizeImage: {biSizeImage} байт")
    print(f"biXPelsPerMeter: {biXPelsPerMeter}")
    print(f"biYPelsPerMeter: {biYPelsPerMeter}")
    print(f"biClrUsed: {biClrUsed}")
    print(f"biClrImportant: {biClrImportant}")