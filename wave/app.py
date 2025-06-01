import dash
from dash import dcc, html, Input, Output, State
import plotly.graph_objects as go
import numpy as np

# Dashアプリケーションの初期化
app = dash.Dash(__name__)

# --- 定数と初期値 ---
X_RANGE = np.linspace(-5, 5, 100)
Y_RANGE = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X_RANGE, Y_RANGE)
TIME_STEPS = np.linspace(0, 2 * np.pi, 50) # アニメーションの時間ステップ

INITIAL_OMEGA = 1.0
INITIAL_K1 = 0.5
INITIAL_K2 = 2.0


# --- 平面波の計算関数 ---
def generate_surface_data(omega, k1, k2, t):
    """指定されたパラメータと時間で平面波のZ値を計算する関数"""
    Z = np.cos(omega * t - k1 * X - k2 * Y)
    return Z

# --- レイアウトの定義 ---
app.layout = html.Div([
    html.H1("3D Plane Wave Animator with Dash", style={'textAlign': 'center'}),

    # グラフ表示領域
    # dcc.Graph(id='plane-wave-graph', style={'height': '520px'}),
    dcc.Graph(id='plane-wave-graph'),

    # アニメーション制御用のDCC Intervalとボタン
    html.Div([
        html.Button('Play Animation', id='play-button', n_clicks=0,
                    style={'marginRight': '10px'}),
        html.Button('Stop Animation', id='stop-button', n_clicks=0),
        dcc.Interval(
            id='interval-component',
            interval=50,
            n_intervals=0,
            disabled=True
        ),
    ], style={'textAlign': 'center', 'padding': '20px'}),

    # スライダーのコンテナ
    html.Div([
        html.Label("Omega (ω):"),
        dcc.Slider(
            id='omega-slider',
            min=0.1,
            max=5.0,
            step=0.1,
            value=INITIAL_OMEGA,
            marks={i: f'{i:.1f}' for i in np.arange(0.1, 5.1, 0.5)},
            tooltip={"placement": "bottom", "always_visible": True},
            updatemode='drag'
        ),
        # html.Br(),

        html.Label("k1:"),
        dcc.Slider(
            id='k1-slider',
            min=-5.0,
            max=5.0,
            step=0.1,
            value=INITIAL_K1,
            marks={i: f'{i:.1f}' for i in np.arange(-5.0, 5.1, 1.0)},
            tooltip={"placement": "bottom", "always_visible": True},
            updatemode='drag'
        ),
        # html.Br(),

        html.Label("k2:"),
        dcc.Slider(
            id='k2-slider',
            min=-5.0,
            max=5.0,
            step=0.1,
            value=INITIAL_K2,
            marks={i: f'{i:.1f}' for i in np.arange(-5.0, 5.1, 1.0)},
            tooltip={"placement": "bottom", "always_visible": True},
            updatemode='drag'
        ),
        html.Br(),
    ], style={'width': '80%', 'margin': 'auto', 'padding': '20px'}),
])

# --- コールバックの定義 ---

# グラフ更新コールバック（スライダーまたは時間経過による更新）
@app.callback(
    Output('plane-wave-graph', 'figure'),
    Input('omega-slider', 'value'),
    Input('k1-slider', 'value'),
    Input('k2-slider', 'value'),
    Input('interval-component', 'n_intervals')
)
def update_graph(omega, k1, k2, n_intervals):
    t_index = n_intervals % len(TIME_STEPS)
    current_t = TIME_STEPS[t_index]

    Z = generate_surface_data(omega, k1, k2, current_t)

    fig = go.Figure(
        data=[go.Surface(z=Z, x=X, y=Y,
                         colorscale='viridis',
                         cmin=-1, cmax=1)],
        layout=go.Layout(
            # 変更点: タイトルに時間表示を再追加
            title=f'Plane Wave: ω={omega:.2f}, k1={k1:.2f}, k2={k2:.2f}, t={current_t:.2f}',
            scene=dict(
                xaxis_title='X',
                yaxis_title='Y',
                zaxis_title='u',
                zaxis=dict(range=[-1.5, 1.5])
            ),
            margin=dict(l=0, r=0, b=0, t=40)
        )
    )
    return fig

# アニメーション制御コールバック
@app.callback(
    Output('interval-component', 'disabled'),
    Input('play-button', 'n_clicks'),
    Input('stop-button', 'n_clicks'),
    State('interval-component', 'disabled')
)
def toggle_animation(play_clicks, stop_clicks, is_disabled):
    ctx = dash.callback_context

    if not ctx.triggered:
        return True
    
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'play-button':
        return False
    elif button_id == 'stop-button':
        return True
    
    return is_disabled

# アプリケーションの実行
if __name__ == '__main__':
    app.run(debug=True)