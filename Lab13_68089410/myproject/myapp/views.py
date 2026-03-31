from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from myapp.models import Person
from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import Person
from django.db.models import Q

def index(request):
    # รับค่าค้นหา
    query = request.GET.get('q')

    # ถ้ามีการค้นหา
    if query:
        all_person = Person.objects.filter(
            Q(name__icontains=query) | Q(age__icontains=query)
        )
    else:
        all_person = Person.objects.all()

    return render(request, "index.html", {
        "all_person": all_person
    })
def about(request):
    return render(request, 'about.html')

# เพิ่มข้อมูล
def add_person(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")

        if name and age:
            try:
                age = int(age)
                Person.objects.create(name=name, age=age)
                return redirect("/")
            except ValueError:
                error = "กรุณากรอกอายุเป็นตัวเลข"
                return render(request, "form.html", {"error": error, "person": {"name": name, "age": age}})
        else:
            error = "กรุณากรอกข้อมูลให้ครบ"
            return render(request, "form.html", {"error": error, "person": {"name": name, "age": age}})
    
    return render(request, "form.html")

# แก้ไขข้อมูล
def edit(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    if request.method == "POST":
        name = request.POST.get("name")
        age = int(request.POST.get("age"))
        person.name = name
        person.age = age
        person.save()
        return redirect("/")
    return render(request, "form.html", {"person": person})

# ลบข้อมูล
def delete(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    person.delete()
    return redirect("/")