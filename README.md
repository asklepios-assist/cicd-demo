# CI/CD Demo 🚀

A simple Flask API to learn CI/CD with GitHub Actions.

## What's here

- `app.py` — Simple Flask API with 3 endpoints
- `test_app.py` — Unit tests (pytest)
- `.github/workflows/ci.yml` — CI pipeline that runs tests on every push

## Endpoints

- `GET /` — Hello message
- `GET /health` — Health check
- `GET /add/<a>/<b>` — Add two numbers

## How CI works

1. You push code to GitHub
2. GitHub Actions automatically runs the tests
3. You see ✅ or ❌ on your commit
4. If tests pass → safe to deploy

## Run locally

```bash
pip install -r requirements.txt
python app.py          # Start the server
pytest test_app.py -v  # Run tests
```
