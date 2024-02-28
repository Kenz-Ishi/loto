import pandas

loto7_url = 'http://sougaku.com/loto7/data/list1/'

#loto7_data = pandas.read_html(loto7_url,header=0,index_col=0)
loto7_data = pandas.read_html(loto7_url)

print("table 1 :")
print(loto7_data[0].head())

print("table 2 :")
print(loto7_data[1].head())

print("table 3:")
print(loto7_data[2].head())

print("table 4:")
print(loto7_data[3].head())


print("all table data")
print(loto7_data[3])

#不要データ削除
loto7_data[3].drop("詳細表示",axis=1,inplace=True)
loto7_data[3].drop("全数字計",axis=1,inplace=True)
loto7_data[3].drop("全数字 奇:偶",axis=1,inplace=True)
loto7_data[3].drop("本数字計",axis=1,inplace=True)
loto7_data[3].drop("本数字 奇:偶",axis=1,inplace=True)

#インデックス変更
loto7_data[3].set_index("抽選回",inplace=True)
#インデックス変更
#loto7_data[3].set_index("ｾｯﾄ",inplace=True)

loto7_data[3].drop(index="抽選回",axis=0,inplace=True)

print("test table:")

#print(loto7_data[3][['抽選回']].head())
print(loto7_data[3])
