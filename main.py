import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time


class test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"src/drivers/chromedriver.exe")
        driver = self.driver
        driver.get('https://dondoctorrey.azurewebsites.net/paciente')
        driver.maximize_window()
       #driver.implicitly_wait(30)
        title_expected = 'Pruebas dondoctor'
        get_title = self.driver.title
        self.assertEqual(get_title, title_expected, 'No estas en el portal esperado')
        #assert get_title, 'Pruebas dondoctor'
        time.sleep(3)


    def test_ir_registrar(self):

        c_video = self.driver.find_element(By.XPATH, "//button[@class='close-button close-modal-button']" )
        c_video.click()
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, 'Entrar').click()
        time.sleep(1)

  #  def test_registrar_paciente(self):

        #registry = self.driver.find_element(By.ID, 'registry')

        # registry= self.driver.find_element(By.ID, "//a[@id='registry']")
        registry= self.driver.find_element(By.ID, '// *[ @ id = "registry"]').click()

       #  registry = self.driver.find_element(By.ID, 'registry')
        print("AQUI", registry)
        self.assertEqual(registry, 'Regístrate aquí')



if __name__=="__main__":
    unittest.main()