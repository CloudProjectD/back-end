from pydantic import BaseModel


class ReportUser(BaseModel):
    reported_user_name: str
    reason: str


class ReportResponse(BaseModel):
    reporter_id: int
    reported_id: int
    reason: str

    class Config:
        orm_mode = True
