from django.contrib import admin
from django.urls import path

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("personentry/", hello.views.personentry, name="personentry"),
    path("admin/", admin.site.urls),
    path("use/", hello.views.use),
    path("newbase/", hello.views.newbase),
    path("quiz/", hello.views.quiz),
    path("login/", hello.views.login),

]
