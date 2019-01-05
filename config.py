# Google Chromeパス
APP_PATH = r"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"

# ChromeDriverパス
DRIVER_PATH = r"D:\\OneDrive\\Development\\chromedriver_win32\\chromedriver.exe"

# ベースURL
BASE_URL = "https://www.microsoft.com/ja-jp/events/techsummit/2018/"

# セッションIDのキー一覧
SESSION_KEYS = [
    "AC",
    "AD",
    "BZ",
    "CI",
    "DA",
    "PR",
    "SP"
]

# IDの最大カウント数
MAX_COUNT = 99

# 出力列
OUTPUT_COLUMNS =[
    "ID",
    "セッション名",
    "PDF",
    "PPT"
]

# 公開済みのPDF
PDF_READY = "PDF"
# 公開予定のPDF
PDF_COMMING_SOON = "PDF公開予定"
# 公開予定なしのPDF
PDF_NOT_READY = "PDF公開予定なし"

# 公開済みのPPT
PPT_READY = "PPT"
# 公開予定のPPT
PPT_COMMING_SOON = "PPT公開予定"
# 公開予定なしのPPT
PPT_NOT_READY = "PPT公開予定なし"