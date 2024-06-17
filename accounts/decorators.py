from django.shortcuts import redirect



def ensure_email_verified(func):
    def wrapper(request,*args, **kwargs):
        if not request.user.profile.verified:
            return redirect('success')
        return func(request,*args, **kwargs)
    return wrapper