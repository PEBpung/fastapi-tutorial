from typing import List

from pydantic import BaseModel


class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://kiminimage.com/image.png",
                "description": "Event 설명 예시입니다.",
                "tags": ["python", "fastapi", "planner", "launch"],
                "location": "Google Meet",
            }
        }
