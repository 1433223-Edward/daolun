from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import io

url = "https://www.wanplus.cn/kog/teamstats"

chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(options=chrome_options)  
driver.get(url)

wait = WebDriverWait(driver, 10)
detail_list_div = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'detail-list')))

# 获取所有的选项
event_options = driver.find_elements(By.CSS_SELECTOR, 'div.match-list select[name="event"] option')
div_titles = driver.find_elements(By.CSS_SELECTOR, 'div.detail-list-title div')

# 创建 ExcelWriter 对象
with pd.ExcelWriter('output_data.xlsx', engine='xlsxwriter') as writer:
    for event_option in event_options:
        for div_title in div_titles:
            # 选择不同的选项和标题
            event_option.click()
            div_title.click()

            # 等待表格加载完成
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'dataTables_wrapper')))

            # 解析网页内容
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            wrapper_div = soup.find('div', {'class': 'dataTables_wrapper no-footer'})
            table = wrapper_div.find('table')

            if table:
                # 使用 pandas 读取 HTML 表格
                df = pd.read_html(io.StringIO(str(table)))[0]

                # 检查是否包含“没有比赛记录”
                if "没有比赛记录。" not in df.to_string():
                    # 删除包含空值的行
                    df = df.dropna()

                    if not df.empty:
                        # 将数据存储到 Excel 文件，使用组合的名称作为 sheet 名称
                        sheet_name = f"{event_option.text}_{div_title.text}"
                        df.to_excel(writer, index=False, sheet_name=sheet_name)
                        print(f"成功存储数据到 {sheet_name}")
                    else:
                        print(f"表格为空，未存储数据。")
                else:
                    print(f"表格中没有比赛记录，跳过录入。")

driver.quit()
