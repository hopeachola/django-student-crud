from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('contact/', views.contact_view, name='contact'),
    
    # 👇 New CRUD routes
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('recipes/update/<int:id>/', views.update_recipe, name='update_recipe'),
    path('recipes/delete/<int:id>/', views.delete_recipe, name='delete_recipe'),

    path('students/', views.student_list, name='student_list'),
    path('students/update/<int:id>/', views.update_student, name='update_student'),
    path('students/delete/<int:id>/', views.delete_student, name='delete_student'),

]