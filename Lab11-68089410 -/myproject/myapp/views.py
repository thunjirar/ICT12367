from django.shortcuts import render, redirect
from myapp.models import Person

# หน้าแรก
def index(request):
    all_person = Person.objects.all()
    return render(request, 'index.html', {"all_person": all_person})

# หน้า about
def about(request):
    return render(request, 'about.html')

# ฟอร์ม
def form(request):
    if request.method == "POST":
        # รับข้อมูลจากฟอร์ม
        name = request.POST.get("name")
        age = request.POST.get("age")

        # บันทึกข้อมูล
        Person.objects.create(
            name=name,
            age=age
        )

        # กลับหน้าแรก
        return redirect("/")

    else:
        return render(request, "form.html")