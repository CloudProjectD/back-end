from pydantic import BaseModel


class ReportUser(BaseModel):
    reported_id: int
    reason: str


class ReportResponse(ReportUser):
    reporter_id: int

    class Config:
        orm_mode = True
