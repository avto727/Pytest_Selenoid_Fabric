import pytest
from selenium.webdriver.common.keys import Keys

@pytest.mark.usefixtures("create_driver")
class TestGoogleHomePageTwo:


    @pytest.mark.only
    def test_navigate_to_home_page_2(self):
        print('Onening the page')
        self.base_page.driver.get('http://duckduckgo.com/')
        print('typing search request')
        search_input = self.base_page.driver.find_element_by_css_selector('input[id="search_form_input_homepage"]').send_keys(
            'selenoid' + Keys.ENTER)
        # search_input = driver.find_element_by_tag_name('body').send_keys(Keys.ENTER)
        # search_input = driver.find_element_by_css_selector('#search_form').click()

    # @pytest.mark.only
    # def test_navigate_to_home_page_2(self):
    #     self.base_page.navigate_to_home_page() \
    #          .enter_text_and_search("Github")
    #         # .click_on_the_first_link()

    # @pytest.mark.only
    # def test_navigate_to_home_page_3(self):
    #     self.base_page.navigate_to_home_page() \
    #          .enter_text_and_search("Github")
