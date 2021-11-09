import os
import zipfile
import sys

"""
import shutil, os, send2trash
・shutil.copy(A, B)
ファイルAをパスBへコピー、Bにファイル名を含めることでファイル名の変更も同時に可能
・shutil.copytree(A, B)
フォルダAをフォルダBという名前とパスでコピー（新規作成）
・shutil.move(A, B)
ファイルAをパスBへ移動、Bにファイル名を含めることでファイル名の変更も同時に可能
・os.unlink(path)
pathに指定したファイルを削除
・os.rmdir(path)
pathに指定したフォルダを削除、フォルダは空である必要がある
・shutil.rmtree(path)
pathに指定したフォルダを削除し、その中のファイルやフォルダも全て削除する
・send2trash.send2trash(path)
pathに指定したファイルをゴミ箱へ移動
"""

# os.walk(path)
if not os.path.exists(r".\chapter9.py"):
    print("chapter9.pyがあるフォルダに移動して！")
    sys.exit()

for walk, folders in enumerate(os.walk(".")):
    foldername, subfolders, filenames = folders[0], folders[1], folders[2]
    print("walk", walk + 1)
    print("The current folder is " + foldername)

    for subfolder in subfolders:
        print("subfolder of " + foldername + ":   " + subfolder)

    for filename in filenames:
        print("file inside " + foldername + ":   " + filename)

    print()

# zipファイルの取り扱い
# 圧縮するアルゴリズム（compress_type）には、zipfile.ZIP_DEFLATED を指定すれば間違いは少ない
new_zip = zipfile.ZipFile("new.zip", "w")  # zipファイルの作成
new_zip.write(r"delicious\cats\catnames.txt",
              compress_type=zipfile.ZIP_DEFLATED)
new_zip.close()
new_zip = zipfile.ZipFile("new.zip", "a")  # zipファイルにファイルの追加
new_zip.write(r"delicious\walnut\waffles\butter.txt",
              compress_type=zipfile.ZIP_DEFLATED)
new_zip.close()
# zipファイルの中身を参照する際には、パスのセパレーターに / を使用しないと何故か上手く読み込めない
new_zip = zipfile.ZipFile("new.zip")  # zipファイルの読み込み、デフォルト
print(new_zip.namelist())  # zipファイル内のすべてのファイルとフォルダを文字列のリストとして返す
# ZipInfoオブジェクトの取得
size_info = new_zip.getinfo(r"delicious/walnut/waffles/butter.txt")
print(size_info.file_size)  # 元のファイルサイズ
print(size_info.compress_size)  # 圧縮後のファイルサイズ
new_zip.close()
new_zip = zipfile.ZipFile("new.zip")
# 一部のファイルだけを場所を指定して展開可能
new_zip.extract(r"delicious/cats/catnames.txt", r"extract")
new_zip.extract(r"delicious/walnut/waffles/butter.txt", r"extract")
new_zip.extractall()  # 全展開
new_zip.close()

with zipfile.ZipFile("new2.zip", "w") as new2_zip:
    new2_zip.write(r"delicious\cats\catnames.txt",
                   compress_type=zipfile.ZIP_DEFLATED)
with zipfile.ZipFile("new2.zip", "a") as new2_zip:
    new2_zip.write(r"delicious\walnut\waffles\butter.txt",
                   compress_type=zipfile.ZIP_DEFLATED)
with zipfile.ZipFile("new2.zip") as new2_zip:
    print(new2_zip.namelist())
    size_info = new2_zip.getinfo(r"delicious/walnut/waffles/butter.txt")
    print(size_info.file_size)
    print(size_info.compress_size)
with zipfile.ZipFile("new2.zip") as new2_zip:
    new2_zip.extract(r"delicious/cats/catnames.txt", r"extract2")
    new2_zip.extract(r"delicious/walnut/waffles/butter.txt", r"extract2")
    new2_zip.extractall()
