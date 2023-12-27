import datetime

from django.http import JsonResponse

from feedBack_app.models import FeedBack


def feedBack(request):
    create = FeedBack.objects.create(date=datetime.datetime.now(), user_id=1, text="dsdsf", rate=1)
    create2 = FeedBack.objects.create(date=datetime.datetime.now(), user_id=1, text="late1", rate=2)
    create3 = FeedBack.objects.create(date=datetime.datetime.now(), user_id=1, text="late2", rate=4)
    create4 = FeedBack.objects.create(date=datetime.datetime.now(), user_id=1, text="late3", rate=4)
    create.save()
    create4.save()
    create2.save()
    create3.save()
    feedbacks = FeedBack.objects.all().order_by("-date")
    json = list(feedbacks.values())
    print(json)
    map(lambda  x :print(x) , feedbacks )
    return JsonResponse(json , safe=False)

# Create your views here.
