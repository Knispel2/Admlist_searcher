from selenium import webdriver, common
from webdriver_manager.chrome import ChromeDriverManager

def give_chrome_option():
    chromeOptions = webdriver.ChromeOptions() #setup chrome option
    #chromeOptions.add_argument("--headless")
    return chromeOptions


def get_admpages():
    base = pandas.read_csv('C:\FSR_Data\base\base.csv')
    data_fac = {'ОК_КОСМИЧЕСКИЕ ИССЛЕДОВАНИЯ И КОСМОНАВТИКА', 'CК_КОСМИЧЕСКИЕ ИССЛЕДОВАНИЯ И КОСМОНАВТИКА',
                'ЦК_КОСМИЧЕСКИЕ ИССЛЕДОВАНИЯ И КОСМОНАВТИКА', 'КОСМИЧЕСКИЕ ИССЛЕДОВАНИЯ И КОСМОНАВТИКА'}
    base = base[base['Направление'].isin(options)]
    base = base['Полис'].to_list()