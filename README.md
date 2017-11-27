
## User 등록 방법

```shell
$ python manage.py shell
>>> from django.contrib.auth.models import User
>>> user = User.objects.create_user(username = '2012123123', password = '1234') # 등록
>>> User.objects.all() # 전체 User 리스트 확인
```

## User 삭제 방법

```shell
$ python manage.py shell
>>> from django.contrib.auth.models import User
>>> User.objects.all().delete() # 전체 User 리스트 삭제
```

## UserCheck 삭제 방법

```shell
$ python manage.py shell
>>> from main.models import UserCheck
>>> UserCheck.objects.all().delete() # 전체 User 리스트 삭제
```
