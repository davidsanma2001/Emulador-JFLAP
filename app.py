from flask import Flask, render_template, jsonify, request
from models.NFA import NFA
from models.DFA import DFA
from models.Turing_machine import Turing_machine
from models.NFA_to_DFA import NFA_DFA
from models.PDA_empty_stack import PDA as PDAEmptyStack
from models.PDA_final_state import PDA as PDAFinalState

app = Flask(__name__)

# Ruta para la página de inicio
@app.route('/')
def home():
    return render_template('index.html')


# Ruta para simular el autómata
@app.route('/simulate_dfa', methods=['GET', 'POST'])
def simulate_automaton():
    if request.method == 'POST':
        try:
            data = request.get_json()
            if not all(key in data for key in ('states', 'alphabet', 'transitions', 'start_state', 'accept_states', 'input_string')):
                return jsonify({"error": "Missing data"}), 400

            states = data.get('states', [])
            alphabet = data.get('alphabet', [])
            transitions = data.get('transitions', {})
            start_state = data.get('start_state', '')
            accept_states = data.get('accept_states', [])
            input_string = data.get('input_string', '')

            dfa = DFA(states, alphabet, transitions, start_state, accept_states)
            
            final_state, accepted = dfa.simulate(input_string)
            
            return jsonify({"final_state": final_state, "result": "Accepted" if accepted == 'accepted' else "Rejected"}), 200
        
        except Exception as e:
            print(f"Error: {str(e)}")
            return jsonify({"error": "An error occurred during simulation."}), 500 

    return render_template('simulate_dfa.html')


# Ruta para simular el autómata NFA
@app.route('/simulate_nfa', methods=['GET', 'POST'])
def simulate_nfa():
    if request.method == 'POST':
        try:
            data = request.get_json()
            if not all(key in data for key in ('states', 'alphabet', 'transitions', 'start_state', 'accept_states', 'input_string')):
                return jsonify({"error": "Missing data"}), 400

            states = data.get('states', [])
            alphabet = data.get('alphabet', [])
            transitions = data.get('transitions', {})
            start_state = data.get('start_state', '')
            accept_states = data.get('accept_states', [])
            input_string = data.get('input_string', '')

            nfa = NFA(states, alphabet, transitions, start_state, accept_states)
            
            current_states, accepted = nfa.simulate(input_string)
            
            return jsonify({"final_states": list(current_states), "result": "Accepted" if accepted == 'accepted' else "Rejected"}), 200
        
        except Exception as e:
            print(f"Error: {str(e)}")
            return jsonify({"error": "An error occurred during simulation."}), 500 

    return render_template('simulate_nfa.html')


@app.route('/simulate_turing', methods=['GET', 'POST'])
def simulate_turing():
    if request.method == 'POST':
        try:
            data = request.get_json()
            if not all(key in data for key in ('states', 'alphabet', 'transitions', 'start_state', 'accept_states', 'input_string')):
               return jsonify({"error": "Missing data"}), 400

            states = data.get('states', [])
            alphabet = data.get('alphabet', [])
            transitions = data.get('transitions', {})
            start_state = data.get('start_state', '')
            accept_states = data.get('accept_states', [])
            input_string = data.get('input_string', '')

            turing_machine = Turing_machine(states, input_string, alphabet, 0, transitions, start_state, accept_states)
            
            final_state, head_position, output_string, accepted = turing_machine.simulate()
            
            return jsonify({"final_state": final_state, "head_position": head_position, "output_string": output_string, "result": "Accepted" if accepted == 'accepted' else "Rejected"}), 200
        except Exception as e:
            print(f"Error: {str(e)}")
            return jsonify({"error": "An error occurred during simulation."}), 500

    return render_template('simulate_turing.html')


@app.route('/nfa_to_dfa', methods=['GET','POST'])
def nfa_to_dfa_route():
    if request.method == 'POST':
        try:
            data = request.get_json()
            print("Datos recibidos:", data)
            # Verificamos que el JSON tiene los campos necesarios
            if not all(key in data for key in ('states', 'alphabet', 'transitions', 'start_state', 'accept_states')):
                return jsonify({"error": "Faltan datos en el JSON"}), 400

            nfa = NFA_DFA(
                states=data['states'],
                alphabet=data['alphabet'],
                transitions=data['transitions'],
                start_state=data['start_state'],
                accept_states=data['accept_states']
            )

            # Convertir el NFA a DFA usando tu función `to_dfa`
            dfa_result = nfa.to_dfa()

            return jsonify({
                'states': dfa_result['states'],  # Estados del DFA
                'alphabet': dfa_result['alphabet'],  # Alfabeto
                'start_state': dfa_result['start_state'],  # Estado inicial
                'accept_states': dfa_result['accept_states'],  # Estados de aceptación
                'transitions': dfa_result['transitions'],  # Transiciones
            }), 200
        except Exception as e:
            print(f"Error: {str(e)}")
            return jsonify({"error": "Ocurrió un error durante la conversión."}), 500

    return render_template('nfa_to_dfa.html')

@app.route('/simulate_pda_empty_stack', methods=['GET', 'POST'])
def simulate_pda_empty_stack():
    if request.method == 'POST':
        try:
            data = request.get_json()
            if not all(key in data for key in ('states', 'alphabet', 'transitions', 'start_state', 'input_string', 'stack_alphabet')):
                return jsonify({"error": "Missing data"}), 400

            # Extract data for PDA
            states = data.get('states', [])
            alphabet = data.get('alphabet', [])
            transitions = data.get('transitions', {})
            start_state = data.get('start_state', '')
            input_string = data.get('input_string', '')
            stack_alphabet = data.get('stack_alphabet', [])

            # Create PDA for empty stack acceptance
            pda = PDAEmptyStack(states, alphabet, transitions, start_state, [], stack_alphabet)
            result = pda.simulate(input_string)

            # Extract values from the result
            final_state = result['final_state']
            final_stack = result['final_stack']
            result_status = result['result']
            remaining_input = result['remaining_input']

            return jsonify({
                "final_state": final_state,
                "result": result_status,
                "final_stack": final_stack,
                "remaining_input": remaining_input
            }), 200

        except Exception as e:
            print(f"Error: {str(e)}")
            return jsonify({"error": "An error occurred during simulation."}), 500 

    return render_template('simulate_pda_empty_stack.html')

@app.route('/simulate_pda_final_state', methods=['GET', 'POST'])
def simulate_pda_final_state():
    if request.method == 'POST':
        try:
            data = request.get_json()
            if not all(key in data for key in ('states', 'alphabet', 'transitions', 'start_state', 'accept_states', 'input_string', 'stack_alphabet')):
                return jsonify({"error": "Missing data"}), 400

            # Extract data for PDA
            states = data.get('states', [])
            alphabet = data.get('alphabet', [])
            transitions = data.get('transitions', {})
            start_state = data.get('start_state', '')
            accept_states = data.get('accept_states', [])
            input_string = data.get('input_string', '')
            stack_alphabet = data.get('stack_alphabet', [])

            # Create PDA for final state acceptance
            pda = PDAFinalState(states, alphabet, transitions, start_state, accept_states, stack_alphabet)
            result = pda.simulate(input_string)

            # Extract values from the result
            final_state = result['final_state']
            final_stack = result['final_stack']
            result_status = result['result']
            remaining_input = result['remaining_input']

            return jsonify({
                "final_state": final_state,
                "result": result_status,
                "final_stack": final_stack,
                "remaining_input": remaining_input
            }), 200

        except Exception as e:
            print(f"Error: {str(e)}")
            return jsonify({"error": "An error occurred during simulation."}), 500 

    return render_template('simulate_pda_final_state.html')

# Rutas para otras funcionalidades
@app.route('/load')
def load_automaton():
    return "Función para cargar autómata (próximamente)"


@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

