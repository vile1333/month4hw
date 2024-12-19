from django.shortcuts import render, redirect, get_object_or_404
from basket.models import Basket
from basket.forms import BasketForm
from django.views import generic


class CreateBasketView(generic.CreateView):
    template_name = 'basket/create_basket.html'
    form_class = BasketForm
    success_url = '/basket_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateBasketView, self).form_valid(form=form)

# Create your views here.
# def create_basket_view(request):
#     if request.method == 'POST':
#         form = BasketForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('basket_view')
#     else:
#         form = BasketForm()
#     return render(request, 'basket/create_basket.html', {'form': form})

class BasketListView(generic.ListView):
    template_name = 'basket/basket_list.html'
    context_object_name = 'basket_list'
    model = Basket

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

# def basket_list_view(request):
#     if request.method == 'GET':
#         basket_list = Basket.objects.all().order_by('-id')
#         context = {'basket_list': basket_list}
#         return render(request, 'basket/basket_list.html', context)

class BasketDetailView(generic.DetailView):
    template_name = 'basket/basket_detail.html'
    context_object_name = 'basket_id'

    def get_object(self,**kwargs):
        basket_id = self.kwargs.get('id')
        return get_object_or_404(Basket, id=basket_id)


# def basket_detail_view(request, id):
#     if request.method == 'GET':
#         basket_id = get_object_or_404(Basket, id=id)
#         context = {'basket_id': basket_id}
#         return render(request, 'basket/basket_detail.html', context)

class UpdateBasketView(generic.UpdateView):
    template_name = 'basket/basket_update.html'
    form_class = BasketForm
    success_url = '/basket_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateBasketView, self).form_valid(form=form)

    def get_object(self,**kwargs):
        basket_id = self.kwargs.get('id')
        return get_object_or_404(Basket, id=basket_id)

# def basket_update_view(request, id):
#     basket_id = get_object_or_404(Basket, id=id)
#     if request.method == 'POST':
#         form = BasketForm(request.POST,instance=basket_id)
#         if form.is_valid():
#             form.save()
#             return redirect('basket_view')
#     else:
#         form = BasketForm(instance=basket_id)
#     return render(request, 'basket/basket_update.html',context={'basket_id': basket_id, 'form': form})

class DeleteBasketView(generic.DeleteView):
    template_name = 'basket/basket_delete.html'
    success_url = '/basket_list/'

    def get_object(self,**kwargs):
        basket_id = self.kwargs.get('id')
        return get_object_or_404(Basket, id=basket_id)

# def basket_delete_view(request, id):
#     basket_id = get_object_or_404(Basket, id=id)
#     basket_id.delete()
#     return redirect('basket_view')
