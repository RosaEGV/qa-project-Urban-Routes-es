from metodos import UrbanRoutesPage
import data
from localizadores import UrbanRoutesPageL
# import codigo
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.routes_page = UrbanRoutesPage(cls.driver)
        cls.loc = UrbanRoutesPageL()
        cls.driver.get(data.urban_routes_url)

#CONFIGURAR LA DIRECCION

    def test_set_route(self):
        self.routes_page.wait_for_load_home_page()
        self.routes_page.set_from(data.address_from)
        self.routes_page.set_to(data.address_to)
        assert self.routes_page.get_from() == data.address_from
        assert self.routes_page.get_to() == data.address_to

#SELECIONAR TARIFA COMFORT

    def test_choose_fare(self):
        self.routes_page.click_order_a_taxi_button()
        self.routes_page.click_fare_comfort()
        assert self.routes_page.get_fare_comfort() == 'Comfort'

#RELLENAR EL NUMERO DE TELEFONO

    def test_phone_verification(self):
        self.routes_page.wait_for_phone_number()
        self.routes_page.click_button_phone_number()
        self.routes_page.set_field_number()
        self.routes_page.click_button_next()
        self.routes_page.set_confirmation_code()
        self.routes_page.click_confirmation_button()
        after = self.routes_page.get_phone_number()
        assert after == data.phone_number
#AGREGAR NUMERO DE TARJETA
    def test_pay_card(self):
        self.routes_page.click_field_pay()
        self.routes_page.click_plus_add_card_button()
        self.routes_page.set_field_card()
        self.routes_page.set_cvv_field_code()
        self.routes_page.click_text_add_card()
        self.routes_page.click_add_button()
        self.routes_page.click_close_button()
        assert self.routes_page.check_close_button_is_enabled()
#AGREGAR MENSAJE PARA EL CONDUCTOR
    def test_message_driver(self):
        self.routes_page.wait_for_field_message_driver()
        self.routes_page.set_field_message_driver()
        assert self.routes_page.verify_message() == data.message_for_driver

#AGREGAR MANTA Y PANUELOS
    def test_accessory(self):
        self.routes_page.click_accessory_button()
        assert self.routes_page.check_accessory_is_enabled()
#AGREGAR 2 HELADOS
    def test_number_ice(self):
        self.routes_page.click_plus_ice_button()
        numbers = self.routes_page.get_ice_cream_counter()
        assert numbers == '2'
#VERIFICAR EL MODAL
    def test_end_button(self):
        self.routes_page.click_end_order_a_taxi()
        assert self.routes_page.check_modal_is_enabled()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
