from django.contrib.auth.models import User

from django.http import HttpResponseForbidden


def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        target_user = User.objects.get(pk=kwargs['pk'])
        # db에 접근해서 User 객체들을 가져오는데 주소창에 있는 pk를 kwargs에서 가져와 비교해서 특정 User를 선별한다.
        if target_user == request.user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden() # 만약 본인이 아니라면 오류페이지
    return decorated

