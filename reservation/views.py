from django.shortcuts import render
from .forms import ReservetionForm

# Create your views here.
def reserve(request):
    reserve_from=ReservetionForm
    if request.method =='POST':
        reserve_from=ReservetionForm(request.POST)
        if reserve_from.is_valid():
            reserve_from.save()
    else:
        reserve_from=ReservetionForm()

    context={
        'form':reserve_from,
    }

    return render(request,'reserveation/reservation.html',context)
