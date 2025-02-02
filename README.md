# Fletora

Build frontend applications in Python. Yeah, I know, it sounds CRAZY!

## Name Origin

A sleek, futuristic name that feels fresh and unique.

> _DeepSeek AI_

---

## UV Setup Instructions

### 1. Install `uv` (if not already installed)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Create and activate a virtual environment

```bash
uv venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate     # On Windows
```

### 3. Install dependencies

```bash
uv sync
```

---

## Pip Setup Instructions

### 1. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate     # On Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application Server

### Using FastAPI CLI

```bash
fastapi dev samples/main.py
```

### Using Uvicorn

```bash
python samples/main.py
```

The application will be available at `http://localhost:8000`.

---

## Development

To enable hot reloading during development, the server automatically watches for file changes and refreshes the browser.

## Resources

- [PyScript GitHub](https://github.com/pyscript/pyscript)
