El repositorio con el codigo completo se encuentra en el siguiente enlace. <https://github.com/Lonnath/MascotasYMascotas-API>

# API REST

Se realiza un proyecto en Django para mostrar por medio de una API Rest los resultados de consultas a base de datos en la cual se guardan registros sobre mascotas adoptadas.

# Configuracion

Para modificar el acceso a la base de datos se habilitó el archivo .env, así se definen las variables del entorno de manera mas sencilla y manejable.

# Peticiones Permitidas

Se definieron dos peticiones las cuales hacen referencia a las siguientes consultas, se anexa un ejemplo de petición url:

- Listar todas las mascotas URL: http://dominio/api/mascotas?parametro=22, el valor del parametro no es obligatorio ni se debe escribir para realizar la consulta correctamente.
- Listas los propietarios que no tienen mascotas URL: http://dominio/api/mascotas-no-adoptadas.

# Instalación

Para la instalación de todas las librerias se recomienda el uso del comando **pip install -r requirements.txt**, posicionandose en la carpeta raiz de donde se ubique el proyecto.

# Librerias Usadas

- django-cors-headers
- dj-database-url
- Django
- sqlparse
- mysqlclient
- django-environ
