import subprocess
import os
from pathlib import Path


def download_m3u8(url: str, output_dir: str = None):
    try:
        # 出力ディレクトリが指定されていない場合、現在のディレクトリを使用
        if output_dir is None:
            output_dir = os.getcwd()

        # 出力ディレクトリが存在しない場合は作成
        os.makedirs(output_dir, exist_ok=True)

        # 出力ファイルパスを構築
        output_file = os.path.join(output_dir, "video.mp4")

        # downloadm3u8コマンドを実行
        result = subprocess.run(
            ["downloadm3u8", "-o", output_file, url], capture_output=True, text=True
        )

        if result.returncode == 0:
            print(f"ダウンロード完了: {output_file}")
            return True
        else:
            print(f"ダウンロードエラー: {result.stderr}")
            return False

    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return False
