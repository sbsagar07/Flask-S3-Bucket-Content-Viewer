from flask import Flask, jsonify

# Create a Flask app instance
app = Flask(__name__)

# Simulated S3 bucket structure
bucket_content = {
    "": ["dir1", "dir2", "file1", "file2"],  # Top-level directory
    "dir1": [],                             # 'dir1' is empty
    "dir2": ["file1", "file2"]              # 'dir2' contains two files
}

@app.route('/list-bucket-content/', defaults={'path': ''}, methods=['GET'])
@app.route('/list-bucket-content/<path:path>', methods=['GET'])
def list_bucket_content(path):
    if path in bucket_content:
        return jsonify({"content": bucket_content[path]})
    else:
        return jsonify({"error": "sagar"}), 404

if __name__ == '__main__':
    app.run(host='172.26.80.1', port=5000)
