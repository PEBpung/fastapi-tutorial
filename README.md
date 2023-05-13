## FastAPI 튜토리얼

### Docker로 실행
```bash
# docker build
DOCKER_BUILDKIT=1 docker build -t fastapi_todo .
# docker run 
docker run -itd -p 8000:8000 --name fastapi_todo fastapi_todo:latest 
```
### Poetry로 실행
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