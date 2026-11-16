# language: es

@ui
Característica: Login en SauceDemo
  Como usuario registrado
  Quiero iniciar sesión con mis credenciales
  Para acceder al inventario de productos

  Antecedentes:
    Dado que el navegador abre la página de login

  @smoke
  Escenario: Login exitoso con credenciales válidas
    Cuando ingreso usuario "standard_user" y clave "secret_sauce"
    Entonces la URL contiene "inventory.html"
    Y veo el título "Products"

  @regression
  Esquema del escenario: Login rechazado con credenciales inválidas
    Cuando ingreso usuario "<usuario>" y clave "<clave>"
    Entonces veo el mensaje de error "<error>"

    Ejemplos:
      | usuario        | clave         | error                                                                   |
      | usuario_falso  | clave_falsa   | Username and password do not match any user in this service            |
      | locked_out_user| secret_sauce  | Sorry, this user has been locked out                                    |
      |                |               | Username is required                                                    |