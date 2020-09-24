from django.shortcuts import render
from django.http import HttpResponse
from book.models import BookInfo,PeopleInfo
from django.db.models import F,Q,Sum

# Create your views here.
def index(request):

    return HttpResponse('ok')

def shop(request,city_id,shop_id):
    Query_dict = request.GET
    print(Query_dict)
    order = Query_dict.get('order')
    print(city_id,shop_id)
    return HttpResponse(f'欢迎来到胡灿的小店：city_id:{city_id},shop_id:{shop_id}')


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