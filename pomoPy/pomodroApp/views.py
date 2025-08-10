from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from django.shortcuts import render, redirect
from django.urls import reverse

IST = ZoneInfo("Asia/Kolkata")
POMODORO_MINUTES_25 = 25
POMODORO_MINUTES_50 = 50

def Pomo50(request, username):
    url_to_be_rev_by_redirect = reverse('pomodroApp:pomo50', kwargs={'username':username})
    if request.method == "POST":
        request.session['start_time'] = datetime.now(IST).isoformat()
        return redirect(url_to_be_rev_by_redirect)

    
    start_time_str = request.session.get('start_time')
    time_left = None

    if start_time_str:
        start_time = datetime.fromisoformat(start_time_str)
        end_time = start_time + timedelta(minutes=POMODORO_MINUTES_50)
        remaining = end_time - datetime.now(IST)

        if remaining.total_seconds() > 0:
            minutes = remaining.seconds // 60
            seconds = remaining.seconds % 60
            time_left = f"{minutes:02d}:{seconds:02d}"
        else:
            time_left = "Time's up!"

    return render(request, 'pomoMain.html', {'time_left': time_left,"username":username})
