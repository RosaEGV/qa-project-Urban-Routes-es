from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Keys
import data
import codigo
import localizadores


class UrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver


    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 15).until(
            expected_conditions.visibility_of_element_located(localizadores.UrbanRoutesPage.from_field))
#ELIGE LA TARIFA COMFORT
    def set_from(self):
        self.driver.find_element(*localizadores.UrbanRoutesPage.from_field).send_keys(data.address_from)

    def set_to(self):
        self.driver.find_element(*localizadores.UrbanRoutesPage.to_field).send_keys(data.address_to)

    def get_from(self):
        return self.driver.find_element(*localizadores.UrbanRoutesPage.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*localizadores.UrbanRoutesPage.to_field).get_property('value')

    def click_order_a_taxi_button(self):
        self.driver.find_element(*localizadores.UrbanRoutesPage.order_a_taxi_button).click()

    def click_fare_comfort(self):
        self.driver.find_element(*localizadores.UrbanRoutesPage.fare_comfort).click()

    def wait_for_phone_number(self):
            WebDriverWait(self.driver, 5).until(
                expected_conditions.element_to_be_clickable(localizadores.UrbanRoutesPage.button_phone_number))
        #RELLENA EL CAMPO NUMERO DE TELEFONO
    def click_button_phone_number(self):
        self.driver.find_element(*localizadores.UrbanRoutesPage.button_phone_number).click()

    def click_field_number(self):
        self.driver.find_element(*localizadores.UrbanRoutesPage.field_number).click()

    def set_field_number(self):
        self.driver.find_element(*localizadores.UrbanRoutesPage.field_number).send_keys(data.phone_number)

    def click_button_next(self):
        self.driver.find_element(*localizadores.UrbanRoutesPage.button_next).click()

    def set_confirmation_code(self):
        code = codigo.retrieve_phone_code(self)
        self.driver.find_element(*localizadores.UrbanRoutesPage.confirmation_code).send_keys(code)

    def click_confirmation_button(self):
        self.driver.find_element(*localizadores.UrbanRoutesPage.confirmation_button).click()

    def wait_for_field_pay(self):
            WebDriverWait(self.driver, 5).until(
                expected_conditions.element_to_be_clickable(localizadores.UrbanRoutesPage.field_pay))

    #AGREGAR TARJETA DE CREDITO
    def click_field_pay(self):
        self.driver.find_element(*localizadores.UrbanRoutesPage.field_pay).click()

    def click_plus_add_card_button(self):
        self.driver.find_element(*localizadores.UrbanRoutesPage.plus_add_card_button).click()

    def click_field_card(self):
        self.driver.find_element(*localizadores.UrbanRoutesPage.field_card).click()

    def set_field_card(self):
        self.driver.find_element(*localizadores.UrbanRoutesPage.field_card).send_keys(data.card_number)

    def click_cvv_field_code(self):
        self.driver.find_element(*localizadores.UrbanRoutesPage.cvv_field_code).click()

    def set_cvv_field_code(self):
        self.driver.find_element(*localizadores.UrbanRoutesPage.cvv_field_code).send_keys(data.card_code)

    def click_text_add_card(self):
        self.driver.find_element(*localizadores.UrbanRoutesPage.text_add_card).click()

    def click_add_button(self):
        self.driver.find_element(*localizadores.UrbanRoutesPage.add_button).click()

    def click_close_button(self):
        self.driver.find_element(*localizadores.UrbanRoutesPage.close_button).click()

    def wait_for_field_message_driver(self):
            WebDriverWait(self.driver, 5).until(
                expected_conditions.element_to_be_clickable(localizadores.UrbanRoutesPage.field_message_driver))
    #MENSAJE AL CONDUCTOR
    def click_field_message_driver(self):
        self.driver.find_element(*localizadores.UrbanRoutesPage.field_message_driver).click()

    def set_field_message_driver(self):
        self.driver.find_element(*localizadores.UrbanRoutesPage.field_message_driver).send_keys(data.message_for_driver)

    #ADICIONAR ACCESORIOS

    def click_accessory_button(self):
        self.driver.find_element(*localizadores.UrbanRoutesPage.accessory_button).click()

    #ADICIONAR DOS HELADOS

    def click_plus_ice_button(self):
        self.driver.find_element(*localizadores.UrbanRoutesPage.plus_ice_button).click()
        self.driver.find_element(*localizadores.UrbanRoutesPage.plus_ice_button).click()

    #PEDIR EL TAXI
    def click_end_order_a_taxi(self):
        self.driver.find_element(*localizadores.UrbanRoutesPage.end_order_a_taxi).click()


    #PASO PARA ELEGIR TARIFA COMFORT
    def choose_fare(self):
        self.set_from()
        self.set_to()
        self.click_order_a_taxi_button()
        self.click_fare_comfort()



