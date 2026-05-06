from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

# Vulnerable endpoint
@app.route('/parse', methods=['POST'])
def parse_yaml():
    try:
        data = request.data.decode("utf-8")

        # ❌ Vulnerable: yaml.load allows code execution
        parsed = yaml.load(data, Loader=yaml.Loader)

        return jsonify({
            "status": "success",
            "parsed": parsed
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

# Safe endpoint (for comparison)
@app.route('/safe-parse', methods=['POST'])
def safe_parse_yaml():
    data = request.data.decode("utf-8")

    # ✅ Safe
    parsed = yaml.safe_load(data)

    return jsonify({
        "status": "safe",
        "parsed": parsed
    })

if __name__ == '__main__':
    app.run(debug=True)