from django.urls import path
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('new-note/',name='new-note',view=views.addnote),
]