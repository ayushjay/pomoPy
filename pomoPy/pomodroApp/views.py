from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from django.shortcuts import render, redirect
from django.urls import reverse

IST = ZoneInfo("Asia/Kolkata")
POMODORO_MINUTES_25 = 25
POMODORO_MINUTES_50 = 50


def Pomo50(request, username):
    if request.method == "POST":
        
        request.session["time_50"] = datetime.now(IST).isoformat()
        return redirect("pomodroApp:pomo50", username=username)

    start_time_str = request.session.get('time_50')
        
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

    return render(request, 'pomodroApp/pomoMain.html', {'time_left': time_left,"username":request.user.username})


def Pomo25(request, username):
    if request.method == "POST":
        
        request.session["time_25"] = datetime.now(IST).isoformat()
        return redirect("pomodroApp:pomo25", username=username)

    start_time_str = request.session.get('time_25')
        
    time_left = None

    if start_time_str:
        start_time = datetime.fromisoformat(start_time_str)
        end_time = start_time + timedelta(minutes=POMODORO_MINUTES_25)
        remaining = end_time - datetime.now(IST)

        if remaining.total_seconds() > 0:
            minutes = remaining.seconds // 60
            seconds = remaining.seconds % 60
            time_left = f"{minutes:02d}:{seconds:02d}"
        else:
            time_left = "Time's up!"

    return render(request, 'pomodroApp/pomoMain.html', {'time_left': time_left,"username":username})


