import traceback
import logging


# raiseとtraceback
# 例外クラスを自作する（Exceptionを継承して、適用する状況に合わせたクラス名を設定）
class EqualOneError(Exception):
    pass


def spam(a=1):
    bacon(a)


def bacon(b):
    if b == 1:
        raise EqualOneError("引数の値が1です。")
        # raise Exeptionクラス("任意のメッセージ")で独自に例外を起こすことが可能
    else:
        print(f"{b}は問題のない引数です。")


try:
    spam()
except EqualOneError:
    with open("errorInfo.txt", "w") as error_file:
        error_traceback = traceback.format_exc()  # 例外発生時のトレースバックを取得
        error_file.write(error_traceback)
    print("トレースバック情報をerrorInfo.txtに書きました。")

try:
    spam(2)
except EqualOneError:
    with open("errorInfo.txt", "w") as error_file:
        error_traceback = traceback.format_exc()  # 例外発生時のトレースバックを取得
        error_file.write(error_traceback)
    print("トレースバック情報をerrorInfo.txtに書きました。")


# アサート
"""
コードが明らかに間違った挙動をしていないかを確認するための正常性チェックのこと
構文：assert 条件式, 条件式がFalseとなったときに表示する文字列
アサートは開発用のものであり、最終製品用のものではない。
assert文による処理速度低下は気になるほどのものではないが、
-Oオプションをつけてプログラムを実行することで、アサートを無効にできる
"""
# 例えば下記は、変数pod_bay_door_statusが処理上"open"であるはずなので（という想定）、それをチェックしている
pod_bay_door_status = "open"
assert pod_bay_door_status == "open", "ポッドベイのドアは'open'でなければならない。"
# pod_bay_door_status = "close"
# assert pod_bay_door_status == "open", "ポッドベイのドアは'open'でなければならない。"


# ログを記録する
def factorial(n):
    # 階乗計算を行う関数
    logging.debug(f"factorial({n})開始")
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug(f"i = {i}, total = {total}")
    logging.debug(f"factorial({n})終了")
    return total


# logging.basicConfigを最初に呪文のように設定する
logging.basicConfig(level=logging.DEBUG,
                    format=" %(asctime)s - %(levelname)s - %(message)s")
logging.debug("プログラム開始")
print(factorial(5))
logging.debug("プログラム終了")

print("ファイルへログ出力")
# logging.basicConfigは一度設定すると、forceオプションをTrueにしないと上書きできない
# ログをファイルに出力するには、filenameオプションを使う。filemodeで"w"か"a"(default)を設定
logging.basicConfig(level=logging.DEBUG,
                    format=" %(asctime)s - %(levelname)s - %(message)s",
                    filename="myProgramLog.txt", filemode="w", force=True)
logging.debug("ファイルへログ出力開始")
print(factorial(5))
logging.debug("ファイルへログ出力終了")

# ログレベル
"""
ログレベルを変更することで、見たいメッセージの表示有無を制御できる
basicConfig(level=logging.DEBUG)で、全てのログレベルのメッセージが表示される（DEBUGが最低レベルのため）
basicConfig(level=logging.ERROR)で、ERRORとCRITICALのメッセージだけが表示される
どのメッセージにどのログレベルを設定するかはその人の裁量
logging.disable(logging.CRITICAL)をプログラムに追加することで全てのログ出力を無効化できる

level     log output function     discription
DEBUG     logging.debug()         最低レベル。詳細情報用。問題解析用に用いる
INFO      logging.info()          各種イベントの情報を記録したりプログラムの要所で動作確認をしたりするために用いる
WARNING   logging.warning()       プログラムが機能しないことはないが将来そうなりそうな潜在的な問題を示すのに用いる
ERROR     logging.error()         プログラムが何か動作に失敗したことによるエラーを記録するために用いる
CRITICAL  logging.critical()      最高レベル。プログラムが実行を中止する致命的なエラーが
                                  起こったか起ころうとしていることを示すのに用いる
"""
logging.basicConfig(level=logging.DEBUG,
                    format=" %(asctime)s - %(levelname)s - %(message)s",
                    force=True)
logging.debug("デバッグ用詳細情報")
logging.info("loggingモジュールは動作中")
logging.warning("エラーメッセージがログ出力されようとしている")
logging.error("エラーが発生した")
logging.critical("プログラムは回復不能")

print("ログレベルERROR, CRITICALのメッセージだけを出力")
logging.basicConfig(level=logging.ERROR,
                    format=" %(asctime)s - %(levelname)s - %(message)s",
                    force=True)
logging.debug("デバッグ用詳細情報")
logging.info("loggingモジュールは動作中")
logging.warning("エラーメッセージがログ出力されようとしている")
logging.error("エラーが発生した")
logging.critical("プログラムは回復不能")

# ログ出力の無効化
print("ログ出力の無効化")
logging.basicConfig(level=logging.DEBUG,
                    format=" %(asctime)s - %(levelname)s - %(message)s",
                    force=True)
logging.disable(logging.CRITICAL)
logging.debug("デバッグ用詳細情報")
logging.info("loggingモジュールは動作中")
logging.warning("エラーメッセージがログ出力されようとしている")
logging.error("エラーが発生した")
logging.critical("プログラムは回復不能")
