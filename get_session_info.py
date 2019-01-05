import pandas
import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

import config
import xpath_config

if __name__ == "__main__":
    # コマンドライン引数取得
    LOGIN_ID = sys.argv[1]
    LOGIN_PASS = sys.argv[2]
    OUTPUT_PATH = sys.argv[3]
        
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
        driver.find_element_by_xpath(xpath_config.XPATH_BTN_MYPAGE).click()
        # 新しく開かれたタブに切り替え
        driver.switch_to_window(driver.window_handles[1])

        try:
            print("ログイン中")
            # メールアドレス
            driver.find_element_by_xpath(xpath_config.XPATH_TXT_ADDRESS).send_keys(LOGIN_ID)
            driver.find_element_by_xpath(xpath_config.XPATH_BTN_NEXT).click()
            sleep(3)
            # パスワード
            driver.find_element_by_xpath(xpath_config.XPATH_TXT_PASSWORD).send_keys(LOGIN_PASS)
            driver.find_element_by_xpath(xpath_config.XPATH_BTN_SIGNIN).click()

        except NoSuchElementException:
            pass

        # セッション一覧に移動
        print("セッション一覧へ移動中")
        driver.find_element_by_xpath(xpath_config.XPATH_BTN_SESSIONS).click()

        print("▼▼▼　セッション情報取得開始　▼▼▼")
        for session_key in config.SESSION_KEYS:
            for session_id in range(0, config.MAX_COUNT + 1):
                target_session = "{0}{1:02d}".format(session_key, session_id)
                try:
                    name = driver.find_element_by_xpath(xpath_config.XPATH_SESSION_NAME.replace("SESSION_ID", target_session)).text
                    pdf = driver.find_element_by_xpath(xpath_config.XPATH_SESSION_PDF.replace("SESSION_ID", target_session)).text
                    ppt = driver.find_element_by_xpath(xpath_config.XPATH_SESSION_PPT.replace("SESSION_ID", target_session)).text

                    if pdf == config.PDF_READY:
                        pdf = "○"
                    elif pdf == config.PDF_COMMING_SOON:
                        pdf = "★"
                    elif pdf == config.PDF_NOT_READY:
                        pdf = "-"

                    if ppt == config.PPT_READY:
                        ppt = "○"
                    elif ppt == config.PPT_COMMING_SOON:
                        ppt = "★"
                    elif ppt == config.PPT_NOT_READY:
                        ppt = "-"

                    se = pandas.Series([target_session, name, pdf, ppt], index=ret.columns)
                    ret = ret.append(se, ignore_index=True)
                    print(target_session, name)

                except NoSuchElementException:
                    continue
                    
        print("▲▲▲　セッション情報取得終了　▲▲▲")

    print("CSV出力中")
    ret.to_csv(OUTPUT_PATH, index=False, encoding="cp932")