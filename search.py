import csv
import os

# 検索ソース
source = [
    "竈門禰豆子",
    "竈門炭治郎",
    "煉獄杏寿郎",
    "冨岡義勇",
    "不死川玄弥",
    "栗花落カナヲ",
    "我妻善逸"
]


class Member(object):
    def __init__(self):
        """
        member.csvの有無の確認とデータの取得を行う
        """
        self.check_csv_file = os.path.exists('member.csv')
        self.fieldnames = ['NAME']

    def ask_character(self):
        self.character = input("\nあなたが好きな鬼滅の刃の登場人物の名前を入力してください！\n\n")
        return self.character

    def print_existence_or_non(self):
        if self.character in source:
            print('\n{}はリストに存在します。\n'.format(self.character))
        else:
            print('\n{}はリストに存在しません。\n'.format(self.character))

    def write_name(self):
        # 既にcsvファイルがある場合
        if self.check_csv_file:
            with open('member.csv', 'r') as rewrite_csv:
                existing_members = csv.DictReader(rewrite_csv)

                existing_member_list = []
                for existing_member in existing_members:
                    existing_member_list.append(existing_member['NAME'])

            # 回答されたキャラクターが既にcsvファイルに存在する場合
            if self.character in existing_member_list:
                pass

            # 回答されたキャラクターがまだcsvファイルに存在しない場合
            else:
                with open('member.csv', 'a') as add_to_csv:
                    writer = csv.DictWriter(add_to_csv, fieldnames=self.fieldnames)
                    writer.writerow({'NAME': self.character})

        # まだcsvファイルがない場合
        else:
            with open('member.csv', 'w', encoding='UTF-8') as write_to_csv:
                writer = csv.DictWriter(write_to_csv, fieldnames=self.fieldnames)
                writer.writeheader()
                for character_name in source:
                    writer.writerow({'NAME': character_name})

                # 回答されたキャラクターが既にsourceに存在する場合
                if self.character in source:
                    pass
                # 回答されたキャラクターがまだsourceに存在しない場合
                else:
                    writer.writerow({'NAME': self.character})

    def __del__(self):
        print('\nご回答有難うございました！\n')


if __name__ == '__main__':
    member = Member()
    member.ask_character()
    member.print_existence_or_non()
    member.write_name()
    del member
