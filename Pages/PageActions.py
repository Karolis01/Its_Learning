from Config.config import TestData
from Pages.BasePage import BasePage
from Tests.compareImage import Comparing


class PageActions(BasePage, Comparing):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def accept_cookies(self):
        self.do_accept_cookies(TestData.COOKIES)

    def horizontal_scroll(self):
        self.driver.maximize_window()
        self.do_horizontal_scroll(TestData.WHOLE_PAGE)

    def horizontal_scroll_off(self):
        self.do_horizontal_scroll_off(TestData.WHOLE_PAGE)

    def do_screenshot(self, text):
        self.take_screenshot(TestData.WHOLE_PAGE, text)

    def skole_page(self):
        self.go_to_skole_page(TestData.SKOLE_PAGE)

    def utdanning_page(self):
        self.go_to_utdanning_page(TestData.HOYERE_UTDANNING_PAGE)

    def pris_page(self):
        self.go_to_pris_page(TestData.PRIS_PAGE)

    def gratis_demo_page(self):
        self.go_to_gratis_demo_page(TestData.GRATIS_DEMO_PAGE)

    def kontakt_oss_page(self):
        self.go_to_kontakt_oss_page(TestData.KONTAKT_OSS)

    def partnere_page(self):
        self.go_to_partnere_page(TestData.PARTNERE)

    def tjenester_page(self):
        self.go_to_tjenester_page(TestData.TJENESTER)

    def historie_page(self):
        self.go_to_historie_page(TestData.HISTORIE)

    def do_compare_img(self, name1, name2):
        self.do_compare(name1, name2)
