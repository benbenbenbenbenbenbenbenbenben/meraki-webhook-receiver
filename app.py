from flask import Flask, request
import main
import os
 
app = Flask(__name__)

@app.route("/", methods=['POST'])
def index():
   if request.method == 'POST':
      return main.handler(request)

# Debug:
if __name__ == "__main__":
    app.run(debug=True, port=5000)

# Prod:
# if __name__ == '__main__':
#     port = int(os.environ.get('PORT', 5000))
#     app.run(host='0.0.0.0', port=port)
