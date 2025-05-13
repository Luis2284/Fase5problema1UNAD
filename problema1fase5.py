# Nombre del estudiante: Luis Navarro Masson
# Grupo: 81
# Número y Texto del programa: - Problema 1 Evaluación Final POA
# Código Fuente: autoría propia

class Curso:
    def __init__(self, nombre, costo_mes, duracion, descuento):
        self.nombre = nombre
        self.costo_mes = costo_mes
        self.duracion = duracion
        self.descuento = descuento

class Estudiante:
    def __init__(self, nombre, curso, modalidad_pago):
        self.nombre = nombre
        self.curso = curso
        self.modalidad_pago = modalidad_pago

class SistemaInscripcion:
    def __init__(self):
        self.cursos = {
            "Programación": Curso("Programación", 300000, 6, 0.20),
            "Diseño Gráfico": Curso("Diseño Gráfico", 250000, 4, 0.15),
            "Redes": Curso("Redes", 200000, 5, 0.10)
        }
        self.estudiantes = []

    def inscribir_estudiante(self, nombre_estudiante, curso_nombre, modalidad_pago):
        if curso_nombre in self.cursos:
            estudiante = Estudiante(nombre_estudiante, self.cursos[curso_nombre], modalidad_pago)
            self.estudiantes.append(estudiante)
            return True
        return False

    def obtener_estadisticas(self):
        estudiantes_por_curso = {curso: 0 for curso in self.cursos}
        modalidad_stats = {"Completo": 0, "Mensual": 0}

        for estudiante in self.estudiantes:
            estudiantes_por_curso[estudiante.curso.nombre] += 1
            modalidad_stats[estudiante.modalidad_pago] += 1

        duracion_total = sum(estudiante.curso.duracion for estudiante in self.estudiantes)

        costo_total_sin_descuento = sum(
            estudiante.curso.costo_mes * estudiante.curso.duracion 
            for estudiante in self.estudiantes
        )

        descuento_total = sum(
            estudiante.curso.costo_mes * estudiante.curso.duracion * estudiante.curso.descuento
            for estudiante in self.estudiantes
            if estudiante.modalidad_pago == "Completo"
        )

        valor_neto = costo_total_sin_descuento - descuento_total

        return {
            "estudiantes_por_curso": estudiantes_por_curso,
            "modalidad_pago": modalidad_stats,
            "duracion_total": duracion_total,
            "costo_total_sin_descuento": costo_total_sin_descuento,
            "descuento_total": descuento_total,
            "valor_neto": valor_neto
        }

def main():
    sistema = SistemaInscripcion()
    
    print("=== Sistema de Inscripción de Cursos ===")
    print("\nCursos disponibles:")
    for nombre, curso in sistema.cursos.items():
        print(f"- {nombre}: ${curso.costo_mes:,} por mes, {curso.duracion} meses, {curso.descuento*100}% descuento en pago completo")
    
    while True:
        try:
            num_estudiantes = int(input("\nIngrese el número de estudiantes a inscribir: "))
            if num_estudiantes > 0:
                break
            print("Por favor ingrese un número positivo.")
        except ValueError:
            print("Por favor ingrese un número válido.")

    for i in range(num_estudiantes):
        print(f"\nInscripción del estudiante {i+1}")
        nombre_estudiante = input("Nombre del estudiante: ")
        
        while True:
            print("\nCursos disponibles:")
            for nombre_curso in sistema.cursos:
                print(f"- {nombre_curso}")
            curso = input("Seleccione el curso: ").title()
            if curso in sistema.cursos:
                break
            print("Curso no válido. Por favor seleccione uno de la lista.")

        while True:
            modalidad = input("Modalidad de pago (Completo/Mensual): ").capitalize()
            if modalidad in ["Completo", "Mensual"]:
                break
            print("Modalidad no válida. Por favor ingrese 'Completo' o 'Mensual'.")

        if sistema.inscribir_estudiante(nombre_estudiante, curso, modalidad):
            curso_obj = sistema.cursos[curso]
            costo_total = curso_obj.costo_mes * curso_obj.duracion
            if modalidad == "Completo":
                costo_total -= costo_total * curso_obj.descuento
            print(f"{nombre_estudiante} inscrito exitosamente. Total a pagar: ${int(costo_total):,}")
        else:
            print("Error al inscribir al estudiante.")

    # Mostrar resultados
    estadisticas = sistema.obtener_estadisticas()
    print("\n=== Resultados ===")
    print("\n1. Cantidad de estudiantes por curso:")
    for curso, cantidad in estadisticas["estudiantes_por_curso"].items():
        print(f"- {curso}: {cantidad} estudiantes")

    print("\n2. Modalidades de pago:")
    for modalidad, cantidad in estadisticas["modalidad_pago"].items():
        print(f"- {modalidad}: {cantidad} estudiantes")

    print(f"\n3. Duración total en meses: {estadisticas['duracion_total']} meses")
    print(f"\n4. Costo total sin descuentos: ${estadisticas['costo_total_sin_descuento']:,}")
    print(f"\n5. Monto total de descuentos: ${estadisticas['descuento_total']:,}")
    print(f"\n6. Valor neto después de descuentos: ${estadisticas['valor_neto']:,}")

if __name__ == "__main__":
    main()
