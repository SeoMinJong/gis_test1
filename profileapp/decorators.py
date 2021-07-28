from django.http import HttpResponseForbidden

from profileapp.models import Profile


def profile_ownership_reqired(func):
    def decorated(request, *args, **kwargs):
        target_profile = Profile.objects.get(pk=kwargs['pk'])  # db에서 가져올 때는 해당 model에서 가져와야 한다.
        if target_profile.user == request.user:
            return func(request, *args, **kwargs)
        else:
            return(HttpResponseForbidden())
    return decorated
