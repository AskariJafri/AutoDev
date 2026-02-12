from backend.models import UserActivities
import pytest

def test_log_and_retrieve_activity():
    user_id = "123"
    activities = UserActivities(user_id)
    activities.log_activity("login")
    activities.log_activity("api_access", timestamp="2023-07-10 14:00:00")
    
    recent_activities = activities.tracker.get_recent_activities()
    
    assert len(recent_activities) == 2
    assert recent_activities[0]['action'] == 'api_access'