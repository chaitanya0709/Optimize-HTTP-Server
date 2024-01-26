from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data')
def get_data():
    file_name = request.args.get('n')
    line_number = request.args.get('m')

    if file_name is None:
        return "Error: Missing 'n' parameter", 400

    file_path = f"/tmp/data/{file_name}.txt"

    try:
        with open(file_path, 'r') as file:
            if line_number:
                for i, line in enumerate(file):
                    if i + 1 == int(line_number):
                        return line.strip()
                return "Error: Line number out of range", 400
            else:
                return file.read()
    except FileNotFoundError:
        return "Error: File not found", 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
