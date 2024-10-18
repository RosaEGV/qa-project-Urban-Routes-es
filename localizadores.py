from selenium.webdriver.common.by import By



class UrbanRoutesPage:

  #SELECCIONAR LA TARIFA COMFORT
  from_field = (By.ID, 'from')
  to_field = (By.ID, 'to')
  order_a_taxi_button = (By. CLASS_NAME,"button round" )
  fare_comfort = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[2]")

  #RELLENA NUMERO DE TELEFONO
  button_phone_number = (By.CLASS_NAME, "np-text")
  field_number = (By.ID, "phone")
  button_next = (By.XPATH, "//*[@id='root']/div/div[1]/div[2]/div[1]/form/div[2]/button)")
  confirmation_code = (By.XPATH, "//*[@id='code']")
  confirmation_button = (By.XPATH, "//*[@id='root']/div/div[1]/div[2]/div[2]/form/div[2]/button[1] ")

  #AGREGAR TARJETA
  field_pay = (By.CLASS_NAME, "pp-button filled")
  plus_add_card_button = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[3]/div/img")
  field_card = (By.ID, "number")
  cvv_field_code = (By.XPATH, "//*[@id='code']")
  text_add_card = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/div")
  add_button = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/form/div[3]/button[1] ")
  close_button = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/button")

  #MENSAJE PARA EL CONDUCTOR
  field_message_driver = (By.ID, "comment")

  #ANADIR MANTA Y PANUELOS
  accessory_button = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span")

  #ANADIR  HELADO
  plus_ice_button = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]")

  #MODAL PARA PEDIR UN TAXI
  end_order_a_taxi = (By.CLASS_NAME, "smart-button-main")
  #MODAL PARA ESPERAR CONDUCTOR

