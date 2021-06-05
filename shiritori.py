# person_list =[i for i in range(person)]
# word_list = []
# remark_list =[]
# for i in range(word):
#     word_list.append(input())
# for i in range(word,word + remark):
#     remark_list.append(input())

# index = 0
# for i in range(remark):
#     if i != 0:
#         if ( remark_list[i][0] != remark_list[i-1][-1]
#         or remark_list[i][-1:] == "z"
#         or remark_list[i] not in word_list
#         or remark_list[i] in remark_list[0:i-1]):
#         else:
#             index += 1
#             print(index)

# N,K,Mがそれぞれ人数、単語数、発言数
N, K, M = [int(x) for x in input().split()]

""" Kは単語数 """
# 単語リスト
words = [input() for x in range(K)]

# 使用済みリスト
used = []
# 最初の人かを判定する変数
init = True

""" Mは参加する人数 """
# 何番目の人が残っているかのリスト
member = list(range(N))
# 発言した人が何番目かの変数
index = 0

""" Mは発言数 """
# 各発言について処理を行う
for _ in range(M):
    # 発言した単語
    said = input()

    """ wordsは単語リスト、numは参加人数、usedは使用済みリスト """
    # 単語リストに存在しない、使用済みリストに存在する、最後の文字が'z'場合
    if said[-1] == 'z' or not said in words or said in used:
        # 人数を１人減らす
        N -= 1
        # しりとりが最初からになる
        init = True
        # ルールを破った場合
        member.pop(index)
        # 1を引く
        index -= 1

    else:
        # 最初の人ではない場合
        if not init:
            # 頭文字が直前の最後の文字と違う場合
            if not used[-1][-1] == said[0]:
                # 人数を１人減らす
                N -= 1
                # しりとりが最初からになる
                init = True
                # ルールを破った場合
                member.pop(index)
                # 1を引く
                index -= 1
            # 頭文字が直前の最後の文字と同じ場合
            else:
                # 使用済みリストに単語を追加
                used.append(said)
                # しりとりを続ける
                init = False
        # 最初の人の場合
        else:
            # 使用済みリストに単語を追加
            used.append(said)
            # しりとりを続ける
            init = False

    # 次に人に移る
    index += 1
    # 残っている人数を超えたら最初に戻る
    if index >= N:
        index = 0

# 何人残っているかを出力
print(N)

# 何番目の人が残っているかを出力
for num in member:
    print(num+1)
