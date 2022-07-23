

from django.contrib.auth.models  import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class signupform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'EMAIL'}
class edituserprofile(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','date_joined','last_login','is_active']
        labels={'email':'EMAIL'}

       
