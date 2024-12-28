# Flask-S3-Bucket-Content-Viewer 

This is a simple Flask application that simulates listing the contents of an S3 bucket. The application provides an HTTP endpoint to view the contents of a bucket at various paths in JSON format.

## Features

- **GET /list-bucket-content/**: Returns the top-level contents of the simulated S3 bucket.
- **GET /list-bucket-content/<path>**: Returns the contents of a specified path in the bucket.
- Supports multiple paths and displays the structure in JSON format.

---

## Example Usage

### Sample S3 Bucket Structure
```plaintext
|-- dir1
|-- dir2
|   |-- file1
|   |-- file2
|-- file1
|-- file2

Here’s a sample README.md file for your Flask project:

markdown
Copy code
# Flask S3 Bucket Content Viewer

This is a simple Flask application that simulates listing the contents of an S3 bucket. The application provides an HTTP endpoint to view the contents of a bucket at various paths in JSON format.

## Features

- **GET /list-bucket-content/**: Returns the top-level contents of the simulated S3 bucket.
- **GET /list-bucket-content/<path>**: Returns the contents of a specified path in the bucket.
- Supports multiple paths and displays the structure in JSON format.

---

## Example Usage

### Sample S3 Bucket Structure
```plaintext
|-- dir1
|-- dir2
|   |-- file1
|   |-- file2
|-- file1
|-- file2

##Endpoints
1 List Top-Level Contents
GET http://<IP>:<PORT>/list-bucket-content/
Response: {"content": ["dir1", "dir2", "file1", "file2"]}
2 List Contents of dir1
GET http://<IP>:<PORT>/list-bucket-content/dir1
Response: {"content": []}
3 List Contents of dir2
GET http://<IP>:<PORT>/list-bucket-content/dir2
Response: {"content": ["file1", "file2"]}


