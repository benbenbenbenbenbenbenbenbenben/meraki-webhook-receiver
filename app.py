from flask import Flask, request
from main import *
 
app = Flask(__name__)

@app.route("/", methods=['POST'])
def index():
   if request.method == 'POST':
      return handler(request)


# Debug:
if __name__ == "__main__":
    app.run(debug=True, port=5000)

# Manual Port:
# if __name__ == '__main__':
#     port = int(os.environ.get('PORT', 5000))
#     app.run(host='0.0.0.0', port=port)
