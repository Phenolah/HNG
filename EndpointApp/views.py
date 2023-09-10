from django.http import JsonResponse
from django.utils import timezone
import datetime

def api(request):
    slack_name = request.GET.get('slack_name', 'Phenolah')
    track = request.GET.get('track', 'Backend')
    current_day = timezone.now().strftime('%A')
    utc_time = timezone.now() + datetime.timedelta(minutes=2)
    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time.strftime('%Y-%m-%dT%H:%M:%SZ'),
        "track": track,
        "github_file_url": "https://github.com/Phenolah/HNG/blob/main/EndpointApp/views.py",
        "github_repo_url": "https://github.com/Phenolah/HNG",
        "status_code": 200
    }
    return JsonResponse(response)

