from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.core.exceptions import FieldError
from phone_field import PhoneField
from django.db.models import DecimalField, FloatField
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class MyUserManager(BaseUserManager):
    def create_user(self, full_name, email, phone_number, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            full_name=full_name,
            email = self.normalize_email(email),
            phone_number=phone_number
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,full_name, email, phone_number, password=None):
        user = self.create_user(
            full_name,
            email,
            phone_number=phone_number,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    full_name = models.CharField(db_index=True, max_length=255)
    phone_number = models.CharField(blank=True, help_text='Contact phone number', max_length=10)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'phone_number']

    # def __init__(self, is_active=True, is_admin=True):
    #     self.is_active = is_active
    #     self.is_admin = is_admin

    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
    8000
    @property
    def is_staff(self):
        return self.is_admin

 


class Owner(MyUser, PermissionsMixin):
   
    # user = models.OneToOneField(MyUser, on_delete = models.CASCADE, primary_key = True)
    current_longitude = models.FloatField( validators=[MinValueValidator(-180), MaxValueValidator(180)], default=None)
    current_latitude = models.FloatField( validators=[MinValueValidator(-180), MaxValueValidator(180)], default=None)
    previous_longitude = models.FloatField( validators=[MinValueValidator(-180), MaxValueValidator(180)], default=None)
    previous_latitude = models.FloatField( validators=[MinValueValidator(-180), MaxValueValidator(180)], default=None)
    is_registered = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='images/owner') 
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
 
    objects = MyUserManager()

    def __init__(self, *args, **kwargs):
        self._meta.get_field('is_active').default = False
        self._meta.get_field('is_admin').default = False
        super(Owner, self).__init__(*args, **kwargs)

       

  
 
    def __str__(self):
        return self.full_name


 
class Driver(MyUser, PermissionsMixin):
    # user = models.OneToOneField(MyUser, on_delete = models.CASCADE, primary_key = True)
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    is_registered = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='images/driver') 
    current_latitude = models.FloatField( validators=[MinValueValidator(-180), MaxValueValidator(180)], default=None)
    current_longitude = models.FloatField( validators=[MinValueValidator(-180), MaxValueValidator(180)], default=None)
    previous_latitude = models.FloatField( validators=[MinValueValidator(-180), MaxValueValidator(180)], default=None)
    previous_longitude = models.FloatField( validators=[MinValueValidator(-180), MaxValueValidator(180)], default=None)
    
   


 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
 
    objects = MyUserManager()

    def __init__(self, *args, **kwargs):
        self._meta.get_field('is_active').default = False
        self._meta.get_field('is_admin').exdefault = False
        super(Driver, self).__init__(*args, **kwargs)

     
 
    def __str__(self):
        return self.full_name

class Passenger(MyUser, PermissionsMixin):
    # user = models.OneToOneField(MyUser, on_delete = models.CASCADE, primary_key = True)
    profile_pic = models.ImageField(upload_to='images/passenger', null =True) 
    current_latitude = models.FloatField( validators=[MinValueValidator(-180), MaxValueValidator(180)], default=None, null =True)
    current_longitude = models.FloatField( validators=[MinValueValidator(-180), MaxValueValidator(180)], default=None, null= True)
    previous_latitude = models.FloatField( validators=[MinValueValidator(-180), MaxValueValidator(180)], default=None, null= True)
    previous_longitude = models.FloatField( validators=[MinValueValidator(-180), MaxValueValidator(180)], default=None, null = True)
    
   


 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
 
    objects = MyUserManager()

    def __init__(self, *args, **kwargs):
        self._meta.get_field('is_active').default = True
        self._meta.get_field('is_admin').exdefault = False
        super(Passenger, self).__init__(*args, **kwargs)

     
 
    def __str__(self):
        return self.full_name