from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from book.models import BookInfo,PeopleInfo
from django.db.models import F,Q,Sum


# Create your views here.
# path('index/',index),
def index(request):
    return HttpResponse('index')
#     path('<int:city_id>/<phone:Mobile>',shop),
def shop(request,city_id,Mobile):
    return JsonResponse({'city_id':city_id,'Mobile':Mobile})

#     path('register/',register),
def register(request):
    username = request.POST.get('username')
    pwd = request.POST.get('password')
    return HttpResponse('账号:{},密码:{}'.format(username,pwd))
    pass

#     path('json/',json),

def json(request):
    json_str = request.body.decode()
    import json
    data_dict = json.loads(json_str)
    return JsonResponse(data_dict)


#     path('method/',method),
def method(request):
    return HttpResponse(request.method)
#     path('response/',response),
def response(request):
    response = HttpResponse({'a':3,'b':5})
    return response
    pass
#     path('set_cookie/',set_cookie),
def set_cookie(request):
    username = request.GET['username']
    response = HttpResponse(username)
    response.set_cookie('username',username)
    return response

#     path('get_cookie/',get_cookie),
def get_cookie(request):
    a = request.COOKIES
    print(a)
    return HttpResponse(a['username'])

#     path('set_session/',set_session),
def set_session(request):
    user_id = request.GET.get('user_id')
    username = request.GET.get('username')
    request.session['user_id'] = user_id
    request.session['username'] = username
    request.session.flush()
    return HttpResponse('set_session')

def get_session(request):
    user_id = request.session.get('user_id')
    user_name = request.session.get('username')
    content = 'id:{},账户:{}'.format(user_id,user_name)
    return HttpResponse(content)

    pass
#     path('get_session/',get_session),


#     path('login/',login),
def login(request):
    if request.method == 'GET':
        return HttpResponse('get')
    else:
        return HttpResponse('post')


#     path('LV/',LoginView.as_view())
from django.views import View
class LoginView(View):
    def get(self,request):
        return HttpResponse('get')
    def pos(self,request):
        return HttpResponse('post')






# def index(request):
#
#     return HttpResponse('ok')
#
# def shop(request,city_id,Mobile):
#     Query_dict = request.GET
#     print(Query_dict)
#     order = Query_dict.get('order')
#     print(city_id,Mobile)
#     return HttpResponse(f'欢迎来到胡灿的小店：city_id:{city_id},shop_id:{Mobile}')
#
# def register(request):
#     Query_dict=request.POST
#     print(Query_dict)
#     return HttpResponse(Query_dict)
#
#
# def json(request):
#     data = request.body
#     json_str= data.decode()
#     import json
#     data_dict = json.loads(data)
#     print(data_dict)
#     return HttpResponse('{},{}'.format(data_dict['name'],data_dict['age']))
#
#
# def method(request):
#     data= request.method
#     return HttpResponse(data)
#
#
# from django.http import HttpResponse,JsonResponse
# def response(request):
#     response = HttpResponse('res',status=200)
#     response['name']= 'itcast'
#     return response
#
#
# def set_cookie(request):
#     name=request.GET.get('username')
#     response = HttpResponse('ok')
#     response.set_cookie('name',name)
#     return response
#
# def get_cookie(request):
#     cookie1 = request.COOKIES.get('name')
#     print(cookie1)
#     return HttpResponse(cookie1)
#
# def set_session(request):
#     name = request.GET.get('username')
#     user_id = 1
#     request.session['user_id'] = user_id
#     request.session['username'] = name
#     request.session.set_expiry(3600)
#     return HttpResponse('set_session')
#
# def get_session(request):
#     user_id = request.session.get('user_id')
#     username = request.session.get('username')
#     content = '{},{}'.format(user_id,username)
#     return HttpResponse(content)
#
# def login(request):
#     if request.method == 'GET':
#         return HttpResponse('get')
#     else:
#         return HttpResponse('post')
#
# from django.views import View
#
# class LoginView(View):
#     def get(self,request):
#         return HttpResponse('get get')
#     def post(self,request):
#         return HttpResponse('post post')


# book1 = BookInfo.objects.create(
#     name='java入门',
#     pub_date= '2020-1-3'
# )
#
# person = PeopleInfo.objects.create(
#     name='itheima',
#     book = book1
# )
#
# PeopleInfo.objects.filter(name='itheima').update(name='传智播客')

# person = PeopleInfo.objects.get(name='传智播客')
# person.delete()
#
# BookInfo.objects.filter(name='django').delete()

# BookInfo.objects.get(id=1)
# BookInfo.objects.get(pk=2)
# BookInfo.objects.all()
# PeopleInfo.objects.all()
# BookInfo.objects.count()

# 查询编号为1的图书



# 查询书名包含'湖'的图书

# BookInfo.objects.filter(name__contains='湖')
# 查询书名以'部'结尾的图书

# BookInfo.objects.filter(name__endswith='部')

# 查询书名为空的图书

# BookInfo.objects.filter(name__isnull=True)

# 查询编号为1或3或5的图书

# BookInfo.objects.filter(id__in=[1,3,5])

# 查询编号大于3的图书

# BookInfo.objects.filter(id__gt=3)

# 查询1980年发表的图书

# BookInfo.objects.filter(pub_date__year=1980)

# 查询1990年1月1日后发表的图书

# BookInfo.objects.filter(pub_date__gt='1990-1-1')

# BookInfo.objects.filter(readcount__gt=F('commentcount'))

# 例：查询阅读量大于2倍评论量的图书。
# 例：查询阅读量大于等于评论量的图书。
# BookInfo.objects.filter(readcount__gle=F('commentcount'))

# 例：查询阅读量大于20，并且编号小于3的图书。

# BookInfo.objects.filter(Q(readcount__gt=20)|Q(id__lt=3))

# 例：查询阅读量大于20的图书，改写为Q对象如下。

# BookInfo.objects.filter(Q(readcount__gt=20))

# 例：查询阅读量大于20，或编号小于3的图书，只能使用Q对象实现

# BookInfo.objects.filter(Q(readcount__gt=20)|Q(id__lt=3))

# 例：查询编号不等于3的图书。

# BookInfo.objects.exclude(id=3)
# BookInfo.objects.filter((~Q(id=3)))

# 例：查询图书的总阅读量。
# BookInfo.objects.aggregate(Sum('readcount'))

# 例：查询图书总数。
# BookInfo.objects.all().order_by('readcount')

# book = BookInfo.objects.get(id=1)
# book.peopleinfo_set.all()
#
# person = PeopleInfo.objects.get(name='郭靖')
# person.book
#
# person = PeopleInfo.objects.get(id=1)
# person.book_id
#
# BookInfo.objects.filter(peopleinfo__description__contains='八')
# PeopleInfo.objects.filter(book__name='天龙八部')
# BookInfo.objects.filter(readcount__gt=30).order_by('pub_date')