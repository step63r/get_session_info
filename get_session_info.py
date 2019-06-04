import pandas
import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.common.exceptions import NoSuchElementException

import config
import xpath_config

def main(login_id, login_pass, output_path):
    """
    メイン関数

    Parameters
    ----------
    login_id : str
        ID
    login_pass : str
        パスワード
    output_path : str
        出力ファイルパス
    """
    # エンジン生成
    print("エンジン生成中")
    options = Options()
    options.binary_location = config.APP_PATH
    options.add_argument('--headless')
    options.add_argument('--lang=ja')

    ret = pandas.DataFrame(index={}, columns=config.OUTPUT_COLUMNS)

    with webdriver.Chrome(chrome_options=options, executable_path=config.DRIVER_PATH) as driver:
        # アクセス
        print("アクセス中：{0}".format(config.BASE_URL))
        driver.get(config.BASE_URL)
        # マイページへ
        print("マイページへ移動中")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath_config.XPATH_BTN_MYPAGE))
        )
        driver.find_element_by_xpath(xpath_config.XPATH_BTN_MYPAGE).click()

        try:
            print("ログイン中")
            # メールアドレス
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath_config.XPATH_TXT_ADDRESS))
            )
            driver.find_element_by_xpath(xpath_config.XPATH_TXT_ADDRESS).send_keys(login_id)
            driver.find_element_by_xpath(xpath_config.XPATH_BTN_NEXT).click()

            # 個人のアカウント
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath_config.XPATH_PERSONAL_BTN))
            )
            driver.find_element_by_xpath(xpath_config.XPATH_PERSONAL_BTN).click()

            # パスワード
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath_config.XPATH_TXT_PASSWORD))
            )
            driver.find_element_by_xpath(xpath_config.XPATH_TXT_PASSWORD).send_keys(login_pass)
            driver.find_element_by_xpath(xpath_config.XPATH_BTN_SIGNIN).click()

        except NoSuchElementException:
            pass

        # セッション一覧に移動
        print("セッション一覧へ移動中")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath_config.XPATH_BTN_SESSIONS))
        )
        driver.find_element_by_xpath(xpath_config.XPATH_BTN_SESSIONS).click()

        print("▼▼▼　セッション情報取得開始　▼▼▼")
        for session_key in config.SESSION_KEYS:
            for session_id in range(0, config.MAX_COUNT + 1):
                try:
                    # 検索中のセッションコード
                    target_session = "{0}{1:02d}".format(session_key, session_id)

                    for div1 in range(1, 68):
                        for div2 in range(1, 21):
                            try:
                                # div番号でセッションコードを取得する
                                selected_session_id = driver.find_element_by_xpath(xpath_config.XPATH_SESSION_CODE.replace("DIV_NUMBER_1", str(div1)).replace("DIV_NUMBER_2", str(div2))).text

                                # 検索中のコードとdiv番号で取得したコードが一致したら処理続行
                                if target_session == selected_session_id:
                                    # セッション名
                                    name = driver.find_element_by_xpath(xpath_config.XPATH_SESSION_NAME.replace("DIV_NUMBER_1", str(div1)).replace("DIV_NUMBER_2", str(div2))).text

                                    # PowerPoint
                                    ppt = driver.find_element_by_xpath(xpath_config.XPATH_SESSION_PPT.replace("SESSION_ID", target_session)).text
                                    if ppt == config.PPT_READY:
                                        ppt = "○"
                                    elif ppt == config.PPT_COMMING_SOON:
                                        ppt = "★"
                                    elif ppt == config.PPT_NOT_READY:
                                        ppt = "-"

                                    # PDF
                                    pdf = driver.find_element_by_xpath(xpath_config.XPATH_SESSION_PDF.replace("SESSION_ID", target_session)).text
                                    if pdf == config.PDF_READY:
                                        pdf = "○"
                                    elif pdf == config.PDF_COMMING_SOON:
                                        pdf = "★"
                                    elif pdf == config.PDF_NOT_READY:
                                        pdf = "-"

                                    # 動画
                                    mov = driver.find_element_by_xpath(xpath_config.XPATH_SESSION_MOV.replace("SESSION_ID", target_session)).text
                                    if mov == config.MOV_READY:
                                        mov = "○"
                                    elif mov == config.MOV_COMMING_SOON:
                                        mov = "★"
                                    elif mov == config.MOV_NOT_READY:
                                        mov = "-"

                                    se = pandas.Series([target_session, name, ppt, pdf, mov], index=ret.columns)
                                    ret = ret.append(se, ignore_index=True)
                                    print(target_session, name)

                                else:
                                    continue
                            except NoSuchElementException:
                                continue
                except NoSuchElementException:
                    continue
        print("▲▲▲　セッション情報取得終了　▲▲▲")

    print("CSV出力中")
    ret.to_csv(output_path, index=False, encoding="cp932")

if __name__ == "__main__":
    # コマンドライン引数取得
    LOGIN_ID = sys.argv[1]
    LOGIN_PASS = sys.argv[2]
    OUTPUT_PATH = sys.argv[3]

    # メイン処理開始
    main(LOGIN_ID, LOGIN_PASS, OUTPUT_PATH)