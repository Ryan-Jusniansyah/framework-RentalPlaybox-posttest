from django.shortcuts import render

# Views homepage.
def homepage(request):
    return render(request, "homepage/index.html")

# Views about
def about(request):
    return render(request, "homepage/about.html")

# Views rent
def rent(request):
    return render(request, "homepage/rent.html")