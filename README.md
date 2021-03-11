# Cloudflare DDNS

## ¿Qué hace este script?
Este script permite la actualización de la IP pública de la maquina que lo ejecuta en los servidores DNS de Cloudflare. Para evitar sobrecargar la API de Cloudflare, se ejecuta cada 5 minutos hasta que el usuario decida parar el servicio. 

## ¿Como puedo configurar el BOT de Telegram?
Para configurar el Bot de Telegram sigue los siguientes pasos:
- Envia a [https://t.me/BotFather](@BotFather) el comando `/newbot`
- Después enviale un mensaje con el nombre que quieres darle al Bot (Ej:`DDNS BOT`)
- A continuación envia el nombre de usuario que quieres poner a tu bot. El nombre de usuario tiene que acabar en bot y tiene que estar libre. (Ej: `adrianddnsbot`).
- A continuación, si todo ha funcionado, te enviará un Token que deberas introducir en el archivo ddns.py

Para obtener tu CID (Chat ID) envia el comando /start al bot [https://t.me/chatid_echo_bot](@chatid_echo_bot). Deberas introducir el número que te devueve en el archivo ddns.py


## ¿Necesita alguna librería externa?
Si, este script necesita la librería [Requests](https://requests.readthedocs.io/en/master/). Puedes instalarla con el siguiente comando "pip install requests"

## ¿Qué datos necesito para autenticarme?
|DATO|INFORMACIÓN|
|-|-|
|CLOUDFLARE_EMAIL|CORREO ELECTRÓNICO UTILIZADO PARA REGISTRARTE EN CLOUDFLARE|
|CLOUDFLARE_CLAVE|GLOBAL API KEY DE CLOUDFLARE. Puedes encontrarla en [https://dash.cloudflare.com/profile/api-tokens](https://dash.cloudflare.com/profile/api-tokens)|
|DOMAIN|DOMINIO QUE QUEREMOS ACTUALIZAR. En caso de querer actualizar cv.adrianpaniagua.es **SOLO** introduciremos adrianpaniagua.es|
|SUBDOMAIN|SUBDOMINIO QUE QUEREMOS ACTUALIZAR. En caso de querer actualizar cv.adrianpaniagua.es **SOLO** introduciremos cv (Si queremos actualizar el dominio principal, dejaremos este campo vacio)|
|TOKEN|TOKEN del Bot de Telegram|
|CID|Tu Chat ID de Telegram|
Tienes que modificar el archivo ddns.py con tus datos para que el script funcione. Es muy importante no introducir espacios para que todo funcione correctamente.

## ¿Cómo puedo colaborar?
Existen dos formas de colaborar:
- Añadiendo nuevas funcionalidades al bot mediante _pull-request_. 
- Aportación económica: Puedes aportar tu granito de arena por [Paypal](https://paypal.me/panleoad)
- Invitarme a un café: Me puedes invitar a un café a través de [Ko-Fi](https://ko-fi.com/adrianpaniagualeon)
