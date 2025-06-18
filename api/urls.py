from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# this router thing will not require basename for modelview sets 
router.register('employees',views.EmployeeViewSet,basename='employees')
urlpatterns = [
    # path('students',views.studentView),
    # path('students/<int:pk>/',views.studentDetailView),
    # path('teachers',views.teacherView),
    # path('teachers/<int:pk>',views.teacherDetailView),
    # path('employees/',views.Employees.as_view()) ,# creating a class based view, always it should be
    # path('employees/<int:pk>',views.Employee_detail.as_view()),                            #.as_view
    path('',include(router.urls)),
    path('blogs/',views.BlogView.as_view()),
    path('blogs/<int:pk>',views.BlogDetailView.as_view()),
    path('comments/',views.CommentView.as_view()),
    path('comments/<int:pk>',views.CommentDetailView.as_view()),

    
]
