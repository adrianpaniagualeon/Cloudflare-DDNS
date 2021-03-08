# Cloudflare DDNS

## ¿Qué hace este script?
Este script permite la actualización de la IP pública de la maquina que lo ejecuta en los servidores DNS de Cloudflare. Para evitar sobrecargar la API de Cloudflare, se ejecuta cada 5 minutos hasta que el usuario decida parar el servicio.

## ¿Cómo puedo colaborar?
Existen dos formas de colaborar:
- Añadiendo nuevas funcionalidades al bot mediante _pull-request_. 
- Aportación económica: Puedes aportar tu granito de arena por [Paypal](https://paypal.me/panleoad)
- Invitarme a un café: Me puedes invitar a un café a través de [Ko-Fi](https://ko-fi.com/adrianpaniagualeon)

## ¿Necesita alguna librería externa?
Si, este script necesita la librería [Requests](https://requests.readthedocs.io/en/master/). Puedes instalarla con el siguiente comando "pip install requests"

## ¿Qué datos necesito para autenticarme?
|DATO|INFORMACIÓN|
|-|-|
|CLOUDFLARE_EMAIL|CORREO ELECTRÓNICO UTILIZADO PARA REGISTRARTE EN CLOUDFLARE|
|CLOUDFLARE_CLAVE|GLOBAL API KEY DE CLOUDFLARE. Puedes encontrarla en [https://dash.cloudflare.com/profile/api-tokens](https://dash.cloudflare.com/profile/api-tokens)|
|DOMAIN|DOMINIO QUE QUEREMOS ACTUALIZAR. En caso de querer actualizar cv.adrianpaniagua.es **SOLO** introduciremos adrianpaniagua.es|
|SUBDOMAIN|SUBDOMINIO QUE QUEREMOS ACTUALIZAR. En caso de querer actualizar blog.adrianpaniagua.es **SOLO** introduciremos adrianpaniagua.es. Si queremos actualizar el dominio principal, dejaremos este campo vacio|

Tienes que modificar el archivo ddns.py con tus datos para que el script funcione. Es muy importante no incluir espacios para que todo funcione correctamente.