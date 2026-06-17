# Ignite Resume Parser

A comprehensive resume parsing solution using FastAPI, OCR, and AI/LLM technologies.

## Project Structure

```
ignite-resume-parser/
├── app/
│   ├── api/           # API endpoints
│   ├── core/          # Configuration and core utilities
│   ├── parsers/       # Resume parsing logic
│   ├── ai/            # AI and LLM integration
│   ├── models/        # Data models
│   ├── services/      # Business logic
│   ├── database/      # Database configuration
│   └── main.py        # Application entry point
├── tests/             # Test suite
├── uploads/           # Uploaded resume files
├── requirements.txt   # Python dependencies
├── Dockerfile         # Docker configuration
├── docker-compose.yml # Docker Compose setup
└── README.md          # This file
```

## Setup

### Prerequisites
- Python 3.11+
- Docker and Docker Compose (for containerized setup)
- Tesseract OCR

### Installation

1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
```bash
cp .env.example .env
```

## Running the Application

### Local Development
```bash
uvicorn app.main:app --reload
```

### Docker
```bash
docker-compose up --build
```

## API Endpoints

- `GET /health` - Health check
- `POST /upload` - Upload resume file
- `POST /parse` - Parse resume and extract data

## Testing

```bash
pytest
```

## License

MIT
