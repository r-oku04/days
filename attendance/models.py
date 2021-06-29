from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class SubmitAttendance(models.Model):
    class Meta:
        db_table = 'attendance'

    PLACES = (
        (1, '本館'),
        (2, '２号館'),
        (3, '別館'),
    )
    IN_OUT = (
        (1, 'IN'),
        (0, 'OUT'),
    )

    staff = models.ForeignKey(get_user_model(), verbose_name="従業員", on_delete=models.CASCADE, default=None)
    place = models.IntegerField(verbose_name='出勤場所', choices=PLACES, default=None)
    in_out = models.IntegerField(verbose_name='IN/OUT', choices=IN_OUT, default=None)
    time = models.TimeField(verbose_name="打刻時間")
    date = models.DateField(verbose_name='打刻日')

    place_dict = dict(PLACES)
    in_out_dict = dict(IN_OUT)

    def __str__(self):
        return str(User.objects.get(id=self.staff_id)) + ' : ' + str(self.place_dict[self.place]) + ' ' + str(
            self.in_out_dict[self.in_out])
