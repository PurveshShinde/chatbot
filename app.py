from flask import Flask, render_template, request, jsonify
from models.ai_model import get_mental_health_analysis  # Ensure this import is correct

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    user_input = request.form['user_input']
    analysis_result = get_mental_health_analysis(user_input)
    return jsonify(analysis_result)  # Return the analysis result in JSON format

if __name__ == '__main__':
    app.run(debug=True)
