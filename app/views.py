from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ProfileForm
from .serializers import ProfileSerializer
from .models import Profile
from rest_framework import generics
# def ProfileView(request):
#         profile=Profile.objects.all()
#         context={'profile':profile}
#         return render(request,'profile.html',context)
# def ProfilePost(request):
#     if request.method=='POST':
#         form=ProfileForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/api/get/') 
#     else:
#            form=ProfileForm()
#     return render(request,'post.html',{'form':form})
class ProfileView(generics.ListAPIView):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
class ProfilePost(generics.CreateAPIView):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer