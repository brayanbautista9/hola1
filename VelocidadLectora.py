import random
import time

cuentos = [
    {'titulo': "Caperucita Roja",
     'texto': """Había una vez una niña llamada Caperucita Roja, que vivía en un bosque con su madre. Un día, su madre le dijo: 
Lleva esta cesta con pan y miel a tu abuela. Está enferma y esto la animará. No hables con extraños y ve directo por el camino.
Caperucita Roja asintió y partió. En el bosque, un lobo la vio y le preguntó:
—¿Adónde vas, niña bonita?
—A casa de mi abuela, al otro lado del bosque —respondió ella, olvidando la advertencia.
El lobo, astuto, corrió a la casa de la abuela, llamó a la puerta y fingió ser Caperucita. La abuela abrió y él la encerró en el armario. Luego, se puso su gorro y se metió en la cama.
Cuando Caperucita llegó, notó algo raro:
—Abuela, ¡qué ojos más grandes tienes!
—Son para verte mejor —dijo el lobo.
—¡Y qué orejas más grandes!
—Son para oírte mejor.
—¡Y qué dientes más grandes!
—¡Son para comerte mejor! —rugió el lobo, saltando de la cama.
En ese momento, un leñador que escuchó los gritos entró con su hacha y asustó al lobo, que huyó para nunca volver. La abuela salió del armario y abrazó a Caperucita, quien prometió nunca más desobedecer.""",
     'palabras': 250,
     'preguntas': [
         {'pregunta': '¿Qué alimentos llevaba Caperucita en su cesta?',
          'opciones': ['Manzanas y peras', 'Pan y miel', 'Queso y vino', 'Galletas y chocolate'],
          'respuesta': 1},
         {'pregunta': '¿Qué advertencia le dio su madre?',
          'opciones': ['Que no se mojara', 'Que no hablara con extraños', 'Que corriera rápido', 'Que cantara fuerte'],
          'respuesta': 1},
         {'pregunta': '¿Dónde escondió el lobo a la abuela?',
          'opciones': ['En el sótano', 'En el armario', 'En el ático', 'En el jardín'],
          'respuesta': 1},
         {'pregunta': '¿Quién rescató a Caperucita?',
          'opciones': ['Un policía', 'Un leñador', 'Un cazador', 'Su padre'],
          'respuesta': 1},
         {'pregunta': '¿Qué prometió Caperucita al final?',
          'opciones': ['Comer más verduras', 'Nunca más desobedecer', 'Visitar más a su abuela', 'Aprender a cocinar'],
          'respuesta': 1}
     ]},
    {'titulo': "La Gallina de los Huevos de Oro",
     'texto': """Había una vez un granjero pobre que vivía con su esposa en una pequeña cabaña. Un día, su gallina, la más gordita del corral, puso un huevo brillante. Al recogerlo, el granjero casi se cae de espaldas: ¡era de oro puro!
—¡Mira, mujer! —gritó emocionado—. ¡Nuestra gallina es mágica!
Al día siguiente, la gallina puso otro huevo de oro, y así durante una semana. El granjero y su esposa vendieron los huevos y se llenaron de lujos: compraron vestidos, comida fina y hasta una carreta nueva.
Pero el granjero, ávido de riqueza, empezó a impacientarse:
—¿Por qué esperar a que ponga un huevo cada día? ¡Si la abrimos, sacaremos todo el oro de una vez!
Su esposa trató de detenerlo:
—¡No seas tonto! Si la matas, no tendremos más oro.
Pero el granjero no escuchó. Tomó un cuchillo, mató a la gallina y la abrió... solo para descubrir que por dentro era igual que todas las demás. No había oro, ni joyas, ni nada.
Al día siguiente, sin gallina y sin huevos, el granjero y su esposa volvieron a ser pobres. El hombre lloró de arrepentimiento, pero ya era tarde.
Moraleja: La avaricia rompe el saco. Quien todo lo quiere, todo lo pierde.""",
     'palabras': 250,
     'preguntas': [
         {'pregunta': '¿Qué ponía la gallina que sorprendió al granjero?',
          'opciones': ['Huevos de chocolate', 'Huevos de oro', 'Huevos gigantes', 'Huevos de colores'],
          'respuesta': 1},
         {'pregunta': '¿Qué compraron con el dinero de los huevos?',
          'opciones': ['Una casa nueva', 'Vestidos y comida fina', 'Un coche', 'Un televisor'],
          'respuesta': 1},
         {'pregunta': '¿Por qué decidió el granjero matar a la gallina?',
          'opciones': ['Porque estaba enferma', 'Para conseguir todo el oro de una vez', 'Porque ya no ponía huevos', 'Porque su esposa se lo pidió'],
          'respuesta': 1},
         {'pregunta': '¿Qué encontró dentro de la gallina?',
          'opciones': ['Muchas monedas de oro', 'Nada especial', 'Un mapa del tesoro', 'Un diamante'],
          'respuesta': 1},
         {'pregunta': '¿Cuál es la moraleja de la historia?',
          'opciones': ['No hay que confiar en los animales', 'La avaricia rompe el saco', 'El oro no da la felicidad', 'Hay que compartir lo que se tiene'],
          'respuesta': 1}
     ]}
]

def calcular_velocidad(palabras, segundos):
    minutos = segundos / 60
    return palabras / minutos

def evaluar_comprension(respuestas_correctas, total_preguntas):
    porcentaje = (respuestas_correctas / total_preguntas) * 100
    if porcentaje >= 80:
        return "Excelente comprensión lectora"
    elif porcentaje >= 60:
        return "Buena comprensión lectora"
    elif porcentaje >= 40:
        return "Comprensión lectora regular"
    else:
        return "Comprensión lectora baja"

# Seleccionar un cuento al azar
cuento = random.choice(cuentos)

# Mostrar el cuento
print(f"\n=== {cuento['titulo']} ===\n")
print(cuento['texto'])
print(f"\n(Palabras: {cuento['palabras']})")

# Pedir tiempo de lectura
input("\nPresiona Enter cuando empieces a leer...")
inicio = time.time()

input("\nPresiona Enter cuando termines de leer...")
fin = time.time()

# Calcular y mostrar resultados
tiempo_segundos = fin - inicio
velocidad = calcular_velocidad(cuento['palabras'], tiempo_segundos)

print(f"\nTiempo de lectura: {tiempo_segundos:.1f} segundos")
print(f"Velocidad lectora: {velocidad:.0f} palabras por minuto")

# Interpretación
if velocidad < 150:
    print("Nivel: Lector básico")
elif 150 <= velocidad < 250:
    print("Nivel: Lector intermedio")
else:
    print("Nivel: Lector avanzado")

# Cuestionario de comprensión
print("\n=== Cuestionario de Comprensión ===")
respuestas_correctas = 0

for i, pregunta in enumerate(cuento['preguntas']):
    print(f"\n{i+1}. {pregunta['pregunta']}")
    for j, opcion in enumerate(pregunta['opciones']):
        print(f"   {j+1}. {opcion}")
    
    while True:
        try:
            respuesta = int(input("Tu respuesta (1-4): ")) - 1
            if 0 <= respuesta <= 3:
                break
            else:
                print("Por favor, ingresa un número entre 1 y 4")
        except ValueError:
            print("Por favor, ingresa un número válido")
    
    if respuesta == pregunta['respuesta']:
        print("¡Correcto!")
        respuestas_correctas += 1
    else:
        print(f"Incorrecto. La respuesta correcta es: {pregunta['opciones'][pregunta['respuesta']]}")

# Resultados del cuestionario
porcentaje = (respuestas_correctas / len(cuento['preguntas'])) * 100
print(f"\nResultados del cuestionario:")
print(f"Respuestas correctas: {respuestas_correctas} de {len(cuento['preguntas'])}")
print(f"Porcentaje de aciertos: {porcentaje:.0f}%")
print(f"Nivel de comprensión: {evaluar_comprension(respuestas_correctas, len(cuento['preguntas']))}")