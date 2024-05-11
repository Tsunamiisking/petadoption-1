from django.contrib import admin
from petadoption1.models import User, Category, Pet, Featured_Pet, CommentNew
# Register your models here.


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Featured_Pet)
admin.site.register(Pet)
admin.site.register(CommentNew)