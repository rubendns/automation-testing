# language: es

@unit @smoke
Característica: Multiplicación de enteros
  Como desarrollador
  Quiero comprobar operaciones matemáticas
  Para asegurar que los resultados sean correctos

  Esquema del escenario: Multiplicar <a> por <b>
    Cuando multiplico <a> y <b>
    Entonces obtengo <resultado>

    Ejemplos:
      | a  | b | resultado |
      | 2  | 3 | 6         |
      | 5  | 0 | 0         |
      | 7  | 4 | 28        |
      | -3 | 2 | -6        |