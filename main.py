from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from IPython.display import display, Image
import io
import matplotlib.pyplot as plt

def tex_to_png(tex_code):
    fig, ax = plt.subplots(figsize=(6, 2))
    ax.text(0.5, 0.5, f"${tex_code}$", fontsize=20, ha='center', va='center')
    ax.axis('off')
    
    # 画像をバッファに保存
    buf = io.BytesIO()
    canvas = FigureCanvas(fig)
    canvas.print_png(buf)
    buf.seek(0)
    
    # バッファから画像を表示
    display(Image(data=buf.getvalue()))
    
    # バッファからPNGファイルとして保存
    with open("output.png", "wb") as f:
        f.write(buf.getvalue())

# ユーザーからのTeXコード入力
tex_code = input("TeXコードを入力してください: ") # 例としてはE=mc^2とかでしょうか
tex_to_png(tex_code)