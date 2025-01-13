Simulador de Autómatas y Máquinas Teóricas
Este proyecto implementa la simulación de varios modelos teóricos de computación, incluyendo autómatas finitos deterministas (DFA), autómatas finitos no deterministas (NFA), autómatas con pila (PDA), y máquinas de Turing. Está diseñado para ser una herramienta educativa y práctica, que permite explorar la teoría de autómatas y lenguajes formales a través de pruebas y simulaciones interactivas.
 
Características principales
•	Simulación de DFA, NFA, PDA (por vaciado de pila y estado final), y Máquinas de Turing.
•	Conversión de NFA a DFA.
•	Soporte para definir estados, transiciones, cadenas de entrada, y condiciones de aceptación.
•	API REST implementada en Flask para integrar simulaciones con otras aplicaciones.
•	Ejemplos claros y casos de prueba predefinidos para cada modelo.
 
Requisitos
•	Python 3.8 o superior
•	Bibliotecas necesarias (instalables con requirements.txt):
bash
Copiar código
pip install -r requirements.txt
Incluye dependencias como Flask, Flask-Cors, y otras.
 
Instalación
1.	Clona este repositorio:
bash
Copiar código
git clone https://github.com/davidsanma2001/Emulador-JFLAP.git
2.	Navega al directorio del proyecto:
bash
Copiar código
cd simulador-automatas
3.	Crea y activa un entorno virtual:
bash
Copiar código
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
4.	Instala las dependencias:
bash
Copiar código
pip install -r requirements.txt
 
Uso
Ejecutar el servidor
1.	Inicia el servidor Flask:
bash
Copiar código
python app.py
2.	Accede al servidor en http://127.0.0.1:5000.
Endpoints disponibles
•	/simulate_dfa: Simula un autómata finito determinista (DFA).
•	/simulate_nfa: Simula un autómata finito no determinista (NFA).
•	/nfa_to_dfa: Convierte un NFA a DFA.
•	/simulate_turing: Simula una máquina de Turing.
•	/simulate_pda_empty_stack: Simula un autómata con pila (PDA) por vaciado de pila.
•	/simulate_pda_final_state: Simula un autómata con pila (PDA) por estado final.
Ejemplo de uso (curl)
Simulación de DFA
bash
Copiar código
curl -X POST \
  http://127.0.0.1:5000/simulate_dfa \
  -H 'Content-Type: application/json' \
  -d '{
    "states": ["q0", "q1", "q2"],
    "alphabet": ["a", "b"],
    "transitions": {
        "(q0,a)": {"new_state": "q1"},
        "(q0,b)": {"new_state": "q0"},
        "(q1,a)": {"new_state": "q2"},
        "(q1,b)": {"new_state": "q1"},
        "(q2,a)": {"new_state": "q2"},
        "(q2,b)": {"new_state": "q0"}
    },
    "start_state": "q0",
    "accept_states": ["q2"],
    "input_string": "aba"
}'
Resultado esperado:
json
Copiar código
{
  "final_state": "q2",
  "result": "Accepted"
}
 
Pruebas
Este proyecto incluye varios casos de prueba para validar el funcionamiento de cada modelo teórico. Puedes probar manualmente usando curl o integrarlos en una suite de pruebas automatizadas.
 
Estructura del Proyecto
•	app.py: Archivo principal que define los endpoints y ejecuta el servidor.
•	models/: Contiene las clases de los modelos teóricos (DFA, NFA, PDA, Turing).
•	templates/: Archivos HTML para posibles interfaces visuales.
•	requirements.txt: Dependencias del proyecto.
 
Contribución
Las contribuciones son bienvenidas. Para colaborar:
1.	Haz un fork del repositorio.
2.	Crea una rama para tu feature (git checkout -b feature/nueva-funcionalidad).
3.	Haz tus cambios y realiza un commit (git commit -m 'Añadir nueva funcionalidad').
4.	Envía un pull request.
 
Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más información.
 
Contacto
Si tienes preguntas, sugerencias o deseas reportar un problema, por favor contacta a:
•	Nombre: David San Martin
•	GitHub: https://github.com/davidsanma2001

![image](https://github.com/user-attachments/assets/01d98b8d-f1fa-42bc-ac1a-eb046a0333bc)
