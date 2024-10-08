from flask import Flask, render_template, request, jsonify
import pyautogui
import time
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Manually recorded coordinates for each agent
agent_coordinates = {
    'brimstone': (500, 320),
    'viper': (635, 320),
    'omen': (770, 320),
    'killjoy': (289, 553),
    'cypher': (500, 440),
    'sova': (635, 440),
    'sage': (770, 440),
    'phoenix': (905, 440),
    'jett': (89, 553),
    'reyna': (635, 560),
    'raze': (770, 560),
    'breach': (905, 560),
    'skye': (500, 680),
    'yoru': (635, 680),
    'astra': (770, 680),
    'kayo': (189, 553),
    'chamber': (500, 800),
    'fade': (635, 800),
    'neon': (389, 553),
    'harbor': (905, 800)
}

@app.route('/')
def index():
    # Return agent names as JSON
    return jsonify({'agents': list(agent_coordinates.keys())})

@app.route('/select_agent', methods=['POST'])
def select_agent():
    agent_name = request.json['agent']  # Use request.json for JSON data
    spam_click(agent_name)
    return jsonify({'message': f'Clicking complete for {agent_name}!'})

def spam_click(agent_name):
    x, y = agent_coordinates[agent_name]
    start_time = time.time()
    pyautogui.hotkey('alt', 'tab')
    while time.time() - start_time < 10:  # click_duration is set to 10 seconds
        pyautogui.click(x, y)
        time.sleep(0.1)  # click_interval is set to 0.1 seconds
        pyautogui.click(950, 754)

if __name__ == '__main__':
    app.run(debug=True)
