from flask_testing import LiveServerTestCase
from selenium import webdriver
from urllib.request import urlopen
from flask import url_for

from application import app, db, models

class TestBase(LiveServerTestCase):
    TEST_PORT = 5050 # test port, doesn't need to be open

    def create_app(self):

        app.config.update(
            SQLALCHEMY_DATABASE_URI="",
            SECRET_KEY="",
            LIVESERVER_PORT=self.TEST_PORT,
            
            DEBUG=True,
            TESTING=True
        )

        return app

    def setUp(self):
        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless')

        self.driver = webdriver.Chrome(options=chrome_options)

        # db.create_all() # create schema before we try to get the page

        self.driver.get(f'http://localhost:{self.TEST_PORT}')

    def tearDown(self):
        self.driver.quit()

        # db.drop_all()

    def test_server_is_up_and_running(self):
        response = urlopen(f'http://localhost:{self.TEST_PORT}')
        self.assertEqual(response.code, 200)

class TestNavigate(TestBase):

    def test_album_menu(self):
        self.driver.find_element_by_xpath("/html/body/table/tbody/tr/td[1]/a").click()
        self.assertIn(url_for("_album"), self.driver.current_url)

    def test_composer_menu(self):
        self.driver.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/a").click()
        self.assertIn(url_for("_composer"), self.driver.current_url)
    
    def test_label_menu(self):
        self.driver.find_element_by_xpath("/html/body/table/tbody/tr/td[3]/a").click()
        self.assertIn(url_for("label"), self.driver.current_url)

    def test_category_menu(self):
        self.driver.find_element_by_xpath("/html/body/table/tbody/tr/td[4]/a").click()
        self.assertIn(url_for("category"), self.driver.current_url)

class TestAdd(TestBase):
    def test_composer_add(self):
        self.driver.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/a").click()
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys("NEW COMPOSER")
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        response = models.composer.query.filter(models.composer.name == "NEW COMPOSER").count()
        self.assertEqual(response, 1)

    def test_label_add(self):
        self.driver.find_element_by_xpath("/html/body/table/tbody/tr/td[3]/a").click()
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys("NEW LABEL")
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        response = models.media_label.query.filter(models.media_label.name == "NEW LABEL").count()
        self.assertEqual(response, 1)

    def test_category_add(self):
        self.driver.find_element_by_xpath("/html/body/table/tbody/tr/td[4]/a").click()
        self.driver.find_element_by_xpath('//*[@id="description"]').send_keys("NEW CATEGORY")
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        response = models.music_category.query.filter(models.music_category.description == "NEW CATEGORY").count()
        self.assertEqual(response, 1)












