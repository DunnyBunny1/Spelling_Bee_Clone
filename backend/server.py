from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, origins='*')

@app.route('/api/users',methods=['GET'] )
def users():
    return jsonify(
        {
            'users' : ['Olivia', 'Karen', 'Bob','Julian']
        }
    )

if __name__ == '__main__':
    # Run the app in development mode on port 5000
    app.run(debug=True)

