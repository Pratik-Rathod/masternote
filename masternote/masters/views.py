from django.shortcuts import render,HttpResponse

# Create your views here.
def test(request):
    res = "<h1> hello world check rpasojd salkdjasldkjas asdkjask</h1>"
    return HttpResponse(res)

