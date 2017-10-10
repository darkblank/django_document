from django.contrib import admin

from model.models import Car, Manufacturer, User, Pizza, Topping, FacebookUser, InstagramUser

admin.site.register(Car)
admin.site.register(Manufacturer)
admin.site.register(User)
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(FacebookUser)
admin.site.register(InstagramUser)