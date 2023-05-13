## FastAPI 튜토리얼

### poetry 설치
```bash
# Mac 환경
brew install poetry
# pip 환경
pip install poetry
```


```bash
# poetry 설정
poetry build
```


```bash
# API 실행
poetry run uvicorn todo.api:app --reload
```