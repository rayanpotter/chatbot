from flask import Flask, render_template, request, jsonify
from scripts.refomul import correct_spelling  

app = Flask(__name__, static_folder="static", static_url_path="/static")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process_query", methods=["POST"])
def process_query():
  
    data = request.get_json()
    user_query = data.get("query", "")


    corrected_query = correct_spelling(user_query)  

    
    response = f"Processed query: {corrected_query}"

    
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
