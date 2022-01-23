"""
データ型の宣言： username
    属性：
        実際のユーザー名
    ルール；
        ユーザー名は4文字以上20文字以内ある
    できること：
        ユーザー名を大文字に変換する
"""


# 「UserName」というクラスを宣言
#  「self.name」はそれぞれのname
class UserName:
    # 右のnameは渡された変数（BobやらTomやら）
    # 「__init__」は引数も渡してあげないとダメ。
    def __init__(self, name):
        # nameのチェック（4文字以上20文字以内を達成していない場合にエラー出す。）
        # ※len()は文字列であれば文字数のカウントも可能
        # 4 <= len(name) <= 20でもOK。
        if not (4 <= len(name) and len(name) <= 20):
            # エラーを出力する。
            raise ValueError(f'{name}はルール違反です')
        self.name = name

    def battle_name(self):
        # 「upper()」で大文字にする。
        return self.name.upper()


# 実体化　上の設計図に
bob = UserName(name='Bob Smith')

print(bob.name)
# bobに「screen_name()」関数を使って大文字にする。
print(bob.battle_name())
