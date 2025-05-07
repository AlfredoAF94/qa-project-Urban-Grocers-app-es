# Proyecto Urban Grocers 

Nombre el proyecto: Jorge Alfredo Alvarado Ferral, 28 grupo - 7 sprint

Descripción del proyecto: El proyecto pone a prueba 9 casos de solicitudes API para Urban Grocers. Específicamente para el campo "Name". Entre las pruebas positivas y negativas, se testea la longitud de los caracteres, incluyendo letras, números y caracteres especiales (sin olvidar el campo vacío). Todo esto, se puso a prueba a través de PyCharm.

Fuente de documentación utilizada: ApiDOC.

Tecnologías y técnicas utilizadas: PyThon test con PyTest. Se utilizó ChatGPT para confirmar los datos de los archivos .py, así como acompletar el esqueleto de cada uno. Una vez se corría una prueba de manera positiva, se pasaba al siguiente cambiando el string del nombre para cada caso, así como el nombre de la prueba; en caso de que el test fallara, se revisaba la respuesta del PyCharm, en caso de no entenderla, se solicitaba el análisis a ChatGPT para corregir la prueba. También se utilizó el material de los anteriores ejercicios para la orientación inicial de contenido para cada ventana.
Crear entorno virtual en la consola: python -m venv venv
Instalación de librerías en la consola: pip install -r requirements.txt
Instalación de pytest en la consola: pip install pytest


Pasos para ejecutar las pruebas: En la ventana de create, se importaron las ventanas necesarias para el proyecto. Posteriormente, se le pidió a ChatGPT armar la primera prueba. Con base en la primera prueba, se fueron añadiendo las demás (ejecutando en individual cada una) cambiándole el nombre para la prueba y el valor de prueba. Una vez se llegó a la prueba 8, se añadió el negative assert para ejecutar la prueba 8 y 9. En cada prueba se hizo un commit para ir guardando los resultados.

