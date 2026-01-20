import pytest
from selenium import webdriver
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

class TestSearchWiki:
    
    def read_data_from_file(file_path):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        DATA_FILE = os.path.join(BASE_DIR, "data.csv")
        with open(DATA_FILE, mode='r') as abc:
            csv_reader = csv.DictReader(abc)
            keywords = []
            for row in csv_reader:
                keywords.append(row['keyword'])
            return keywords
        
    testdata = read_data_from_file("data.csv")
        
    @pytest.mark.parametrize("keyword",testdata)
    def test_search_wikipedia(self, driver, keyword):
        search_box = driver.find_element(By.NAME,"search")
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.ENTER)
        sleep(5)