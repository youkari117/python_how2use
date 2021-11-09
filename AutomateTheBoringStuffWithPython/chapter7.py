"""
正規表現の基本ステップ
1. import re
2. re.compile()関数を呼び出しRegexオブジェクトを生成（raw文字列を使用）
3. Regexオブジェクトのsearch()メソッドに、検索対象の文字列を渡すと、Matchオブジェクトを返す
   search()メソッドは、最初に出現したものが、Matchオブジェクトとして返る
4. Matchオブジェクトのgroup()メソッドを呼び出し、実際にマッチした文字列を取得する

正規表現に用いる記号の簡単まとめ
・?              → 直前のグループの０回か１回の出現にマッチ
・*              → 直前のグループの０回以上の出現にマッチ
・+              → 直前のグループの１回以上の出現にマッチ
・{n}            → 直前のグループのｎ回の出現にマッチ
・{n,}           → 直前のグループのｎ回以上の出現にマッチ
・{,m}           → 直前のグループの０～ｍ回の出現にマッチ
・{n,m}          → 直前のグループのｎ～ｍ回の出現にマッチ
・{n,m}?, *?, +? → 直前のグループの非貪欲マッチを行う
・^spam          → 「spam」から始まる文字列とマッチ
・spam$          → 「spam」で終わる文字列とマッチ
・.              → 改行文字以外の任意の１文字とマッチ
・\d, \w, \s     → それぞれ数字、単語を構成する文字、空白文字にマッチ
・\D, \W, \S     → それぞれ数字、単語を構成する文字、空白文字以外の文字にマッチ
・[a-zA-Z0-9]    → 角カッコの中の任意の１文字にマッチ
・[a-zA-Z0-9]    → 角カッコの中の文字以外の任意の１文字にマッチ

re.compile()の第二引数(|でつなげて複数を同時に利用可能、re.DOTALL | re.IGNORECASE)
re.DOTALL     → ドット文字が改行を含む全ての文字とマッチ
re.IGNORECASE → 大文字と小文字を区別せずにマッチ
re.VERVOSE    → 正規表現の文字列中の空白文字やコメントを無視
"""

import re
phone_num_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
mo = phone_num_regex.search("私の電話番号は415-555-4242です。")
print("電話番号が見つかりました：" + mo.group())

# 丸かっこを用いたグルーピング、group()とgroups()
phone_num_regex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
mo = phone_num_regex.search("私の電話番号は415-555-4242です。")
print(mo.group())
print(mo.group(0))
print(mo.group(1))
print(mo.group(2))
print(mo.groups())

# |の使い方
bat_regex = re.compile(r"Bat(man|mobile|copter|bat)")
mo = bat_regex.search("Batmobile Batman")
print(mo.group())
print(mo.group(1))

# findall()メソッド
# findall()はMatchオブジェクトではなく、マッチした文字列のリストを返す
# 正規表現にグループが含まれていると、findall()はタプルのリストを返す
# 各タプルの要素は、正規表現のグループに対応してマッチした文字列
phone_num_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
mo = phone_num_regex.search("Call: 415-555-9999 Work: 212-555-0000")
print(mo.group())
print(phone_num_regex.findall("Call: 415-555-9999 Work: 212-555-0000"))
phone_num_regex = re.compile(r"(\d\d\d)-(\d\d\d)-(\d\d\d\d)")
print(phone_num_regex.findall("Call: 415-555-9999 Work: 212-555-0000"))

# sub()メソッドによる文字列の置換
# 第一引数に\1, \2, \3のようにグループの番号を記述すると、そのグループに該当する文字列に置換される
names_regex = re.compile(r"Agent \w+")
print(names_regex.sub("CENSORED",
                      "Agent Alice gave the secret documents to Agent Bob."))
agent_names_regex = re.compile(r"Agent (\w)\w*")
agent_str = "Agent Alice told Agent Carol \
that Agent Eve knew Agent Bob was a double agent."
print(agent_names_regex.sub(r"\1****", agent_str))

# re.VERVOSEの使用例
phone_regex = re.compile(r"""(
    (\d{3}|\(\d{3}\))?             # 3桁の市外局番、（）がついていてもよい
    (\s|-|\.)?                     # 区切り（スペースかハイフンかドット）
    \d{3}                          # 3桁の市外局番
    (\s|-|\.)                      # 区切り
    \d{4}                          # 4桁の番号
    (\s*(ext|x|ext.)\s*\d{2,5})?   # 2~5桁の内線番号
)""", re.VERBOSE)
