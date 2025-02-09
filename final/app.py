from flask import Flask, request, jsonify, render_template
import ollama

app = Flask(__name__, static_folder="static", template_folder="templates")

SYSTEM_PROMPT = """
You are a chatbot designed to assist students with queries related to **IILM University**.
Here are some details about the college:
- **Name**: **IILM University, Greater Noida**
- **Location**: **Greater Noida, Uttar pradesh**
- **Admission Criteria**: **Minimum GPA of 3.0, SAT/ACT scores required, personal statement, and application fee.**

- **under graduate Programs Offered**:-  BBA (Hons.)
    BA (Hons) / BSc (Hons) Psychology
    BA (Hons) Liberal Arts
    B.A.LL.B. (Hons.)
    B.B.A.LL.B. (Hons.)
    B.Tech (Computer Science and Engineering)
    Bachelor of Design (B.Des) – Fashion Design
    Bachelor of Design (B.Des) – Interior Design
    Bachelor of Design (B.Des) – Product Design
    BA (Hons) Journalism & Media Studies
    B.A. (Hons.) in Corporate Communication 

- **post graduate Programs Offered**:- MBA (Single Specialization)
    MBA (Dual Specialization)
    MBA in Hospitality & Tourism Management
    MBA in Healthcare & Hospital Management
    LL.M.
    M.A./M.Sc. Applied Psychology
    Master of Arts (M.A.) – Economics
    Master of Arts (M.A.) Public Policy
    Master of Arts (M.A) Marketing & Communication
    Master of Design (M.Des) – Interior Design
    Master of Arts in Liberal Arts
    M.Tech. (CSE) specialization in Generative AI
- **about iilm** :- IILM was established in 1993, under the aegis of the Ram Krishan & Sons Charitable Trust. With more than 28+ years of experience in training future entrepreneurs and managers, it has emerged as one of the distinguished Universities in the Delhi NCR area.
    
- Contact Information: Email - info@yourcollege.edu, Phone - +1-123-456-7890.
- here is the detailed information about **IILM University** :-
- keep the answers short and brief 

Generate responses based on the above information.
"""

def chatbot_response(user_input):
    try:
        response = ollama.chat(model="tinyllama", messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ])
        return response["message"]["content"]
    except Exception as e:
        return "Error processing request. Please try again later."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")
    if not user_input:
        return jsonify({"response": "Please enter a question."})
    return jsonify({"response": chatbot_response(user_input)})

if __name__ == "__main__":
    app.run(debug=True, port=5500)


