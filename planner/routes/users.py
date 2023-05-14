from fastapi import APIRouter, HTTPException, status

from models.users import User, UserSignIn

# user router 객체 생성
user_router = APIRouter(tags=["User"])

users = {}


# 회원가입 진행
@user_router.post("/signup")
async def sign_new_user(data: User) -> dict:
    if data.email in users:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="사용자의 Email이 이미 존재합니다.")
    users[data.email] = data
    return {"message": "User successfully registered!"}


# 로그인 진행
@user_router.post("signin")
async def sign_user_in(user: UserSignIn) -> dict:
    if user.email not in users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="사용자가 존재하지 않습니다.")

    if user[user.email].password != user.password:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="비밀번호가 일치하지 않습니다.")
    return {"message": "User signed in successfully"}
