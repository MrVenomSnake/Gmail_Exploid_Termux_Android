# Guía para Ejecutar GmailExploid-1.0 en Android

GmailExploid-1.0 crea una cuenta de Gmail automáticamente llenando el formulario. **Importante**: Solo funciona parcialmente. Tendrás que resolver el CAPTCHA y verificar el teléfono manualmente. Usa solo para pruebas, no para crear cuentas masivas (viola reglas de Google).

## ¿Qué Necesitas?
- Un teléfono Android (versión 7 o superior).
- La app **Termux** (terminal para Android).
- Conexión a internet.

## Paso 1: Instalar Termux
1. Abre Google Play Store o F-Droid.
2. Busca "Termux".
3. Instala la app (elige F-Droid si puedes, es más actualizada).
4. Abre Termux. Verás una pantalla negra como una terminal de computadora.

## Paso 2: Preparar Termux
1. En Termux, escribe: `pkg update && pkg upgrade` y presiona Enter. Espera a que termine (puede tardar).
2. Instala Python: `pkg install python` y Enter.
3. Instala Chromium (navegador): `pkg install chromium` y Enter.
4. Instala herramientas: `pip install selenium webdriver-manager` y Enter.

## Paso 3: Descargar el Script
1. Copia los archivos del script a tu Android:
   - Crea una carpeta en tu teléfono (e.g., "ScriptGmail").
   - Descarga `GmailExploid-1.0.py` y `requirements.txt` desde tu PC (o copia el código).
   - Mueve los archivos a Termux: Usa un explorador de archivos para copiar a `/data/data/com.termux/files/home/ScriptGmail/`.
2. En Termux, ve a la carpeta: `cd ScriptGmail`.

## Paso 4: Ejecutar el Script
1. Escribe: `python GmailExploid-1.0.py` y presiona Enter.
2. El script te pedirá un proxy opcional (e.g., http://ip:port). Ingresa uno si quieres usar proxy para evitar bloqueos de IP, o deja en blanco.
3. El script abrirá un navegador invisible (headless) con user-agent rotativo y proxy si especificado, y llenará el formulario de Gmail.
4. Verás mensajes en pantalla, como "Browser started" y "Form filled".
5. Cuando diga "CAPTCHA detected", abre tu navegador normal (Chrome en Android) y ve a la página de Gmail manualmente.
6. Resuelve el CAPTCHA y completa la verificación telefónica tú mismo.
7. Las credenciales generadas se guardan en `generated_accounts.txt`.
8. Los logs se guardan en `gmail_exploit.log`.
9. El script esperará y luego dirá "Done".

## ¿Qué Hace el Script?
- Abre un navegador web invisible.
- Va a la página de registro de Gmail.
- Llena nombre, apellido, usuario y contraseña con datos inventados.
- Se detiene para que resuelvas el CAPTCHA y verifiques el teléfono.

## Nuevas Mejoras
- **Compatibilidad Mejorada con Android**: Detecta automáticamente el SO y configura Chromium correctamente.
- **Soporte para Proxies**: Permite ingresar un proxy para rotar IP y evitar bloqueos (útil para evadir detección de Google).
- **Técnicas de Evasión**: User-agents rotativos y delays aleatorios para simular comportamiento humano y reducir detección.
- **Logging**: Registra eventos en `gmail_exploit.log` para depuración.
- **Guardado de Credenciales**: Las cuentas generadas se guardan en `generated_accounts.txt`.
- **Manejo de Errores**: Mejorado con logging y reintentos implícitos.

Para usar proxy en Android, instala una app como Orbot (para Tor) y configura el proxy SOCKS (el script usa HTTP proxies; convierte si necesario).

## Problemas Comunes
- Si dice "Failed to start browser", reinstala Chromium: `pkg reinstall chromium`.
- Si es lento, espera más tiempo en conexiones lentas.
- No funciona en Android muy viejos (necesita buen procesador).
- Si falla, prueba en un emulador de Android en PC primero.

## Advertencias
- **Legal**: Crear cuentas así viola las reglas de Google. Puede bloquear tu IP.
- **Ético**: No uses para spam o cosas malas.
- **Seguridad**: No compartas tus datos. Usa solo para aprender.

Si no funciona, revisa los mensajes de error y busca ayuda. ¡Éxito!
- Developer: https://github.com/MrVenomSnake to Andy.