from django.shortcuts import render
import datetime

def home(request):
    return render(request,'project_home.html')


def Django_template(request):
    data = {'author':'rahim','list_of_name':[
            {'name': 'amy', 'age': 22},
            {'name': 'joe', 'age': 31},
            {'name': 'zed', 'age': 19},
        ],'str':'String with spaces','num_messages':2,'linenumbers':['cat','dog','horse'],
        'linenumber':"""cat
        dogs
        tiger""",'timesince':'2022-01-02T10:30:00.000123','escape':'<p>You are <em>pretty</em> smart!</p>','numbers':['one','two','three'],'list1': ['a','b','c'],'value':'123456789','project':'<h1>This is Project Home</h1>','states':['States', ['Kansas', ['Lawrence', 'Topeka'], 'Illinois']],'center':'my name is korim','defalult':'','name':"I'm Jai",'age':20,"lst":['python','is','best'],'birthday':datetime.datetime(year=1969, month=7, day=21,
        hour=2, minute=56, second=15,
        tzinfo=datetime.timezone.utc),'val' : '','courses':[
            {
                'id':1,
                'name':'Python',
                'fee': 5000
            },
            {
                'id':2,
                'name':'Django',
                'fee':10000
            },
            {
                'id':3,
                'name':'C',
                'fee':1000
            },
            {
                'id':4,
                'name':'D',
                'fee':100090
            },
            {
                'id':5,
                'name':'E',
                'fee':100430
            },
            {
                'id':6,
                'name':'F',
                'fee':4430
            },
        ]}
    return render(request,'django_template.html',data)