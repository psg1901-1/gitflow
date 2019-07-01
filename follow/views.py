from django.shortcuts import render

def follow(request):
    return render(request,'follow.html',{})
def unfollow(request):
    return render(request,'unfollow.html',{})
