from django.shortcuts import render, redirect, get_object_or_404
from basket.models import Basket
from basket.forms import BasketForm

# Create your views here.
def create_basket_view(request):
    if request.method == 'POST':
        form = BasketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('basket_view')
    else:
        form = BasketForm()
    return render(request, 'basket/create_basket.html', {'form': form})

def basket_list_view(request):
    if request.method == 'GET':
        basket_list = Basket.objects.all().order_by('-id')
        context = {'basket_list': basket_list}
        return render(request, 'basket/basket_list.html', context)

def basket_detail_view(request, id):
    if request.method == 'GET':
        basket_id = get_object_or_404(Basket, id=id)
        context = {'basket_id': basket_id}
        return render(request, 'basket/basket_detail.html', context)

def basket_update_view(request, id):
    basket_id = get_object_or_404(Basket, id=id)
    if request.method == 'POST':
        form = BasketForm(request.POST,instance=basket_id)
        if form.is_valid():
            form.save()
            return redirect('basket_view')
    else:
        form = BasketForm(instance=basket_id)
    return render(request, 'basket/basket_update.html',context={'basket_id': basket_id, 'form': form})

def basket_delete_view(request, id):
    basket_id = get_object_or_404(Basket, id=id)
    basket_id.delete()
    return redirect('basket_view')
