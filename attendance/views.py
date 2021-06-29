from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import SubmitAttendance
from .forms import SubmitAttendanceForm
import datetime as dt


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        form = SubmitAttendanceForm
        context = {
            'form': form,
            "user": request.user,
        }
        return render(request, 'attendance/index.html', context)


index = IndexView.as_view()


class ResultView(View):
    def post(self, request):
        form = SubmitAttendanceForm(request.POST)
        now = dt.datetime.now()
        month = now.month
        day = now.day
        hour = now.hour
        minute = now.minute

        obj = form.save(commit=False)
        obj.place = request.POST["place"]
        obj.in_out = request.POST["in_out"]
        obj.staff = request.user
        obj.date = dt.datetime.now().date() - dt.timedelta(hours=9)  # 日をまたいだ時、日付が変わらないように
        obj.time = dt.datetime.now().time()
        obj.save()

        if request.POST["in_out"] == '1':
            comment = str(month) + "月" + str(day) + "日" + str(hour) + "時" + str(minute) + "分" + "出勤確認しました。今日も頑張りましょう！"
        else:
            comment = str(month) + "月" + str(day) + "日" + str(hour) + "時" + str(minute) + "分" + "退勤確認しました。"
        context = {
            'place': SubmitAttendance.PLACES[int(obj.place) - 1][1],
            'comment': comment,
        }
        return render(request, 'attendance/result.html', context)


result = ResultView.as_view()
