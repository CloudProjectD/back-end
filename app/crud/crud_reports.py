from sqlalchemy.orm import Session
from app.models.schemas.reports import Report
from app.models.domain.reports import ReportUser, ReportResponse
from app.models.schemas.users import User
from fastapi import HTTPException


def create_report(
    db: Session, reporter_id: int, report_in: ReportUser
) -> ReportResponse:
    # Get the reported user by user's id
    reported_user = db.query(User).filter(User.id == report_in.reported_id).first()

    if not reported_user:
        raise HTTPException(status_code=400, detail="Reported user not found")

    # Create the report
    report = Report(
        reporter_id=reporter_id, reported_id=reported_user.id, reason=report_in.reason
    )
    db.add(report)
    db.commit()
    db.refresh(report)

    report_response = ReportResponse(
        reporter_id=report.reporter_id,
        reported_id=report.reported_id,
        reason=report.reason,
    )
    return report_response
