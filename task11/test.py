import random

# 直接读取单词文件
words = []
with open("./task11/obesenec.txt", 'r') as file:
    words = file.read().splitlines()

# 随机选择单词
word_to_guess = random.choice(words).lower()

guessed_letters = set()
attempts = 0
max_attempts = 10

while attempts < max_attempts:
    # 生成当前显示字符串
    current_display = ""
    for letter in word_to_guess:
        current_display += letter if letter in guessed_letters else "."
    print(f"\n当前单词: {current_display}")

    # 处理玩家输入
    while True:
        guess = input("请输入一个字母: ").lower()
        if len(guess) == 1 and guess.isalpha():
            break
        print("请输入一个有效的字母！")

    # 检查是否重复猜测
    if guess in guessed_letters:
        print("这个字母已经猜过了，请换一个")
        continue

    guessed_letters.add(guess)

    # 判断猜测结果
    if guess in word_to_guess:
        print(f"正确！字母 {guess} 在单词中")
    else:
        print(f"错误！字母 {guess} 不在单词中")
        attempts += 1

    # 检查是否胜利
    is_win = True
    for letter in word_to_guess:
        if letter not in guessed_letters:
            is_win = False
            break
    if is_win:
        print(f"\n恭喜！你猜对了单词 {word_to_guess}！")
        break

    # 显示剩余次数
    print(f"剩余尝试次数: {max_attempts - attempts}")

# 失败处理
if not is_win:
    print(f"\n游戏结束！正确单词是：{word_to_guess}")