from django.shortcuts import render

# Create your views here.
def guide_view(request):
    return(render(request,"guides/guides.html"))

def mg_purchase_view(request):
    return(render(request,"guides/main_guide_purchase.html"))

def av1_purchase_view(request):
    return(render(request,"guides/av1_purchase.html"))