import numpy as np
import plotly.graph_objects as go
from ipywidgets import interact, FloatSlider, Layout, HBox, VBox, Dropdown
from IPython.display import display, HTML

# --- 初期パラメータ設定 ---
initial_w = 1.0
initial_k1 = 1.0
initial_k2 = 0.5

# 空間範囲
x_min, x_max = -5, 5
y_min, y_max = -5, 5
num_points = 80 # 解像度

# 時間範囲 (スライダー用)
t_min, t_max = 0, 2 * np.pi / initial_w # 少なくとも1周期分
t_step = 0.1

# --- 空間グリッドの生成 ---
x = np.linspace(x_min, x_max, num_points)
y = np.linspace(y_min, y_max, num_points)
X, Y = np.meshgrid(x, y)

# --- Plotly Figureの初期化 ---
# 初期波形を計算
initial_u = np.cos(initial_w * 0 - initial_k1 * X - initial_k2 * Y)

fig = go.Figure(data=[go.Surface(z=initial_u, x=X, y=Y, colorscale='Viridis')])

# レイアウトの設定
fig.update_layout(
    title=r'$$u(x, y, t) = \cos(\omega t - k_1 x - k_2 y)$$',
    scene=dict(
        xaxis_title=r'$$x$$',
        yaxis_title=r'$$y$$',
        zaxis_title=r'$$u$$',
        zaxis=dict(range=[-1.2, 1.2]), # Z軸の範囲を固定
        aspectmode='auto' # 3Dのアスペクト比自動調整
    ),
    width=800,
    height=700,
    margin=dict(l=50, r=50, b=50, t=80)
)

# --- インタラクティブUIの作成 ---

# スライダーのスタイル設定
slider_layout = Layout(width='600px')

# 角周波数 w のスライダー
w_slider = FloatSlider(
    value=initial_w,
    min=0.1,
    max=5.0,
    step=0.1,
    description='Angular Frequency (w):',
    orientation='horizontal',
    layout=slider_layout
)

# 波数 k1 のスライダー
k1_slider = FloatSlider(
    value=initial_k1,
    min=0.0,
    max=3.0,
    step=0.1,
    description='Wave Number k1:',
    orientation='horizontal',
    layout=slider_layout
)

# 波数 k2 のスライダー
k2_slider = FloatSlider(
    value=initial_k2,
    min=0.0,
    max=3.0,
    step=0.1,
    description='Wave Number k2:',
    orientation='horizontal',
    layout=slider_layout
)

# 時間 t のスライダー
t_slider = FloatSlider(
    value=0,
    min=t_min,
    max=t_max,
    step=t_step,
    description='Time (t):',
    orientation='horizontal',
    layout=slider_layout
)

# --- 更新関数 ---
def update_plot(t_val, w_val, k1_val, k2_val):
    """
    スライダーの値に基づいてプロットを更新する関数
    """
    # 新しいZデータを計算
    new_u = np.cos(w_val * t_val - k1_val * X - k2_val * Y)

    # Plotlyのトレースを更新
    with fig.batch_update(): # バッチアップデートで高速化
        fig.data[0].z = new_u
        fig.layout.title.text = (
            f'$$u(x, y, t) = \\cos({w_val:.1f}t - {k1_val:.1f}x - {k2_val:.1f}y)$$'
        )
        # 時間表示をタイトルに追加
        fig.layout.scene.annotations = [
            dict(
                text=f'Time: $t={t_val:.2f}$',
                xref="paper", yref="paper",
                x=0.05, y=0.95, showarrow=False,
                font=dict(size=14, color="black")
            )
        ]

# --- UIとプロットの結合 ---
# interact関数を使ってスライダーとupdate_plot関数を結合
interactive_plot = interact(
    update_plot,
    t_val=t_slider,
    w_val=w_slider,
    k1_val=k1_slider,
    k2_val=k2_slider
)

# UIウィジェットとFigureを縦に並べて表示
ui = VBox([
    HBox([w_slider]),
    HBox([k1_slider]),
    HBox([k2_slider]),
    HBox([t_slider])
])

# Jupyter Notebook/Labで表示
display(ui, fig)