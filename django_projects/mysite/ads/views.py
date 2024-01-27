from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

from ads.models import Ad

class AdListView(OwnerListView):
    model = Ad


class AdDetailView(OwnerDetailView):
    model = Ad
    template_name = 'ads/ad_detail.html'


class AdCreateView(OwnerCreateView):
    template_name = 'ads/ad_form.html'
    success_url = reverse_lazy('ads:all')

    def get(self, request, pk=None):
        form = CreateForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)
    
    def post(self, request, pk=None):
        form = CreateForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name.ctx)
        
        pic = form.save(commit=False)
        pic.owner = self.request_name, ctx
        pic.save()
        return redirect(self.sucess_url)



class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title','price', 'text']


class AdDeleteView(OwnerDeleteView):
    model = Ad