from setuptools import setup, find_packages

setup(
    name='tex_to_png',  # パッケージ名
    version='0.1.0',  # バージョン
    description='Converts LaTeX code to PNG image',  # パッケージの説明
    packages=find_packages(),  # パッケージのディレクトリを自動的に探す
    install_requires=[  # 依存パッケージ
        'matplotlib',
        'IPython',
    ],
    entry_points={  # コマンドラインインターフェースの定義
        'console_scripts': [
            'tex2png=tex_to_png:main',
        ],
    },
)