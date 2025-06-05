import random

# ダミーの選手名リスト（実在しそうな名前を中心に）
names = [
    "佐藤 大輔", "鈴木 一郎", "高橋 健太", "田中 直樹", "伊藤 翔", "渡辺 亮", "山本 拓海", "中村 悠斗", "小林 海斗", "加藤 大地",
    "John Smith", "Michael Brown", "David Johnson", "James Williams", "Robert Miller",
    "김민준", "박지훈", "이준서", "최지우", "정현우",
    "王 伟", "李 强", "张 伟", "刘 洋", "陈 俊",
    "Lucas Martin", "Mateo García", "Liam O'Connor", "Noah Dubois", "Oliver Müller", "Ivan Petrov"
]

# ダミーの出身地リスト（日本＋海外）
birthplaces = [
    "東京都", "大阪府", "北海道", "福岡県", "愛知県", "神奈川県", "京都府", "兵庫県", "埼玉県", "千葉県",
    "アメリカ", "イギリス", "カナダ", "オーストラリア", "ブラジル", "韓国", "中国", "フランス", "ドイツ", "スペイン",
    "イタリア", "ロシア", "アルゼンチン", "メキシコ", "インド", "タイ", "ベトナム", "フィリピン", "インドネシア", "南アフリカ"
]

# 選手データ生成
runners = []
for i in range(30):
    name = names[i]
    age = random.randint(18, 35)
    time = round(random.uniform(9.56, 12.00), 2)
    birthplace = random.choice(birthplaces)
    runners.append({
        "name": name,
        "age": age,
        "time": time,
        "birthplace": birthplace
    })

# タイムが悪い順（降順）にソート
runners_sorted = sorted(runners, key=lambda x: x["time"], reverse=True)

# 結果表示
print(f"{'順位':<4} {'氏名':<15} {'年齢':<4} {'タイム':<5} {'出身地'}")
for idx, runner in enumerate(runners_sorted, 1):
    # print(f"{idx:<4} {runner['name']:<15} {runner['age']:<4} {runner['time']:<5} {runner['birthplace']}")