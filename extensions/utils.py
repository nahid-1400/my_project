from . import jalali
from django.utils import timezone
def django_jalali_converter(time):
    time = timezone.localtime(time)
    j_mount = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']
    time_to_str = "{},{},{}".format(time.year, time.month, time.day)
    time_to_persian_tuple = jalali.Gregorian(time_to_str).persian_tuple()
    time_to_persian_list = list(time_to_persian_tuple)

    for index, month in enumerate(j_mount):
        if time_to_persian_list[1] == index + 1:
            time_to_persian_list[1] = month
            break

    output = '{} {} {} ساعت {}:{}'.format(
        time_to_persian_list[2],
        time_to_persian_list[1],
        time_to_persian_list[0],
        time.hour,
        time.minute,
    )
    return output