import os
import shelve
import sys
"""
プレーンテキストを読み書きする基本手順
1. open()関数を呼び出し、Fileオブジェクトを取得する
2. Fileオブジェクトのread()やwrite()メソッドを呼び出して読み書きする
3. Fileオブジェクトのclose()オブジェクトを呼び出してファイルを閉じる
"""
if not os.path.isfile(r".\chapter8.py"):
    print("chapter8.pyがあるフォルダに移動して！")
    sys.exit()

bacon_file = open("bacon.txt", "w")  # 書き込みモード、上書きであることに注意
bacon_file.write("Hello world!\n")
bacon_file.close()
bacon_file = open("bacon.txt", "a")  # 追記モード
bacon_file.write("Bacon is not a vegetable.")
bacon_file.close()
bacon_file = open("bacon.txt")  # デフォルトでは、読み込み（r）モード
content = bacon_file.read()  # read()やraadlines()で読み込んだ後は、オブジェクトの中身がなくなるようだ
content_line = bacon_file.readlines()
bacon_file.close()
print(content)
print(content_line)

with open("egg.txt", "w") as egg_file:
    egg_file.write("Hello world!\n")
with open("egg.txt", "a") as egg_file:
    egg_file.write("Egg is not a vegetable.")
with open("egg.txt") as egg_file:
    content = egg_file.read()
with open("egg.txt") as egg_file:
    content_line = egg_file.readlines()
print(content)
print(content_line)

# shelveモジュールによる変数の保存
shelf_file = shelve.open("mydata")  # ないものを指定すると新規作成される
cats = ["Zophie", "Pooka", "Simon"]
shelf_file["cats"] = cats
shelf_file.close()
shelf_file = shelve.open("mydata")
print(type(shelf_file))
print(shelf_file["cats"])
print(list(shelf_file.keys()))
print(list(shelf_file.values()))
shelf_file.close()

# 以下はpythonによるファイルとファイルパスの取り扱い
# OSに依存する区切り文字でつないだ正しいパスを文字列で返す
print(os.path.join("usr", "bin", "spam", "filename"))

# カレントディレクトリの取得
cwd = os.getcwd()
print(cwd)

# チェンジディレクトリ
os.chdir(r"C:\Windows\System32")
print(os.getcwd())
os.chdir(cwd)

# 新規フォルダの作成
delicious_path = r".\delicious\walnut\waffles"
if not os.path.exists(delicious_path):
    os.makedirs(delicious_path)

# 引数に渡したパスの絶対パスを文字列として返す
print(os.path.abspath("."))

# 引数が絶対パスならTrue, 相対パスならFalse
print(os.path.isabs("."))
print(os.path.isabs(os.path.abspath(".")))

# startからpathへの相対パスを文字列として返す
# os.path.relpath(path, start)
print(os.path.relpath(r"C:\Windows", r"C:\\"))
print(os.path.relpath(r"C:\Windows", r".\delicious\walnut\waffles"))

# os.path.basename(), os.path.dirname(), os.path.split()
path = r"C:\Windows\System32\calc.exe"
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.split(path))

# os.sepはプログラムを実行しているOSにおけるパス区切り文字が格納されている
# 文字列のsplit()メソッドと組み合わせて、パスを個々のフォルダまで分割する
print(path.split(os.sep))

# ファイルサイズの取得
print(os.path.getsize(r".\chapter8.py"))
print(os.path.getsize("."))  # 何のサイズが返却されているか不明

# 引数に指定したパスに含まれるファイル名とフォルダ名のリストを取得
print(os.listdir("."))

# パスの検査
print(os.path.exists(r"C:\Windows"))  # 引数に指定したファイルやフォルダが存在すればTrue
print(os.path.exists(r"C:\some_made_up_folder"))
print(os.path.isdir(r"C:\Windows\System32"))  # 引数に指定した先が存在し、それがフォルダであればTrue
print(os.path.isfile(r"C:\Windows\System32"))  # 引数に指定した先が存在し、それがフォルダであればTrue
print(os.path.isdir(r".\chapter8.py"))
print(os.path.isfile(r".\chapter8.py"))
