import hashlib
lat_low = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
hash = "d29896ef28a3cb46d4fbd6a048a4910bd9779a48574173c9d54a0b4253e85a8c"
symbols = numbers + lat_low
found = False
for t1 in symbols:
    for t2 in symbols:
        for t3 in symbols:
            for t4 in symbols:
                for t5 in symbols:
                    for t6 in symbols:
                        password = t1 + t2 + t3 + t4 + t5 + t6
                        gen_hash =  hashlib.sha256(password.encode()).hexdigest()
                        if gen_hash == hash:
                            print(password)
                            break
                    if found: break
                if found: break
            if found: break
        if found: break
    if found: break
if not found:
    print("No password found")