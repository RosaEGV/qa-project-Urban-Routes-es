Proyecto Urban Routes
Pruebas automatizadas con Selenium en Python para verificar las funciones de Urban Routes
Rosa Guzman Valencia Cohort 14

DESCRIPCION
Selenium es una herramienta de código abierto que se utiliza para automatizar las pruebas realizadas en los navegadores web.
Selenium WebDriver. Selenium WebDriver es el sucesor de Selenium Remote Control. Es el componente más utilizado de Selenium. El mismo permite a los usuarios escribir su código en distintos lenguajes de programación e interactuar con el navegador seleccionado.En el siguiente proyecto se realizaron pruebas automatizadas para la pagina de la aplicacion de Urban Routes con la ayuda de Selenium y PyTest.

Lo cual es una gran ventaja sobre otras herramientas de prueba. Otras razones detrás de la creciente popularidad de Selenium son:

Los scripts de prueba se pueden escribir en cualquiera de estos lenguajes de programación: Java, Python, C #, PHP, Ruby, Perl y .Net
Las pruebas se pueden realizar en cualquiera de estos sistemas operativos: Windows, Mac o Linux
Las pruebas se pueden llevar a cabo utilizando cualquier navegador: Mozilla Firefox, Internet Explorer, Google Chrome, Safari u Opera
Se puede integrar con herramientas como TestNG y JUnit para gestionar casos de prueba y generar informes
Se puede integrar con Maven, Jenkins y Docker para lograr pruebas continuas.

Dentro de este proyecto se crearon varios archivos cada uno con diferentes finalidades. Se corrieron las pruebas en base a la funcionalidad de la pagina web.
PASOS A SEGUIR:

1. SE CREARON LOS SIGUIENTES ARCHIVOS:  data.py, localizadores.py, metodo.py, codigo.py , main.py y README
2. SE EMPEZO A TRABAJAR CON LOS LOCALIZADORES EN LA APLICACION DE URBAN ROUTES
3. SE CREARON LOS METODOS PARA LLEGAR A LA PEDIDA DE UN TAXI
4. SE CREARON TEST PARA COMPPROBAR CADA PASO DE PEDIDA DE TAXI

TECNOLOGIAS A NECESITAR:
-SELENIUM WEBDRIVER
-PYCHARM
-PYTEST
-DEVTOOLS


PASOS A SEGUIR PARA LA AUTOMATIZACION:

-Configurar la dirección
-Seleccionar la tarifa Comfort.
-Rellenar el número de teléfono.
-Agregar una tarjeta de crédito. 
-Escribir un mensaje para el controlador. 
-Pedir una manta y pañuelos.
-Pedir 2 helados.
-Aparece el modal para buscar un taxi.

CONTENIDO DE CADA ARCHIVO EN EL PROYECTO DE URBAN ROUTES

DATA:
AQUI VAMOS A METER TODAA LOS PARAMETROS A UTILIZAR:URL, NUMEROS DE TELEFONO, NUMERO DE CODIGO, ETC

LOCALIZADORES:
AQUI VAMOS A METER TODOS LOS LOCALIZADORES DE LOS ELEMENTOS A UTILIZAR , QUE CON AYUDA DEL DEVTOOLS ANALIZAREMOS CUAL OCUPAREMOS

CODIGO:
ESTE ES UN CODIGO YA PROPORCIONADO POR LA PLATAFORMA , PARA LLENAR EL CAMPO CODIGO DE CONFIRMACION EN EL CAMPO NUMERO DE TELEFONO

METODOS:
EN ESTE ARCHIVO CREAREMOS CADA UNO DE LOS PASOS PARA CONSEGUIR UN VIAJE EN ESTA APLICACION EN LA TARIFA COMFORT

MAIN:

EN ESTE CREAMOS LOS DIFERENTES TEST PARA PROBAR LA AUTOMATIZACION DE LA PEDIDA DE UN TAXI

METODOLOGIA

-SE REALIZO EL RECLUTAMIENTO DE LOS LOCALIZADORES PARA CADA UNO DE LOS PASOS SOLICITADOS PARA EL PROYECTO, ESTOS LOCALIZADORES FUERON EXTRAIDOS CON AYUDA DEL DEVTOOL, CADA UNO FUE ELEGIDO EN BASE A CRITERIOS YA CONOCIDOS Y AL MOMENTO DE REALIZAR LOS METODOS ALGUNOS FUERON CAMBIADOS O ADICIONADOS
-YA TENIENDO LOS LOCALIZADORES SE PROCEDE A CREAR LOS METODOS PARA CADA UNO DE LOS PASOS REQUERIDOS PARA LA PEDIDA DE UN TAXI EN LA APLICACION URBAN ROUTES
-SE UTILIZARON METODOS CLICK, SET, GET, CHECK, WAIT.DRIVER POR SUPUESTO.
-POSTERIORMENTE  SE REALIZARON TEST PARA CADA UNA DE LAS PRUEBAS EN LAS CUALES SE INCLUYERON LOS DECORADORES SETUP CLASS Y TEARDOWN CLASS
-DENTRO DE ESTAS PRUEBAS SE COLOCARON LOS METODOS CORRESPONDIENTES EN CADA UNO DE LOS PASOS REQUERIDOS PARA CADA PUNTO SOLICITADO
-TAMBIEN SE REALIZARON EN CADA PASA CON ASSERT CON LA FINALIDAD DE PROBAR O VERIFICAR  CIERTO REQUISITO PARA CADA PASO


CONCLUSION:

ESTE PROYECTO ES MUY INTERESANTE PORQUE NOS PERMITE UTILIZAR LA AUTOMATIZACION MEDIANTE SELENIUM Y LA IDE PYCHARM, EL CODIGO DE SELENIUM ES FACIL DE DIGERIR, PERO ES MUY IMPORTANTE PARA UN PROYECTO COMO ESTE, CONOCER Y SELECCIONAR ADECUADAMENTE LOS LOCALIZADORES PARA CADA PASO, YA QUE ESTO ES ESENCIAL PARA LA REALIZACION Y EL EXITO DE LAS AUTOMATIZACIONES.
