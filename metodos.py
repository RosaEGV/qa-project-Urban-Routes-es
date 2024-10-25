from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Keys
import data
import codigo
import localizadores
from localizadores import UrbanRoutesPageL


class UrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver
        self.locators = UrbanRoutesPageL

    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 15).until(
            expected_conditions.visibility_of_element_located(self.locators.from_field))

    def wait_for_page_comfort(self):
        WebDriverWait(self.driver, 15).until(
            expected_conditions.visibility_of_element_located(self.locators.fare_comfort))

#ELIGE UNA RUTA
    def set_from(self,from_field):
        self.driver.find_element(*self.locators.from_field).send_keys(from_field)

    def set_to(self,to_field):
        self.driver.find_element(*self.locators.to_field).send_keys(to_field)

    def get_from(self):
        return self.driver.find_element(*self.locators.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.locators.to_field).get_property('value')

    # ELIGE LA TARIFA CONFORT
    def click_order_a_taxi_button(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(self.locators.order_a_taxi_button))
        self.driver.find_element(*self.locators.order_a_taxi_button).click()

    def click_fare_comfort(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(self.locators.fare_comfort))
        self.driver.find_element(*self.locators.fare_comfort).click()

    def get_fare_comfort(self):
        return self.driver.find_element(*self.locators.fare_text).text

    def wait_for_phone_number(self):
            WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable(self.locators.button_phone_number))
        #RELLENA EL CAMPO NUMERO DE TELEFONO
    def click_button_phone_number(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(self.locators.button_phone_number))
        self.driver.find_element(*self.locators.button_phone_number).click()


    def set_field_number(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(self.locators.field_number))
        self.driver.find_element(*self.locators.field_number).send_keys(data.phone_number)

    def click_button_next(self):
        self.driver.find_element(*self.locators.button_next).click()


    def set_confirmation_code(self):
        code = codigo.retrieve_phone_code(driver= self.driver)
        self.driver.find_element(*self.locators.confirmation_code).send_keys(code)

    def click_confirmation_button(self):
        self.driver.find_element(*self.locators.confirmation_button).click()

    def get_phone_number(self):
        return self.driver.find_element(*self.locators.button_phone_number).text

    def wait_for_field_pay(self):
            WebDriverWait(self.driver, 5).until(
                expected_conditions.element_to_be_clickable(self.locators.field_pay))

    #AGREGAR TARJETA DE CREDITO

    def click_field_pay(self):
        WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located(self.locators.field_pay))
        self.driver.find_element(*self.locators.field_pay).click()

    def click_plus_add_card_button(self):
        self.driver.find_element(*self.locators.plus_add_card_button).click()

    def click_field_card(self):
        self.driver.find_element(*self.locators.field_card).click()

    def set_field_card(self):
        self.driver.find_element(*self.locators.field_card).send_keys(data.card_number)

    def click_cvv_field_code(self):
        WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located(self.locators.cvv_field_code))
        self.driver.find_element(*self.locators.cvv_field_code).click()

    def set_cvv_field_code(self):
        self.driver.find_element(*self.locators.cvv_field_code).send_keys(data.card_code)

    def click_text_add_card(self):
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(self.locators.cvv_field_code))
        self.driver.find_element(*self.locators.text_add_card).click()

    def click_add_button(self):
        self.driver.find_element(*self.locators.add_button).click()

    def click_close_button(self):
        WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located(self.locators.close_button))
        self.driver.find_element(*self.locators.close_button).click()

    def check_close_button_is_enabled(self):
        return self.driver.find_element(*self.locators.close_button).is_enabled()

    def wait_for_field_message_driver(self):
            WebDriverWait(self.driver, 5).until(
                expected_conditions.element_to_be_clickable(self.locators.field_message_driver))
    #MENSAJE AL CONDUCTOR
    def click_field_message_driver(self):
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(self.locators.field_message_driver))
        self.driver.find_element(*self.locators.field_message_driver).click()

    def set_field_message_driver(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(self.locators.field_message_driver))
        self.driver.find_element(*self.locators.field_message_driver).send_keys(data.message_for_driver)

    def verify_message(self):
        return self.driver.find_element(*self.locators.field_message_driver).get_property('value')


    def wait_for_button_accessory(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.locators.accessory_button))
    #ADICIONAR ACCESORIOS

    def click_accessory_button(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(self.locators.accessory_button))
        self.driver.find_element(*self.locators.accessory_button).click()

    def check_accessory_is_enabled(self):
        return self.driver.find_element(*self.locators.accessory_button).is_enabled()

    def wait_for_ice_button(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.locators.plus_ice_button))
    #ADICIONAR DOS HELADOS

    def click_plus_ice_button(self):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(self.locators.plus_ice_button))
        self.driver.find_element(*self.locators.plus_ice_button).click()
        self.driver.find_element(*self.locators.plus_ice_button).click()


    def get_ice_cream_counter(self):
        return self.driver.find_element(*self.locators.ice_cream_counter).text



    def wait_for_end_button(self):
        WebDriverWait(self.driver, 15).until(
            expected_conditions.visibility_of_element_located(self.locators.end_order_a_taxi))

    #PEDIR EL TAXI
    def click_end_order_a_taxi(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(self.locators.end_order_a_taxi))
        self.driver.find_element(*self.locators.end_order_a_taxi).click()

    def check_modal_is_enabled(self):
        return self.driver.find_element(*self.locators.modal_taxi).is_enabled()