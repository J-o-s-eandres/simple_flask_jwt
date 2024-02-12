```markdown
# Flask API with JWT Authentication

Este proyecto implementa una API Flask que utiliza autenticación JWT para proteger rutas y realizar solicitudes a la API de GitHub para obtener información de usuarios.

## Instalación

Antes de ejecutar la aplicación, asegúrate de tener instaladas las siguientes dependencias:

- Flask
- PyJWT
- Requests

Puedes instalarlas usando pip:

```bash
pip install Flask PyJWT requests
```

## Uso

La aplicación consta de las siguientes funcionalidades:

### Autenticación

- **/login (POST)**: Esta ruta permite a los usuarios iniciar sesión. Si el nombre de usuario es "Joseandres Montesino", se genera un token JWT válido y se devuelve como respuesta. De lo contrario, se devuelve un mensaje de error.

- **/verify/token (GET)**: Esta ruta permite verificar un token JWT proporcionado en el encabezado de autorización. Si el token es válido, devuelve los datos decodificados del token. Si no es válido, devuelve un mensaje de error.

### Usuarios de GitHub

- **/github/users (POST)**: Esta ruta permite realizar una búsqueda de usuarios en GitHub por ubicación. Se espera que se proporcione un objeto JSON con el país de búsqueda. Devuelve una lista de usuarios encontrados en GitHub para esa ubicación.

## Configuración

Antes de ejecutar la aplicación, asegúrate de configurar la variable de entorno `SECRET` con tu clave secreta JWT.

```bash
export SECRET='tu_clave_secreta'
```

## Ejemplo de Uso

```python
import requests

# Iniciar sesión para obtener un token
response = requests.post("http://localhost:5000/login", json={"username": "Joseandres Montesino"})
if response.status_code == 200:
    token = response.json()
    print("Token JWT:", token)

    # Verificar el token JWT
    verify_response = requests.get("http://localhost:5000/verify/token", headers={"Authorization": f"Bearer {token}"})
    if verify_response.status_code == 200:
        decoded_data = verify_response.json()
        print("Datos decodificados del token:", decoded_data)

    # Buscar usuarios en GitHub
    github_response = requests.post("http://localhost:5000/github/users", json={"country": "Spain"})
    print("Usuarios de GitHub en España:", github_response.json())
else:
    print("Error:", response.json()["message"])
```

## Licencia

Este proyecto está bajo la [Licencia MIT](LICENSE). Consulta el archivo [LICENSE](LICENSE) para más detalles.
```