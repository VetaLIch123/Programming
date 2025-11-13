import os
import shutil
from pathlib import Path

base_dir = Path("folder_1")

folder_2 = base_dir / "folder_2"
folder_3 = base_dir / "folder_3"
folder_4 = base_dir / "folder_4"

print("Вміст каталогу folder_1 і підкаталогів:\n")
for root, dirs, files in os.walk(base_dir):
    level = root.replace(str(base_dir), "").count(os.sep)
    indent = " " * 4 * level
    print(f"{indent}{os.path.basename(root)}/")
    for file in files:
        print(f"{indent}    {file}")

folder_4.mkdir(exist_ok=True)
print("\nПідкаталог folder_4 створено (або вже існує).")

for file in folder_2.glob("*.pdf"):
    shutil.copy(file, folder_4)
print("Файли *.pdf скопійовано з folder_2 у folder_4.")

for file in folder_2.glob("*.docx"):
    shutil.move(str(file), folder_4)
print("Файли *.docx переміщено з folder_2 у folder_4.")

for file in folder_2.glob("*.pdf"):
    new_name = file.stem + "_2024" + file.suffix
    file.rename(file.with_name(new_name))
print("Файли *.pdf у folder_2 перейменовано (додано _2024).")

for file in folder_2.glob("*"):
    if file.is_file() and file.stat().st_size > 100 * 1024:
        file.unlink()
print("Видалено файли у folder_2, більші за 100 КБ.")

if folder_3.exists():
    shutil.rmtree(folder_3)
    print("Підкаталог folder_3 видалено.")
else:
    print("Підкаталог folder_3 не знайдено.")
