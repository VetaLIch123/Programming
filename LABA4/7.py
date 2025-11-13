import string

data = b"t\n\xd4G\xde\xe5\xb3\x98\xd6\xe4\xa6\xaeWU\x93\x8d\xc9O\xab?\x8fj\xa5#\rMC[\xad\x0e\xb1\x04\xd4?\x02\xf1\xffd+\x99J\xa1\xaf\xe9b\xaetx0\xf0\xc4\xc8`'\x15"

def hexdump(buf: bytes, width: int = 16) -> str:
    lines = []
    for off in range(0, len(buf), width):
        chunk = buf[off:off+width]
        hex_part = ' '.join(f'{b:02x}' for b in chunk)
        ascii_part = ''.join(chr(b) if chr(b) in string.printable and b >= 0x20 else '.' for b in chunk)
        lines.append(f'{off:08x}: {hex_part:<{width*3}}    {ascii_part}')
    return '\n'.join(lines)

def dehex(dump: str) -> bytes:
    out = bytearray()
    for line in dump.splitlines():
        if ':' not in line:
            continue
        _, rest = line.split(':', 1)
        hex_field = rest.strip().split('    ')[0]
        for token in hex_field.split():
            out.append(int(token, 16))
    return bytes(out)

# Demo
dump = hexdump(data)
print(dump)
restored = dehex(dump)
assert restored == data
