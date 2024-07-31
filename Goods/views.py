from django.shortcuts import render
from . import models
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



def paginator_page(data, num, request):
    paginator = Paginator(data.order_by('-id'), num)
    pages = request.GET.get('page')
    try:
        paginated_list = paginator.page(pages)
    except PageNotAnInteger:
        paginated_list = paginator.page(1)
    except EmptyPage:
        paginated_list = paginator.page(paginator.num_pages)
    return paginated_list

def main(request):
    banners = models.Banner.objects.all()
    category = models.Category.objects.all()
    last_img = models.ProductImg.objects.all()
    wishlist = models.WishList.objects.all()
    
    context = {}
    context['banners'] = banners
    context['categories'] = category
    context['products'] = paginator_page(last_img, 8 , request)
    context['wishlist'] = wishlist

    return render(request, 'index.html', context)


def user(request):
    return render(request, 'user/detail.html')

def category(request):
    return render(request, 'user/like.html')
# from django.shortcuts import render, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from .models import  Preference


# @login_required
# def createpost(request):
#         if request.method == 'POST':
#             if request.POST.get('title') and request.POST.get('content'):
#                 post=models.Product()
#                 post.title= request.POST.get('title')
#                 post.content= request.POST.get('content')
#                 post.author= request.user
#                 post.save()
                

#                 return render(request, 'user/like.html')  

        

#         else:
#                 return render(request,'user/like.html')


# def home(request):
#         allposts= models.Product.objects.all()

#         context={'allposts': allposts }

#         return render(request, 'user/like.html', context)


# def detail_post_view(request, id=None):
#         eachpost= get_object_or_404(models.Product, id=id)

        

#         context={'eachpost': eachpost}

#         return render (request, 'user/like.html', context)
# def some_view(request):
#     from .models import Preference


# @login_required
# def postpreference(request, postid, userpreference):
        
#         if request.method == "POST":
#                 eachpost= get_object_or_404(models.Product, id=postid)

#                 obj=''

#                 valueobj=''

#                 try:
#                         obj= Preference.objects.get(user= request.user, post= eachpost)

#                         valueobj= obj.value #value of userpreference


#                         valueobj= int(valueobj)

#                         userpreference= int(userpreference)
                
#                         if valueobj != userpreference:
#                                 obj.delete()


#                                 upref= Preference()
#                                 upref.user= request.user

#                                 upref.post= eachpost

#                                 upref.value= userpreference


#                                 if userpreference == 1 and valueobj != 1:
#                                         eachpost.likes += 1
#                                         eachpost.dislikes -=1
#                                 elif userpreference == 2 and valueobj != 2:
#                                         eachpost.dislikes += 1
#                                         eachpost.likes -= 1
                                

#                                 upref.save()

#                                 eachpost.save()
                        
                        
#                                 context= {'eachpost': eachpost,
#                                   'postid': postid}

#                                 return render (request, 'user/like.html', context)

#                         elif valueobj == userpreference:
#                                 obj.delete()
                        
#                                 if userpreference == 1:
#                                         eachpost.likes -= 1
#                                 elif userpreference == 2:
#                                         eachpost.dislikes -= 1

#                                 eachpost.save()

#                                 context= {'eachpost': eachpost,
#                                   'postid': postid}

#                                 return render (request, 'user/like.html', context)
                                
                        
        
                
#                 except Preference.DoesNotExist:
#                         upref= Preference()

#                         upref.user= request.user

#                         upref.post= eachpost

#                         upref.value= userpreference

#                         userpreference= int(userpreference)

#                         if userpreference == 1:
#                                 eachpost.likes += 1
#                         elif userpreference == 2:
#                                 eachpost.dislikes +=1

#                         upref.save()

#                         eachpost.save()                            


#                         context= {'eachpost': eachpost,
#                           'postid': postid}

#                         return render (request, 'user/like.html', context)


#         else:
#                 eachpost= get_object_or_404(Post, id=postid)
#                 context= {'eachpost': eachpost,
#                           'postid': postid}

#                 return render (request, 'user/like.html', context)

