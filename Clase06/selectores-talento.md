
# Clase 6 - Selectores CSS y XPath

## Página utilizada

https://www.saucedemo.com/

## Selectores encontrados

| Elemento | Selector elegido | Tipo | Razón |
|---|---|---|---|
| Usuario | `#user-name` | CSS | Tiene un id único y estable. |
| Usuario | `//*[@id='user-name']` | XPath | Localiza el campo por su id. |
| Contraseña | `#password` | CSS | Tiene un id único y estable. |
| Contraseña | `//*[@id='password']` | XPath | Localiza el campo por su id. |
| Botón Login | `#login-button` | CSS | Tiene un id único y estable. |
| Botón Login | `//*[@id='login-button']` | XPath | Localiza el botón por su id. |

## Verificación

Los selectores fueron probados en DevTools utilizando:

- `document.querySelector()` para CSS.
- `$x()` para XPath.

Se comprobó que cada selector encuentra el elemento esperado,
cambiando su contorno primero a verde y después a rojo.

## Prueba masiva de selectores CSS

```javascript
['#user-name', '#password', '#login-button'].forEach(sel => {
    const el = document.querySelector(sel);
    if (el) el.style.backgroundColor = 'khaki';
});
```

### Resultado

Los tres elementos (Username, Password y Login)
cambiaron su fondo a amarillo claro.

Esto confirma que los tres selectores CSS funcionan.