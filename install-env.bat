rem Creamos entorno
python -m venv flask-env
rem Activamos el entorno
call ./flask-env/Scripts/activate
rem instalamos paquetes que se precisan 
rem https://rukbottoland.com/blog/como-instalar-paquetes-python-con-requirementstxt/
pip install -r requirements.txt

echo Para ejecutar la aplicación ejecutar el fichero app.py desde visual studio code

pause