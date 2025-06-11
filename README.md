# 🎵 Gestión de Códigos Promocionales de Bandcamp  

Este proyecto es una aplicación interactiva desarrollada con **Streamlit**, diseñada para **gestionar códigos promocionales de Bandcamp**. Los usuarios pueden **registrarse en un formulario**, recibir un código promocional y canjearlo. La aplicación también incluye funcionalidades para **validar usuarios únicos** y **gestionar los códigos promocionales disponibles**.  

## 🛠️ Tecnologías Utilizadas  

- **Python** – Lenguaje principal utilizado para la lógica de la aplicación.  
- **Streamlit** – Framework para crear la **interfaz de usuario interactiva**.  
- **Supabase** – Base de datos utilizada para almacenar registros de usuarios y códigos promocionales.  
- **Pandas** – Biblioteca para manipulación de datos, utilizada en la gestión de códigos promocionales **almacenados en archivos CSV**.  
- **Streamlit Cookies Manager** – Para manejar **cookies** y generar **identificadores únicos** para los usuarios.  

## 🌟 Características Principales  

### 📋 Formulario de Registro  
- Los usuarios pueden ingresar su **nombre, apellido, correo electrónico, número de teléfono, país y comentario**.  
- Validación de **campos obligatorios** y **formato de correo electrónico**.  

### 🎟️ Gestión de Códigos Promocionales  
- Los códigos promocionales se almacenan en **un archivo CSV** o en **la base de datos de Supabase**.  
- Los códigos se **asignan de manera única** y se eliminan una vez asignados.  

### 🔒 Validación de Usuarios Únicos  
- Se utiliza un **identificador único (`unique_id`)** generado con **cookies** para asegurar que cada usuario **solo reciba un código**.  
- También se pueden validar usuarios mediante **dirección IP** y **User-Agent**.  

### 📧 Envío de Correos Electrónicos  
- Los códigos promocionales se envían al **correo electrónico** proporcionado por el usuario.  

### 🎨 Interfaz de Usuario  
- La aplicación tiene un diseño **limpio y moderno**, con un **fondo personalizado** y una lista de canciones (**tracklist**) estilizada.  

## 🔄 Cómo Funciona  

### 📝 Registro del Usuario  
1. El usuario completa el **formulario** y envía la información.  
2. La aplicación **valida los datos** ingresados.  

### 🎟️ Asignación de Código  
3. Si el usuario es **válido y único**, se le asigna un **código promocional**.  
4. El código se **elimina** del archivo CSV o de la base de datos para **evitar duplicados**.  

### ✉️ Envío del Código  
5. El código **se muestra en pantalla** y **se envía al correo electrónico** del usuario.  

### ⚙️ Gestión de Códigos  
6. Los códigos se gestionan mediante funciones que **leen, eliminan y actualizan el archivo CSV o la base de datos**.  

## 🚀 Cómo Empezar  

### 📂 Clonar el Repositorio  
~~~bash
git clone <URL_DEL_REPOSITORIO>
~~~~

### 📦 Instalar Dependencias
pip install -r requirements.txt


### ▶️ Ejecutar la Aplicación
streamlit run app.py


### 🏗️ Estructura del Proyecto
- `pages/registro.py`– Contiene el formulario de registro y la lógica para asignar códigos promocionales.

- `utils/search_code.py` – Funciones para gestionar los códigos promocionales almacenados en archivos CSV.
- `utils_bd/` – Módulo para interactuar con la base de datos Supabase.
- `styles.css` – Archivo CSS para personalizar el diseño de la aplicación.
- `secrets.toml` – Archivo para almacenar configuraciones sensibles como contraseñas y claves de API.

### 🤝 Contribuciones
El proyecto está abierto a contribuciones. Puedes abrir un issue o enviar un pull request si deseas colaborar.

### 📜 Licencia
Este proyecto está licenciado bajo la Licencia MIT, lo que permite su uso, modificación y distribución.
### 🎯 Objetivo
El objetivo principal del proyecto es proporcionar una solución sencilla y eficiente para gestionar códigos promocionales de Bandcamp, asegurando que cada usuario reciba un código único y evitando duplicados.
