from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# driver.get("https://www.amazon.com.br/dp/B084DWCZY6/ref=ods_gw_nh_atfd_md2023_bo?pf_rd_r=YETHBWGD2V861FFYNY0R&pf_rd_p=45702d04-8771-4e16-a836-55d5e76bdffb&pd_rd_r=1556ad71-2ba2-4b5f-8ff5-8737c27373e2&pd_rd_w=mqgeJ&pd_rd_wg=vwGoJ&ref_=pd_gw_unk") #open the browser
# price = driver.find_elements(By.CLASS_NAME, "a-offscreen")
# search = driver.find_elements(By.NAME, 'field-keywords')
#
# time.sleep(1)
# driver.quit() # quit all tabs for actual tab - .close

driver.get('https://www.python.org/')
elements = driver.find_elements(By.XPATH, '/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul')
string = ''
for element in elements:
    string += element.text


lista = string.split('\n')
time_list = []
name_list = []
for item in lista:
    index = lista.index(item)
    if index % 2 == 0:
        time_list.append(item)
    else:
        name_list.append(item)

dict_result = {}
for item in time_list:
    dict_result[time_list.index(item)] = {'time': item, 'name': name_list[time_list.index(item)]}

print(dict_result)
