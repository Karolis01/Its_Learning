from selenium.webdriver.common.by import By


class TestData:
    BASE_URL = "https://itslearning.com/no/"

    SCRENSHOT_PATH = "/Users/karolis/Documents/pythonProject/Its_Learning/Tests"
    WHOLE_PAGE = (By.TAG_NAME, "body")
    COOKIES = (By.ID, "onetrust-accept-btn-handler")
    SCREEN = "./Screen/"
    SKOLE_PAGE = (By.XPATH, "//a[@class='menu-link main-menu-link'][normalize-space()='Skole']")
    HOYERE_UTDANNING_PAGE = (By.XPATH, "//a[@class='menu-link main-menu-link'][normalize-space()='Høyere utdanning']")
    PRIS_PAGE = (By.XPATH, "//a[@class='menu-link main-menu-link'][normalize-space()='Pris']")
    GRATIS_DEMO_PAGE = (By.XPATH, "//a[@class='menu-link main-menu-link'][normalize-space()='Gratis demo']")
    KONTAKT_OSS = (By.XPATH, "//a[contains(text(),'Kontakt oss')]")
    PARTNERE = (By.XPATH, "//p[contains(text(),'Våre partnere ›')]")
    TJENESTER = (By.XPATH, "//p[contains(text(),'Våre tjenester ›')]")
    HISTORIE = (By.XPATH, "//p[contains(text(),'Vår historie ›')]")


