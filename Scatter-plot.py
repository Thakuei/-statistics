# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 23:09:44 2023

@author: hakue
"""
#パッケージをインポート

from matplotlib import pyplot as plt
import pandas as pd

#日本語フォントを使えるようにする
plt.rcParams['font.family'] = 'Meiryo'

#csvの読み込み
df = pd.read_csv(r"C:\Users\hakue\OneDrive\デスクトップ\統計学Ⅱ\analys-data.csv", encoding="utf-8")

colorlist = ["#FFA500"]

#3bプロットをする新たな図(Fiugre)を作成する
fig = plt.figure()
ax =fig.add_subplot(111, projection = "3d")
ax.scatter(df["主成分1"], df["皮の薄さ"],df["主成分3"], color=colorlist)

#軸の名前を付ける
ax.set_xlabel('X軸の名前', fontdict={'fontsize': 10, 'fontweight': 'medium'})
ax.set_ylabel('y軸の名前', fontdict={'fontsize': 10, 'fontweight': 'medium'})
ax.set_zlabel('z軸の名前', fontdict={'fontsize': 10, 'fontweight': 'medium'})

#県名をプロットされた点に対して名前を付ける
for i in range(len(df)):
    ax.text(df.iloc[i]['主成分1'], df.iloc[i]['皮の薄さ'], df.iloc[i]['主成分3'], df.iloc[i]["県名"])
