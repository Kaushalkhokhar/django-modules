from datetime import date, datetime, time
from django.shortcuts import render, HttpResponse
from .models import Students, Teachers
from django.db.models import Q, Avg, Sum, Min, Max, Count

def home(request):
    """
    Part 1: returns a new queryset
    """
    # students = Students.objects.all()
    # students = Students.objects.filter(marks__gte=34)
    # students = Students.objects.exclude(marks=34)

    # students = Students.objects.order_by('marks')
    # students = Students.objects.filter(marks__gte=34).order_by('marks')
    # students = Students.objects.filter(marks__gte=34).order_by('-marks')
    # students = Students.objects.filter(marks__gte=34).order_by('?') # will give random sequence

    # students = Students.objects.filter(marks__gte=22).order_by('marks').reverse()
    # students = Students.objects.filter(marks__gte=22).order_by('marks').reverse()[:3]

    # students = Students.objects.values() # values will give a dictionary object with key value pair
    # students = Students.objects.values('name', 'marks')
    
    # students = Students.objects.values_list()
    # students = Students.objects.values_list('name', 'marks')
    # students = Students.objects.values_list('name', 'marks', named=True) # gives name to row data
    
    # students = Students.objects.using('default').filter(marks__gt=20) # for using multiple database

    # students = Students.objects.dates('pass_date', 'month')
    # students = Students.objects.datetimes('pass_date', 'month')

    ################# Second Part ######################
    # qs1 = Students.objects.values_list('id', 'name')
    # qs2 = Teachers.objects.values_list('id', 'name')

    # students = qs2.union(qs1) 
    # students = qs2.union(qs1, all=True) 
    # without all - removes duplicates, with all=True - gives all the queris
    # union must have same column name like here. i.e id, name

    # students = qs1.intersection(qs2) 
    # here it gives the common data if exists in both the table otherwise empty list
    # here both the column like id and name should be same

    # students = qs1.difference(qs2) 

    ################# AND OR Operator ######################

    # students = Students.objects.filter(name='kush') & Students.objects.filter(marks=50)
    # students = Students.objects.filter(name='kush', marks=50)
    # students = Students.objects.filter(Q(name='kush') & Q(marks=50))
    # above both query will result in same data

    # students = Students.objects.filter(name='kush') | Students.objects.filter(id=1)
    # students = Students.objects.filter(Q(name='kush') | Q(id=1))
    # above both query will result in same data

    # print(f'Queryset: {students}')
    # print(f'Query: {students.query}')

    # for st in students:
        # print(st.id, st.name,  st.roll_no, st.marks, st.city)
        # print(st.get('id'), st.get('name'),  st.get('roll_no'), st.get('marks'), st.get('city')) # this is for values method
        # print(st) # this is for values_list


    """
    Part 2: does not returns a new queryset
    """
    # std = Students.objects.get(id=1)
    # here get only used to get one data, if we pass params shuch that is not unidue that it will give exceptions
    
    # std = Students.objects.first()
    # std = Students.objects.order_by('name').first()

    # std = Students.objects.last()
    # std = Students.objects.order_by('name').last()

    # std = Students.objects.latest('pass_date') # returns latest data
    # it requires a datatime column params as args

    # std = Students.objects.earliest('pass_date') # returns oldetst data
    # it requires a datatime column params as args

    # std = Students.objects.all().exists() # true if data exists else false
    # one_std = Students.objects.get(id=2)
    # std = Students.objects.filter(id=one_std.id).exists()

    # std = Students.objects.create(name='Ridham', roll_no=9, marks=26, city='Surat', pass_date=datetime.utcnow())
    # create method save automatically

    # std, created = Students.objects.get_or_create(name='Ridham', roll_no=9, marks=26, city='Surat')
    # here if new data is created then created will be true

    # no_of_rows_updated = Students.objects.filter(id=1).update(name='Kaushal', marks=49)
    # no_of_rows_updated = Students.objects.filter(marks__gt=35).update(city="Surat")
    # it returns the number of rows updated and only valid on quryset not on object

    # no_of_rows_deleted = Students.objects.filter(name="Ridham").delete() 
    # no_of_rows_deleted = Students.objects.get(id=5).delete() 
    # so it deletes the qeuryset as well as single object

    # counts = Students.objects.all().count()

    # print(counts)
    # return HttpResponse('This is home page')

    """
    Part 3: Field Lookups
    """
    # stds = Students.objects.filter(name__exact='kaushal') # case sensitive
    # stds = Students.objects.filter(name__iexact='kaushal') # case insensitive
    # stds = Students.objects.filter(name__contains='u') # case sensitive
    # stds = Students.objects.filter(name__icontains='u') # case insensitive
    # stds = Students.objects.filter(id__in=[1, 5, 7])
    # stds = Students.objects.filter(marks__gt=35) # greter than
    # stds = Students.objects.filter(marks__gte=34) # greter than equal
    # stds = Students.objects.filter(marks__lt=34) # greter than equal
    # stds = Students.objects.filter(marks__lte=34) # greter than equal
    # stds = Students.objects.filter(name__startswith='a') 
    # stds = Students.objects.filter(name__istartswith='a') 
    # stds = Students.objects.filter(name__endswith='a') 
    # stds = Students.objects.filter(name__iendswith='a') 
    
    # stds = Students.objects.filter(pass_date__range=('2021-04-01', '2021-08-15')) 
    # this works for datefield and datetimefield
    # stds = Students.objects.filter(pass_date__date=date(2021, 8, 16))
    # this is only for datetimefield
    # stds = Students.objects.filter(pass_date__date__gt=date(2021, 8, 1))
    # this is example of multiple lookup. we can do like this for others too
    
    # below methods works for datefield as well as datetimefield
    # stds = Students.objects.filter(pass_date__year=2020)
    # stds = Students.objects.filter(pass_date__year__gt=2020)
    # example of multiple lookups
    # stds = Students.objects.filter(pass_date__month=8)
    # stds = Students.objects.filter(pass_date__month__gt=8)
    # stds = Students.objects.filter(pass_date__day__gt=2)
    # stds = Students.objects.filter(pass_date__week=23) # 52 week per year
    # stds = Students.objects.filter(pass_date__week_day=1) # sunday=1, monday=2, ...saturday=7
    # stds = Students.objects.filter(pass_date__quarter=1) # qaurter 1 = jan, feb, mar; qauter 2 = april, may, jun; ....

    # below method only for datetimefield
    # stds = Students.objects.filter(pass_date__time__gt=time(6, 00)) # after 6 am
    # stds = Students.objects.filter(pass_date__hour__gt=5) # 0-23 
    # stds = Students.objects.filter(pass_date__minute__gt=26) # 0-59 
    # stds = Students.objects.filter(pass_date__second__gt=30) # 0-59 


    # print(f'Query Set: {stds}')
    # print(f'Query SQL: {stds.query}')
    
    # for std in stds:
    #     print(std.id, std.name)

    """
    part 4: Queryset Aggregration
    """

    # ans = Students.objects.all().aggregate(Avg('marks'))
    # ans = Students.objects.all().aggregate(Sum('marks'))
    # ans = Students.objects.all().aggregate(Min('marks'))
    # ans = Students.objects.all().aggregate(Max('marks'))
    # ans = Students.objects.all().aggregate(Count('marks'))

    # print(ans)

    """
    Part 5: Q objects
    """
    # stds = Students.objects.filter(Q(name='kush') & Q(marks=50))
    # stds = Students.objects.filter(Q(name='kush') | Q(marks=49))
    # stds = Students.objects.filter(~Q(name='kush'))


    # for std in stds:
    #     print(std)

    """
    Part 6: Limiting Queryset
    """
    # stds = Students.objects.all()[0:4]
    # stds = Students.objects.all()[2:4]
    stds = Students.objects.all()[2:4:2]


    for std in stds:
        print(std)


    return HttpResponse('This is home page')