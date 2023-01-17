# MiniMasterClass de Api REST con Django

¿No crees en la magia? Pues después de esta MasterClass lo harás xD

En esta MasterClass vamos a hacer una Api REST básica con Django y Django RestFramework. La MasterClass se centrará en explotar las ventajas de los Frameworks opinados y con 'baterías cargadas', los cuales, por el momento, no tienen parangón en el ecosistema de JavaScript, el cual se centra más en seguir una filosofía de ligereza y de escalabilidad a medida que la aplicación lo va necesitando.


# DRY y Django

La clave de Django es seguir la filosofía del *Don't repeat yourself*, para lo cual, el Framework abstrae la lógica de las necesidades **CRUD** y las validaciones pertinentes a partir de los esquemas que se extraen de su **ORM**.


# Virtualenv

Antes de que se impulsaran los servicios para *contenedorizar* aplicaciones (como por ejemplo, Docker), las aplicaciones de Python ya utilizaban algo similar para congelar el entorno de ejecución de sus Apps y facilitar su exportación. Estamos hablando de los *virtual environments* y el primer paso para utilizar Django (y casi cualquier app con Python) es crear el entorno virtual dentro del cual instalaremos los requisitos para nuestra App.

Comando en Windows:

    python -m venv venv

  Comando en Unix:

    python3 -m venv venv

Para activar este entorno virtual y poder instalar Django y Django Restframework debemos ejecutar el siguiente comando:

Comando en Windows:

    \venv\Scripts\activate.bat

  Comando en Unix:

    source ./venv/bin/activate


## Django

Para instalar Django, tan solo debemos recurrir a *pip* (el *npm* de Python). Una vez activado nuestro entorno virtual procederemos con la instalación de nuestro Framework:

    pip install django

## Django rest_framework

Para instalar Django RestFramework, el miniFramework que habilita a Django para poder serializar nuestra aplicación en formato JSON, además de dotarnos de métodos para automatizar nuestras Vistas, debemos ejecutar:


pip install djangorestframework


## Iniciando nuestro proyecto

De nuevo, con el entorno virtual activado, ejecutamos:

    django-admin startproject nombre_proyecto .


## En Django, el trabajo se divide en APP's

En Django las responsabilidades se dividen en App's que son totalmente reutilizables dentro de otros proyectos. Al final, son como aplicaciones estancas que pueden enchufarse en cualquier otro proyecto con Django. Para generar una App, solo debemos ejecutar:

django-admin startapp nombre_app

## Activar las aplicaciones instaladas

Django necesita saber que hemos instalado Restframework y, también, que hemos generado una App nueva. Para ello iremos al archivo de settings.py y en el apartado de INSTALLED_APPS las añadiremos:

    INSTALLED_APPS  = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'nuestra_app',
    'rest_framework',



## Manos a la obra

Lo siguiente será hundir las manos en el fango y ponernos a trabajar ya en nuestra App. Para ello empezaremos a trabajar en el archivo models.py de la propia App y, a partir de ahí, en la MasterClass explicaremos como es, precisamente este archivo, el eje que vertebrará toda la lógica de nuestras aplicaciones con Django, pues es a partir de aquí es desde donde Django hará su magia para abstraer el CRUD y para deducir las validaciones que necesitamos extendiéndolas a los formularios (si hacemos frontend) o a los JSON (si hacemos una Api REST).
