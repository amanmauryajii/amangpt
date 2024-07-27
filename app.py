from flask import Flask, render_template, request, Response
import time
from groq import Groq

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form['question']
    return Response(generate_answer(question), mimetype='text/plain')

def generate_answer(question):
    client = Groq(api_key="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",)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
        model="llama3-8b-8192",
    )
    
    question = chat_completion.choices[0].message.content

    words = f"{question}".split()
    for word in words:
        time.sleep(0)  # Simulate processing time
        yield word + ' '

if __name__ == '__main__':
    app.run(debug=True)
