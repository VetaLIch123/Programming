dir = (
 "_file1.doc\n"
 "file2.pdf\n"
 "file222_.docx\n"
 "cmd.exe\n"
 "sys.dll\n"
 "FiLe7_5.txt\n"
 "foto1.jpg\n"
 "song1.mp3\n"
 "!!!song2.mp3\n"
 "video.avi\n"
 "file9.txt\n"
 "file_3_document.docx\n"
 "my_document!!!.ppt\n"
 "main.c\n"
 "lab3.py\n"
 "lookup.xml\n"
 "pic1.png\n"
 "pic2.bmp\n"
)
files = dir.strip().split('\n')

print("Початковий вміст каталогу")
for f in files:
    print(f"    {f}")

print(f"\nУ каталозі є {len(files)} файлів")

ext_a = ('.dll', '.mp3')
files_a = [f for f in files if f.lower().endswith(ext_a)]
print(f"Файлів з розширенням .dll або .mp3: {len(files_a)}")
for f in files_a:
    print(f"    {f}")

renamed = []
for f in files:
    if f.lower().endswith('.doc'):
        renamed.append(f[:-4] + '.py')
    else:
        renamed.append(f)

print("\nКаталог після заміни розширення .doc на .py")
for f in renamed:
    print(f"    {f}")

lowered = [f.lower() for f in renamed]
print("\nКаталог після приведення імен файлів до нижнього регістру")
for f in lowered:
    print(f"    {f}")

final = [f for f in lowered if not f.endswith('.py')]
print("\nКаталог після видалення файлів з розширенням .py")
for f in final:
    print(f"    {f}")
