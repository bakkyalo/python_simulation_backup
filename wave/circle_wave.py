import numpy as np
import matplotlib.pyplot as plt

# プロットの設定
fig, ax = plt.subplots(1, 3, figsize=(12, 4),
                       subplot_kw={'projection': 'polar'}) # 極座標プロットを指定

# 角度データ
theta = np.linspace(0, 2 * np.pi, 500) # 0から2πまでを500分割

R = 1 
a = 0.2 # 振幅

# 基準となる円のデータ (r=R)
r_base_circle = np.full_like(theta, R) # theta と同じ形状で全ての要素が 3 の配列を作成

# ax[0]: k=2 に相当 (sin(4*theta))
k = 2
r0 = R + a * np.sin(k * theta) # 2k*theta で元の問題の k=2, 3, 4 に合わせる
ax[0].plot(theta, r_base_circle, color='gray', linestyle='--', alpha=0.7, label='r = 3') # r=3 の円を重ねる
ax[0].plot(theta, r0, color='blue')
ax[0].set_ylim(0, 1.3)
ax[0].spines['polar'].set_visible(False) # 極座標のスパインを非表示にする
ax[0].set_title(f'k = 2', pad=20, fontsize=16) # タイトルを上にずらす
ax[0].set_aspect('equal') # アスペクト比を保持

# 軸、軸ラベル、グリッドを非表示
ax[0].set_xticks([])
ax[0].set_yticks([])
ax[0].set_xlabel('')
ax[0].set_ylabel('')
# ax[0].grid(False)


# ax[1]: k=3 に相当 (sin(6*theta))
k = 3
r1 = R + a * np.sin(k * theta)
ax[1].plot(theta, r1, color='red')
ax[1].plot(theta, r_base_circle, color='gray', linestyle='--', alpha=0.7, label='r = 3') # r=3 の円を重ねる
ax[1].set_ylim(0, 1.3)
ax[1].set_title(f'k = 3', pad=20, fontsize=16) # タイトルを上にずらす
ax[1].set_aspect('equal')
ax[1].spines['polar'].set_visible(False) # 極座標のスパインを非表示にする

# 軸、軸ラベル、グリッドを非表示
ax[1].set_xticks([])
ax[1].set_yticks([])
ax[1].set_xlabel('')
ax[1].set_ylabel('')
ax[1].grid(False)


# ax[2]: k=4 に相当 (sin(8*theta))
k = 4
r2 = R + a * np.sin(k * theta)
ax[2].plot(theta, r2, color='green')
ax[2].set_title(f'k = 4', pad=20, fontsize=16) # タイトルを上にずらす
ax[2].plot(theta, r_base_circle, color='gray', linestyle='--', alpha=0.7, label='r = 3') # r=3 の円を重ねる
ax[2].set_aspect('equal')
ax[2].spines['polar'].set_visible(False) # 極座標のスパインを非表示にする
ax[2].set_ylim(0, 1.3)

# 軸、軸ラベル、グリッドを非表示
ax[2].set_xticks([])
ax[2].set_yticks([])
ax[2].set_xlabel('')
ax[2].set_ylabel('')
ax[2].grid(False)

plt.tight_layout() # サブプロット間のスペースを調整

plt.subplots_adjust(top=0.85) # 値を小さくすると上に広がる

plt.savefig('circle_wave.png', dpi=300)