import random

# 英検1級レベルの単語リスト（例：単語:意味）
words = [
    ("aberration", "逸脱"),
    ("acquiesce", "黙認する"),
    ("alacrity", "敏速"),
    ("animosity", "敵意"),
    ("belligerent", "好戦的な"),
    ("cacophony", "不協和音"),
    ("capitulate", "降伏する"),
    ("circumspect", "用心深い"),
    ("cogent", "説得力のある"),
    ("conundrum", "難問"),
    ("deleterious", "有害な"),
    ("disparate", "異なる"),
    ("egregious", "ひどい"),
    ("enervate", "弱める"),
    ("equanimity", "平静"),
    ("fastidious", "気難しい"),
    ("fortuitous", "偶然の"),
    ("gregarious", "社交的な"),
    ("harangue", "長々しい演説"),
    ("iconoclast", "因習打破主義者"),
    ("laconic", "簡潔な"),
    ("magnanimous", "寛大な"),
    ("nefarious", "極悪な"),
    ("obfuscate", "分かりにくくする"),
    ("paragon", "模範"),
    ("quixotic", "非現実的な"),
    ("recalcitrant", "反抗的な"),
    ("sagacious", "賢明な"),
    ("taciturn", "無口な"),
    ("ubiquitous", "至る所にある"),
    ("vociferous", "騒々しい"),
    ("wary", "用心深い"),
    ("zealous", "熱心な"),
    ("vindicate", "潔白を証明する"),
    ("tantamount", "同等の"),
    ("spurious", "偽の"),
    ("rancor", "憎しみ"),
    ("placate", "なだめる"),
    ("obsequious", "こびへつらう"),
    ("mollify", "和らげる"),
]

# 30問ランダムに出題
questions = random.sample(words, 30)
score = 0

print("英検1級単語 5択クイズ（30問）")
print("意味に合う英単語を選んでください。\n")

for i, (word, meaning) in enumerate(questions, 1):
    # 正解＋不正解4つを選択肢に
    choices = [word]
    while len(choices) < 5:
        w, _ = random.choice(words)
        if w not in choices:
            choices.append(w)
    random.shuffle(choices)
    print(f"Q{i}: 「{meaning}」に最も近い英単語は？")
    for idx, choice in enumerate(choices, 1):
        print(f"  {idx}. {choice}")
    try:
        ans = int(input("番号で回答: "))
    except:
        ans = 0
    if 1 <= ans <= 5 and choices[ans-1] == word:
        print("正解！\n")
        score += 1
    else:
        print(f"不正解。正解は「{word}」\n")

print(f"あなたの正解数: {score}/30")
if score >= 21:
    print("合格です！おめでとうございます。")
else:
    print("不合格です。再チャレンジしましょう。")