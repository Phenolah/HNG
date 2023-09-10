from django.http import JsonResponse
from django.utils import timezone
from datetime import datetime

def api(request):
    slack_name = request.GET.get('slack_name', 'example_name')
    track = request.GET.get('track', 'backend')
    current_day = timezone.now().strftime('%A')
    utc_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": "https://github.com/Phenolah/HNG/blob/main/EndpointApp/views.py",
        "github_repo_url": "https://github.com/Phenolah/HNG",
        "status_code": 200
    }
    return JsonResponse(response)

