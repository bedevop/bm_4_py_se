# BM, Igal

import os.path, configparser, random, string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# Configuration file name, .ini expected
configuration_file = './cnf.ini'

# Init web Driver Chrome
# options = webdriver.ChromeOptions()
# options.add_argument("headless")
chrome_web_driver = webdriver.Chrome(executable_path='../cd/cd.exe')


# Parse target uri from configuration file
def load_configuration(ini_file):
    full_path = None
    config_section = 'URI'
    if os.path.isfile(ini_file):
        config_parsed = configparser.ConfigParser()
        print('Parsed file : ' + str(config_parsed.read(ini_file)))
        try:
            full_path = config_parsed[config_section]['protocol']\
                        + '://' \
                        + config_parsed[config_section]['url']
        except KeyError:
            print('URI section not configured')
        finally:
            return full_path
    else:
        print('Configuration file not found')


# Generate random string fitted for password requirements
def generate_string():
    generate = random.sample(string.ascii_lowercase, 4) + \
        random.sample(string.ascii_uppercase, 4) + \
        random.sample(string.digits, 2)
    return ''.join(generate)


# Check if target is set
if url := load_configuration(configuration_file):

    # A. Registration screen
    chrome_web_driver.get(url)

    login_register = WebDriverWait(chrome_web_driver, 20).until(
        expected_conditions.element_to_be_clickable((By.CLASS_NAME, "seperator-link")))
    login_register.click()

    choose_register = WebDriverWait(chrome_web_driver, 30).until(
        expected_conditions.element_to_be_clickable((By.CLASS_NAME, "text-link")))
    choose_register.click()

    generated_str = generate_string()
    form_input = chrome_web_driver.find_elements(By.XPATH, '//input')
    for index, _ in enumerate(form_input[:4]):
        if index == 1:
            _.send_keys(generated_str + '@testmail.ru')
        elif index == 3:
            _.send_keys(generated_str)
            _.send_keys(Keys.ENTER)
        else:
            _.send_keys(generated_str)

    # B. Home Screen
    # selections = WebDriverWait(chrome_web_driver, 30).until(
   #     expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'chosen-single')))
    # web_element_select = Select(chrome_web_driver.find_element(By.CLASS_NAME, 'form-control dib search-chosen ember-view ember-chosenselect form-control chosen-rtl'))
    chrome_web_driver.get(url + '/search')
    #select = Select(WebDriverWait(chrome_web_driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH,
     #                                                                                                       "//*[contains(@href,'סכום')]"
      #                                                                                                      ))))
    #select.select_by_index(1)
    z = WebDriverWait(chrome_web_driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH,
                                                                                                           "//*[contains(text(),'סכום')]/following")))
    z.click()
    #z.send_keys(Keys.ARROW_DOWN)
    #z.send_keys(Keys.RETURN)

    #// *[ @ id = "ember978_chosen"] / div / ul / li[1]
    #// *[ @ id = "ember1033"] / option[4]
    # select = Select(chrome_web_driver.find_element_by_xpath('// * [ @ id = "ember1033_chosen"] / a / span'))
    # select.select_by_value("Test")
    # // *[ @ id = "ember978_chosen"] / a / span
    # # ember993_chosen > a > span
    # document.querySelector("#ember993_chosen > a > span")
    # // *[ @ id = "ember978_chosen"] / a

    #         // * [ @ id = "ember1033_chosen"] / a / span
                                     #                                           // * [ @ id = "ember1048_chosen"] / a
                                       #                                                                             // * [ @ id = "ember1058_chosen"]
    # print(web_element_select.all_selected_options())

    # for _ in web_element_select[:1]:
    #   print(Select(_).options.value)

    # selections = WebDriverWait(chrome_web_driver, 30).until(
    #     expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'selected')))
    # print(selections.options)
#    for _ in selections:
 #       Select(_).select_by_index(1)

















    # chrome_web_driver.quit()



