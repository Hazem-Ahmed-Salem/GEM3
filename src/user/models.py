from django.db import models
from django.contrib.auth.models import UserManager ,AbstractBaseUser , PermissionsMixin
from uuid import    uuid4
from .utils import user_pph
from django.templatetags.static import static


class CustomUserManger(UserManager):
    
    def create_user(self, email, username, password,  is_staff=False, is_active=True, is_superuser=False):
        if not email:
            raise ValueError("You  have not provided a vaild e-mail !")
        if not password:
            raise ValueError("You  have not provided a vaild password !")
        if not username:
            raise ValueError("You  have not provided a vaild username !")
        user_obj = self.model(
            email=self.normalize_email(email),
            username=username,)
        user_obj.staff = is_staff
        user_obj.superuser = is_superuser
        user_obj.active = is_active
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj
    
    def create(self, data ,**kwargs):
        # override this method to be able to create a user
        return self.create_user(email=data['email'], username=data['username'], password=data['password'])

    def create_staff_user(self, email=None, password=None, username=None):
        user_obj = self.create_user(
            email,
            username,
            password,
            is_staff=True
        )
        return user_obj
    
    def create_superuser(self, email=None, password=None, username=None):
        user_obj = self.create_user(
            email,
            username,
            password,
            is_staff=True,
            is_superuser=True,
        )
        return user_obj
    

class User(AbstractBaseUser,PermissionsMixin):
    id                  = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    email               = models.EmailField(verbose_name="email",max_length=255,unique=True)
    username            = models.CharField(max_length=60,unique=True)
    first_name          = models.CharField(max_length=50,null=True,blank=True)
    last_name           = models.CharField(max_length=50,null=True,blank=True)
    date_joined         = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login          = models.DateTimeField(verbose_name="last login", auto_now=True)
    active              = models.BooleanField(default=True)
    staff               = models.BooleanField(default=False)
    superuser           = models.BooleanField(default=False)
    # profile_image       = models.ImageField(max_length=255,upload_to=//,null=True,blank=True,default=//)

    objects = CustomUserManger()
    USERNAME_FIELD ='email'
    # USERNAME_FIELD and password are required by default
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.username
    
    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


    @property
    def is_staff(self):
        return self.staff
    @property
    def is_active(self):
        return self.active
    @property
    def is_superuser(self):
        return self.superuser
    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    istourist= models.BooleanField("istourist")
    image = models.ImageField(upload_to=user_pph, null=True, blank=True)
    displayname = models.CharField(max_length=30, null=True, blank=True)
    info = models.TextField(null=True, blank=True) 



    def __str__(self):
        return str(self.user)

    @property
    def name(self):
        if self.displayname:
            name = self.displayname
        else :
            name = self.user.username
        return name

    @property
    def avatar(self):
        try:
            avatar=self.image.url
        except:
            avatar = static('images/avatar.svg')
        return avatar
