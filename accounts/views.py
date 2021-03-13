from django.shortcuts import render

# Create your views here.
from .forms import RegisterForm


def register(request):
    # 서버에 데이터가 전송됨을 의미
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            # new_user를 생성은 하지만 데이터베이스에 반영하지 않고 메모리 상에 생성
            new_user = user_form.save(commit=False)
            # password를 입력받고 난 뒤 실제로 데이터베이스에 저장
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = RegisterForm()

    return render(request, 'registration/register.html', {'form': user_form})
