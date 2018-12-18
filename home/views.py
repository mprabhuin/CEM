from django.shortcuts import render

# Create your views here.
def index(request):
    """View function for home page of site."""

    # the context variable used in the render function, a context variable, which is a Python dictionary, containing the data to insert into the placeholders.
    context = {
        
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

