from Pages.PageActions import PageActions
from Tests.test_base import BaseTest


class TestHorizontalScrolling(BaseTest):

    def test_homepage(self):
        self.pageActions = PageActions(self.driver)
        self.pageActions.accept_cookies()
        self.pageActions.horizontal_scroll()
        self.pageActions.do_screenshot("./Screen/homepage1.png")
        self.pageActions.horizontal_scroll_off()
        self.pageActions.do_screenshot("./Screen/homepage2.png")
        self.pageActions.do_compare_img("homepage1.png", "homepage2.png")

    def test_skole_page(self):
        self.pageActions = PageActions(self.driver)
        self.pageActions.skole_page()
        self.pageActions.horizontal_scroll()
        self.pageActions.do_screenshot("./Screen/skole1.png")
        self.pageActions.horizontal_scroll_off()
        self.pageActions.do_screenshot("./Screen/skole2.png")
        self.pageActions.do_compare_img("skole1.png", "skole2.png")

    def test_utdanning_page(self):
        self.pageActions = PageActions(self.driver)
        self.pageActions.utdanning_page()
        self.pageActions.horizontal_scroll()
        self.pageActions.do_screenshot("./Screen/utdanning1.png")
        self.pageActions.horizontal_scroll_off()
        self.pageActions.do_screenshot("./Screen/utdanning2.png")
        self.pageActions.do_compare_img("utdanning1.png", "utdanning2.png")

    def test_pris_page(self):
        self.pageActions = PageActions(self.driver)
        self.pageActions.pris_page()
        self.pageActions.horizontal_scroll()
        self.pageActions.do_screenshot("./Screen/pris1.png")
        self.pageActions.horizontal_scroll_off()
        self.pageActions.do_screenshot("./Screen/pris2.png")
        self.pageActions.do_compare_img("pris1.png", "pris2.png")

    def test_gratis_demo_page(self):
        self.pageActions = PageActions(self.driver)
        self.pageActions.gratis_demo_page()
        self.pageActions.horizontal_scroll()
        self.pageActions.do_screenshot("./Screen/gratisDemo1.png")
        self.pageActions.horizontal_scroll_off()
        self.pageActions.do_screenshot("./Screen/gratisDemo2.png")
        self.pageActions.do_compare_img("gratisDemo1.png", "gratisDemo2.png")

    def test_kontakt_oss_page(self):
        self.pageActions = PageActions(self.driver)
        self.pageActions.kontakt_oss_page()
        self.pageActions.horizontal_scroll()
        self.pageActions.do_screenshot("./Screen/kontaktOss1.png")
        self.pageActions.horizontal_scroll_off()
        self.pageActions.do_screenshot("./Screen/kontaktOss2.png")
        self.pageActions.do_compare_img("kontaktOss1.png", "kontaktOss2.png")

    def test_partnere_page(self):
        self.pageActions = PageActions(self.driver)
        self.pageActions.partnere_page()
        self.pageActions.horizontal_scroll()
        self.pageActions.do_screenshot("./Screen/partnere1.png")
        self.pageActions.horizontal_scroll_off()
        self.pageActions.do_screenshot("./Screen/partnere2.png")
        self.pageActions.do_compare_img("partnere1.png", "partnere2.png")

    def test_tjenester_page(self):
        self.pageActions = PageActions(self.driver)
        self.pageActions.tjenester_page()
        self.pageActions.horizontal_scroll()
        self.pageActions.do_screenshot("./Screen/tjenester1.png")
        self.pageActions.horizontal_scroll_off()
        self.pageActions.do_screenshot("./Screen/tjenester2.png")
        self.pageActions.do_compare_img("tjenester1.png", "tjenester2.png")

    def test_historie_page(self):
        self.pageActions = PageActions(self.driver)
        self.pageActions.historie_page()
        self.pageActions.horizontal_scroll()
        self.pageActions.do_screenshot("./Screen/historie1.png")
        self.pageActions.horizontal_scroll_off()
        self.pageActions.do_screenshot("./Screen/historie2.png")
        self.pageActions.do_compare_img("historie1.png", "historie2.png")

