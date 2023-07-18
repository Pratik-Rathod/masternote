from django.urls import path
from . import views
urlpatterns = [
    path('', name='home', view=views.home),
    # path('admin/', admin.site.urls),
    path('post/<int:post_id>', name='post', view=views.viewpost),
    path('new-note/', name='new-note', view=views.addnote),
]
