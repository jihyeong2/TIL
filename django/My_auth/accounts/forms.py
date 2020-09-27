from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.conf import settings
from django.contrib.auth import get_user_model


class CustomUserChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm.Meta):
        # model=settings.AUTH_USER_MODEL
        model=get_user_model()
        fields=('email','first_name','last_name',)

        
class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        # model=settings.AUTH_USER_MODEL
        model=get_user_model()
        fields = UserCreationForm.Meta.fields + ('email',)