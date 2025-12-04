# FastAPI SHA256 Checksum Service

This application provides two routes:
- **GET /**: Returns a welcome message.
- **POST /tokenize**: Accepts a JSON payload with a `text` field and returns the SHA256 checksum of the text.

## Requirements

- Python 3.8+
- Install dependencies:
  ```bash
  pip install fastapi uvicorn
  ```

## How to Run the App

1. Make sure all Python files (`main.py`, `input_text_model.py`, `checksum_util.py`) are in the same directory.

2. Start the FastAPI application using Uvicorn:

   ```bash
   uvicorn main:app --reload
   ```

   - The `--reload` option is useful in development; it automatically restarts the server on code changes.

3. The app will be running at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Testing the Endpoints

- **GET Welcome Message**
  ```bash
  curl http://127.0.0.1:8000/
  ```

- **POST Tokenize Text**
  ```bash
  curl -X POST http://127.0.0.1:8000/tokenize -H "Content-Type: application/json" -d '{"text": "hello"}'
  ```

## Running Tests

To run test cases (after installing `pytest`):

```bash
pip install pytest
pytest test_main.py
```