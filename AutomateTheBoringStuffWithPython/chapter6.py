import pyperclip

print("6章 文字列操作")

print("isXという文字列メソッド")
print("hello".isalpha())  # 1文字以上の英数字だけから文字列が構成されている場合にTrue
print("hello123".isalpha())
print("hello123".isalnum())  # 1文字以上の英文字か数字から構成されている場合にTrue
print("hello".isalnum())
print("123".isdecimal())  # 1文字以上の数字だけから構成されている場合にTrue
print(" ".isspace())  # 文字列がスペースかタブか改行だけで構成されている場合にTrue
print("This Is Title Case".istitle())  # 大文字から始まり残りが全て小文字の英単語から構成されている場合にTrue
print("This Is Title Case 123".istitle())
print("This Is not Title Case".istitle())
print("This Is NOT Title Case Either".istitle())
print()

print("rjust(), ljust(), center()メソッド")
print("Hello".rjust(10))
print("Hello".rjust(20))
print("Hello World".rjust(20))
print("Hello".ljust(10))
print("Hello".rjust(20, "*"))
print("Hello".ljust(20, "-"))
print("Hello".center(20))
print("Hello".center(20, "="))
print()

print("strip(), rstrip(), lstrip()メソッド")
spam = "          Hello World          "
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())
spam = "SpamSpamBaconSpamEggsSpamSpam"
# strip()に ampS という引数を渡すと、a, m, p, Sを文字列の両端から除去する
# strip()に渡す文字列の中で、文字列の並び順は任意。すなわち、strip("ampS"), strip("mapS"), strip(Spam)は同じ
print(spam.strip("ampS"))

print("pyperclipモジュール")
pyperclip.copy("Hello world!")  # "Hello world!"をクリップボードにコピー
print(pyperclip.paste())  # クリップボードの内容を取得
