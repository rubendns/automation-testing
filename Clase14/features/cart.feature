# language: es

@ui @regression
Característica: Carrito de compras en SauceDemo
  Como usuario registrado
  Quiero agregar productos al carrito
  Para preparar mi compra

  Antecedentes:
    Dado que inicié sesión en SauceDemo como usuario estándar

  Escenario: Agregar una mochila al carrito
    Cuando agrego el producto "Sauce Labs Backpack" al carrito
    Entonces el carrito muestra 1 producto