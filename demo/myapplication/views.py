# Name: bansri shah
# course: CST8333 Programming Language Research Project.
# final project
# student-number: 040920837
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import HttpResponse
from django.shortcuts import render
import csv
from .models import *
from collections import OrderedDict
from .fusioncharts import FusionCharts
print("bansri shah")
# Create your views here.
# Main page
# inheritance method
def data(request):
    class check_parent():
# parent method: getdisplay method
        def getDisplay(self):
            data1 = assign4.objects.get(id=1)
            return data1
#child method which use method from parent class
    class check_child(check_parent):

        def getDisplay(self):
            # get id=6 row from the databse
            data1 = assign4.objects.get(id=6)
            return data1
   #call sub class object
    s = check_child()

    # this function show return the home page with request happen

    return render(request, 'data.html', {'data': s.getDisplay()})
# function return home page
def show(request):

        return render(request, 'home.html')


#function reterive data from databse
def index(request):
    # open csv file and save it into the csv_data as list
    with open(r"Templates\13100262.csv") as csv_files:
        csv1 = csv.reader(csv_files, delimiter=',')
        csv_data = list(csv1)
    # loop through the entire csv file
    for c in csv_data:
        # call object of databse
        m = assign4()
        # give each row from csv file into the database particular field.
        m.REF_DATE = c[0]
        m.GEO = c[1]
        m.DGUID = c[2]
        m.Sex = c[3]
        m.Agegroup = c[4]
        m.Studentresponse = c[5]
        m.UOM = c[6]
        m.UOM_ID = c[7]
        m.SCALAR_FACTOR = c[8]
        m.SCALAR_ID = c[9]
        m.VECTOR = c[10]
        m.COORDINATE = c[11]
        m.VALUE = c[12]
        m.STATUS = c[13]
        m.SYMBOL = c[14]
        m.TERMINATED = c[15]
        m.DECIMALS = c[16]
        # call the save function to saving data in to the database.
        m.save()
        # call objects from model clss then call all function which reterive entire database
        data1 = assign4.objects.all()
        return render(request, 'show.html', {'data': data1})


# function to add data in the csv file
def add(request):
    # first it check if request is post method or not.
    if request.method != 'POST':
        # if it is not post method navigate to add .html page where we see the form of add page
        return render(request, 'add.html')
    else:
        # if it is post method then first get data from session which we store it firstly and store it into data

        # then each field fill by user will get using the request.post.get method and store it to object from the database.
        m = assign4()
        m.REF_DATE=request.POST.get('d')
        m.GEO =  request.POST.get('GEO')
        m.DGUID = request.POST.get('DGUID')
        m.Sex =  request.POST.get('SEX')
        m.Agegroup =  request.POST.get('AGEGROUP')
        m.Studentresponse =request.POST.get('STUDENT')
        m.UOM =request.POST.get('UOM')
        m.UOM_ID =request.POST.get('UOM_ID')
        m.SCALAR_FACTOR = request.POST.get('SCALAR')
        m.SCALAR_ID =  request.POST.get('S_ID')
        m.VECTOR = request.POST.get('VECTOR')
        m.COORDINATE =  request.POST.get('C')
        m.VALUE = request.POST.get('VALUE')
        m.STATUS =request.POST.get('STATUS')
        m.SYMBOL = request.POST.get('SYMBOL')
        m.TERMINATED = request.POST.get('TERMINATED')
        m.DECIMALS =   request.POST.get('DECIMAL')
       # call save function to save data
        m.save()



        data1 = assign4.objects.all()
        return render(request, 'show.html', {'data': data1})



# function use to reterive update page
def update(request):
    # if request is not post method then it goes to update page
    if request.method != 'POST':
        data = assign4.objects.all()
        return render(request, 'update.html', {'data': data})
# if request is post method or when you select on line for update it navigate through updated page
    else:
        return render(request, 'updated.html')


# function to update data in the csv file
def updated(request):
    # if request is not post method then it goes to update page
    if request.method != 'POST':
        data = assign4.objects.all()
        return render(request, 'update.html', {'data': data})

    else:
        # get id from html pagge on which you clicked.
        id = int(request.POST['id'])
        m = dict()
        m.REF_DATE = request.POST.get('d')
        m.GEO= request.POST.get('GEO')
        m.DGUID = request.POST.get('DGUID')
        m.Sex = request.POST.get('SEX')
        m.Agegroup = request.POST.get('AGEGROUP')
        m.Studentresponse = request.POST.get('STUDENT')
        m.UOM = request.POST.get('UOM')
        m.UOM_ID = request.POST.get('UOM_ID')
        m.SCALAR_FACTOR = request.POST.get('SCALAR')
        m.SCALAR_ID = request.POST.get('S_ID')
        m.VECTOR = request.POST.get('VECTOR')
        m.COORDINATE = request.POST.get('C')
        m.VALUE = request.POST.get('VALUE')
        m.STATUS = request.POST.get('STATUS')
        m.SYMBOL = request.POST.get('SYMBOL')
        m.TERMINATED = request.POST.get('TERMINATED')
        m.DECIMALS = request.POST.get('DECIMAL')
        # call update function from database
        assign4.objects.get(id=id).update(m)
        data1 = assign4.objects.all()
        return render(request, 'show.html', {'data': data1})



# function to delete data from the csv file
def delete(request):
    # if request is not post method then it goes to delete page
    if request.method != 'POST':
        data = assign4.objects.all()
        return render(request, 'delete.html', {'data': data})
 # if request is post method then first it get data from session and store it to data
    else:

        # first we get id of line which user want to delete

        # use delete function to delete particular row from  db
        id = request.POST.get('delete')
        # again we have to store value to session
        assign4.objects.get(id=id).delete()

    data = assign4.objects.all()
    # it return to show.html page with data
    return render(request, 'delete.html', {'data': data})

