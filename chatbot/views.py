from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json, nltk
from nltk.chat.util import Chat, reflections

# Create your views here.

def hello(request):
    return HttpResponse("<h2>Hello </h2>")

def about(request):
    return HttpResponse("about")

def chat(request):
    return render(request, 'chat.html')

pares = [
        [
            r"me llamo (.*)",
            ["Hola %1, mi nombre es EVA (Esgode Virtual Assistant) ¿cómo puedo ayudarte?",]
        ],
        [
            r"mi nombre es (.*)",
            ["Hola %1, mi nombre es EVA (Esgode Virtual Assistant) ¿cómo puedo ayudarte?",]
        ],
        [
            r"hola|Hola|Buenos dias|Buenas tardes|Buenas noches|ola|",
            ["Hola, bienvenido a E S G O D E, somos una empresa de tecnología y dispositivos móviles ¿Cómo te llamas?",]
        ],
        [
            r"¿Cómo estás?|como estás?",
            ["Estoy bien, gracias por preguntar", "¡Genial! ¿Y tú?",]
        ],
        [
            r"(.*) iPhone (.*)",
            ["Tenemos los mejores modelos de iPhone en nuestra tienda en línea. ¿En qué modelo estás interesado?",]
        ],
        [
            r"(.*) Samsung (.*)",
            ["Claro, tenemos varios modelos de Samsung disponibles. ¿Cuál te interesa?",]
        ],
        [
            r"(.*) Xiaomi (.*)",
            ["¡Sí! Los Xiaomi son una excelente opción. ¿Cuál modelo en específico te llama la atención?",]
        ],
        [
            r"(.*) accesorio(.*)",
            ["Tenemos una amplia selección de accesorios para celulares, ¿buscas algo en específico?",]
        ],
        [
            r"(.*) domótica(.*)",
            ["Sí, también ofrecemos artículos para la domótica del hogar. ¿En qué puedo ayudarte?",]
        ],
        [
            r"Adiós|Hasta luego|Chao|Bye",
            ["¡Hasta luego! Espero haberte sido de ayuda.", "¡Nos vemos pronto!",]
        ],
    ]

# Inicialización del chatbot
chatbot = Chat(pares, reflections)

# Función para obtener la respuesta de EVA
def obtener_respuesta(message):
    return chatbot.respond(message)

# Vista para la página del chatbot
def chat(request):
    return render(request, 'chat.html')

# Vista para procesar las solicitudes del chatbot
@csrf_exempt
def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = obtener_respuesta(message)
        data = {'response': response}
        return JsonResponse(data)
