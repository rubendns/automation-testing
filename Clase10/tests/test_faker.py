from faker import Faker


def test_generar_datos_con_faker():
    fake = Faker("es_AR")

    nombre = fake.name()
    correo = fake.email()
    direccion = fake.address()

    print(f"\nNombre generado: {nombre}")
    print(f"Correo generado: {correo}")
    print(f"Dirección generada: {direccion}")

    assert isinstance(nombre, str)
    assert len(nombre) > 0

    assert isinstance(correo, str)
    assert "@" in correo

    assert isinstance(direccion, str)
    assert len(direccion) > 0