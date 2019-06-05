# Google Chromeパス
APP_PATH = r"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
# ChromeDriverパス
DRIVER_PATH = r"C:\\chromedriver_win32\\chromedriver.exe"
# ベースURL
BASE_URL = "https://www.event-marketing.jp/events/decode/2019/register/LoginCheckMypage.aspx"

# セッションIDのキー一覧
SESSION_KEYS = [
    "AI",
    "CM",
    "CD",
    "DP",
    "DT",
    "IT",
    "MW",
    "PR",
    "SE",
    "SP"
]

# IDの最大カウント数
MAX_COUNT = 99
# DIV(1)の最大カウント数
MAX_DIV1 = 67
# DIV(2)の最大カウント数
MAX_DIV2 = 20

# 出力列
OUTPUT_COLUMNS =[
    "ID",
    "セッション名",
    "PowerPoint",
    "PDF",
    "動画"
]

# 公開済みのPDF
PDF_READY = "PDF 形式"
# 公開予定のPDF
PDF_COMMING_SOON = "PDF 形式 公開予定"
# 公開予定なしのPDF
PDF_NOT_READY = "PDF 形式 公開なし"

# 公開済みのPowerPoint
PPT_READY = "PowerPoint 形式"
# 公開予定のPowerPoint
PPT_COMMING_SOON = "PowerPoint 形式 公開予定"
# 公開予定なしのPowerPoint
PPT_NOT_READY = "PowerPoint 形式 公開なし"

# 公開済みの動画
MOV_READY = "動画"
# 公開予定の動画
MOV_COMMING_SOON = "動画公開予定"
# 公開予定なしの動画
MOV_NOT_READY = "動画公開なし"
