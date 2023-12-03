from typing import Any
from app.models.domain.reports import ReportUser, ReportResponse
from app.crud.crud_reports import create_report
from sqlalchemy.orm import Session
from app.api.dependencies import database
from fastapi import APIRouter, Depends
from app.services.user_manager import current_active_user
from app.crud.crud_users import get_user_by_email
from app.db.fastapi_user import User


router = APIRouter()


@router.post("", description="악성 사용자를 신고합니다.")
def report_user(
    *,
    db: Session = Depends(database.get_db),
    current_user: User = Depends(current_active_user),
    report_in: ReportUser
) -> Any:
    reporter_id = get_user_by_email(db=db, email=current_user.email).id

    report = create_report(
        db=db,
        reporter_id=reporter_id,
        report_in=report_in,
    )
    return {"message": "Report submitted successfully", "report_record": report}
