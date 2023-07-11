import datetime

entradas_platinum = [None] * 20
entradas_gold = [None] * 30
entradas_silver = [None] * 50
asistentes = []

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")

        if not validar_opcion(opcion):
            print("Opción inválida. Intente nuevamente.")
            continue

        opcion = int(opcion)

        if opcion == 1:
            comprar_entradas()
        elif opcion == 2:
            mostrar_ubicaciones_disponibles()
        elif opcion == 3:
            ver_listado_asistentes()
        elif opcion == 4:
            mostrar_ganancias_totales()
        elif opcion == 5:
            salir()
            break

def mostrar_menu():
    print("=== Menú ===")
    print("1. Comprar entradas")
    print("2. Mostrar ubicaciones disponibles")
    print("3. Ver listado de asistentes")
    print("4. Mostrar ganancias totales")
    print("5. Salir")

def comprar_entradas():
    cantidad = int(input("Ingrese la cantidad de entradas a comprar (1-3): "))
    if cantidad < 1 or cantidad > 3:
        print("Cantidad inválida. Intente nuevamente.")
        return
    
    print("Ubicaciones disponibles:")
    mostrar_ubicaciones_disponibles()

    for _ in range(cantidad):
        ubicacion_valida = False
        while not ubicacion_valida:
            ubicacion = int(input("Seleccione una ubicación (1-100): "))
            
            if ubicacion >= 1 and ubicacion <= 20:
                if entradas_platinum[ubicacion-1] is None:
                    ubicacion_valida = True
                    entradas_platinum[ubicacion-1] = obtener_run()
                else:
                    print("Ubicación no disponible.")
            elif ubicacion >= 21 and ubicacion <= 50:
                if entradas_gold[ubicacion-21] is None:
                    ubicacion_valida = True
                    entradas_gold[ubicacion-21] = obtener_run()
                else:
                    print("Ubicación no disponible.")
            elif ubicacion >= 51 and ubicacion <= 100:
                if entradas_silver[ubicacion-51] is None:
                    ubicacion_valida = True
                    entradas_silver[ubicacion-51] = obtener_run()
                else:
                    print("Ubicación no disponible.")
            else:
                print("Ubicación inválida.")
    
    print("Operación realizada correctamente.")

def obtener_run():
    run = input("Ingrese el RUN del asistente (sin guiones ni puntos): ")
    return run

def mostrar_ubicaciones_disponibles():
    print("Ubicaciones disponibles:")
    print("Escenario:")
    print("|" + "-" * 10 + "|")

    print("Platinum:")
    mostrar_asientos(entradas_platinum, 10)
    print("\nGold:")
    mostrar_asientos(entradas_gold, 10)
    print("\nSilver:")
    mostrar_asientos(entradas_silver, 10)
    print()

def mostrar_asientos(asientos, columnas):
    for i in range(0, len(asientos), columnas):
        for j in range(i, min(i+columnas, len(asientos))):
            if asientos[j] is None:
                print("O", end=" ")
            else:
                print("X", end=" ")
        print()

def ver_listado_asistentes():
    if len(asistentes) == 0:
        print("No hay asistentes registrados.")
        return

    asistentes_ordenados = sorted(asistentes)
    print("Listado de asistentes:")
    for asistente in asistentes_ordenados:
        print(asistente)

def mostrar_ganancias_totales():
    total_platinum = len([asistente for asistente in entradas_platinum if asistente is not None]) * 120000
    total_gold = len([asistente for asistente in entradas_gold if asistente is not None]) * 80000
    total_silver = len([asistente for asistente in entradas_silver if asistente is not None]) * 50000
    total_general = total_platinum + total_gold + total_silver

    print("Tipo Entrada\tCantidad\tTotal")
    print("Platinum\t2\t\t$%d" % total_platinum)
    print("Gold\t\t4\t\t$%d" % total_gold)
    print("Silver\t\t10\t\t$%d" % total_silver)
    print("TOTAL\t\t16\t\t$%d" % total_general)

def salir():
    print("Gracias por usar el sistema, Hasta luego.")

def validar_opcion(opcion):
    if opcion.isdigit() and int(opcion) >= 1 and int(opcion) <= 5:
        return True
    return False

if __name__ == '__main__':
    main()
