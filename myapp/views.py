from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import ContactMessage, Recipe  # 👈 Import both models
from .models import ContactMessage, Recipe, Student
def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password != confirm_password:
            return HttpResponse("Error: Passwords do not match! Please go back and try again.")
            
        if User.objects.filter(username=username).exists():
            return HttpResponse("Error: That username is already taken!")

        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()
        
        return HttpResponse(f"Registration successful! User '{username}' is now saved in the database.")

    return render(request, 'myapp/home.html')


def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )
        
        return HttpResponse(f"Thank you {name}! Your message has been saved to the database.")

    return render(request, 'myapp/contact.html')


# 👇 1. CREATE & READ: Add a new recipe and display all saved recipes
def recipe_list(request):
    if request.method == "POST":
        title = request.POST.get('title')
        ingredients = request.POST.get('ingredients')
        prep_time = request.POST.get('prep_time')
        
        Recipe.objects.create(
            title=title,
            ingredients=ingredients,
            prep_time=prep_time
        )
        return redirect('recipe_list')

    recipes = Recipe.objects.all().order_by('-created_at')
    return render(request, 'myapp/recipes.html', {'recipes': recipes})


# 👇 2. UPDATE: Edit an existing recipe
def update_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if request.method == "POST":
        recipe.title = request.POST.get('title')
        recipe.ingredients = request.POST.get('ingredients')
        recipe.prep_time = request.POST.get('prep_time')
        recipe.save()
        return redirect('recipe_list')

    return render(request, 'myapp/update_recipe.html', {'recipe': recipe})


# 👇 3. DELETE: Remove a recipe
def delete_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    recipe.delete()
    return redirect('recipe_list')

# 1. CREATE & READ: Add a new student and display all registered students
def student_list(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        reg_number = request.POST.get('reg_number')
        email = request.POST.get('email')
        course = request.POST.get('course')

        Student.objects.create(
            full_name=full_name,
            reg_number=reg_number,
            email=email,
            course=course
        )
        return redirect('student_list')

    students = Student.objects.all().order_by('-created_at')
    return render(request, 'myapp/students.html', {'students': students})


# 2. UPDATE: Edit an existing student's details
def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        student.full_name = request.POST.get('full_name')
        student.reg_number = request.POST.get('reg_number')
        student.email = request.POST.get('email')
        student.course = request.POST.get('course')
        student.save()
        return redirect('student_list')

    return render(request, 'myapp/update_student.html', {'student': student})


# 3. DELETE: Remove a student record
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')

