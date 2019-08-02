import random
from .models import *
from community.models import *

# crontab에 지정된 함수 이름을 실행.
# (settings.py의 CRONJOBS 부분의 지정된 함수 이름을 통해 실행 가능.)
def my_scheduled_job():
    # HotDealNumber 모델의 product_rnd_number 필드 레코드가 4개 이므로,
    # 해당 레코드 하나하나를 랜덤 숫자로 변경, 저장시키기 위해 총 4번의 save를 실행.
    for i in range(1, 5):
        num = random.randrange(0, 181)
        HotDealNumber(id=i, product_rnd_number=num).save()

    for j in range(1, 4):
        num_2nd = random.randrange(0, 18)
        HotStoryNumber(id=j, product_rnd_number=num_2nd).save()

    HotStoryNumber(id=5, product_rnd_number=random.randrange(0, 18)).save()
    # CronLog 모델에 랜덤으로 들어간 숫자의 이력을 생성함. 단순히 저장된 날짜,시간만을 표시!
    CronLog.objects.create()



