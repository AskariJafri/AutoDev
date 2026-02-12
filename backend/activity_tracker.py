from datetime import datetime
from typing import Dict, Optional

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from backend.models import User, Activity
from backend.database import get_db
from backend.auth import get_current_user

router = APIRouter()

@router.post("/track-activity")
async def record_activity(
    activity_data: Dict[str, str],
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Endpoint for recording user activities"""
    
    if not current_user:
        raise HTTPException(status_code=401, detail="Authentication required")
        
    # Create new activity record
    activity = Activity(
        user_id=current_user.id,
        timestamp=datetime.utcnow(),
        action=activity_data.get("action", "unknown"),
        details=activity_data.get("details", "{}")
    )
    
    db.add(activity)
    db.commit()
    
    return JSONResponse(
        content={"message": "Activity recorded successfully"},
        status_code=201
    )