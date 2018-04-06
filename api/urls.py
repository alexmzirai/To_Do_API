from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'', views.ListTodo.as_view()),
    url(r'^<int:pk>/', views.DetailTodo.as_view()),

]

'''router = DefaultRouter()
router.register('', TodoViewSet, base_name='todos')
urlpatterns = router.urls'''


