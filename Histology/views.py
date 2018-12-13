from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Entrynew, boxDisplayView
from .forms import Entrymodel, Boxmodel, BoxDisplayForm
import re
from datetime import datetime
from datetime import date




def index(request):
    global mo1
    global datemo

    if request.method == 'POST':
        form = Entrymodel(request.POST)
        if form.is_valid():
            datemo = datetime.now()
            print(datemo)
            HTmsg = form.cleaned_data['starting_DIDSTR']
            HTNumRegex = re.compile(r'(\d\d\d\d\d\d\d\d\d)')
            mo1 = HTNumRegex.findall(HTmsg)
            print(mo1)
            
            article = form.save(commit=False)
            article.author = request.user
            article.first_name = request.user.first_name
            article.last_name = request.user.last_name
            article.starting_DID = mo1[0]
            box_article = boxDisplayView(author_box = request.user, DID_num = mo1[0])
            box_article.save()
            # article.save()
            return HttpResponseRedirect('box_started/' %mo1 )
            
            







    form = Entrymodel()
    if not request.user.is_anonymous:
        box_list = Entrynew.objects.filter(author = request.user).filter(date__gte = date.today())
    else:
        box_list = 0

       

    return render(request, 'login/index.html', { 'form':form, 'box_list':box_list})




def box_details(request, box_id):
    print(box_id)
    box =Entrynew.objects.filter(author = request.user).filter(date__gte = date.today())
    box1 =box.get(box_number = box_id)
    print(box1)

    return render(request, 'login/box_details.html', {'box1':box1})




def box_started(request):
    global mo1
    global datemo
    
    if request.method == 'POST':
        form = Boxmodel(request.POST)
        if form.is_valid():
            datemo1 = datetime.now()
            print(datemo1)
            print(datemo)
            datemo2 = datemo1 - datemo
            print(datemo2)
            msg = form.cleaned_data['message_field']
            print(msg.upper())
            NumRegex = re.compile(r'(\d\d|\d)')
            TypeRegex = re.compile(r'(TIQ|DDX|GI|BOOBS|STAT|BONE)')
            mo = NumRegex.findall(msg.upper())
            print(mo)

            mo2 = TypeRegex.search(msg.upper())
            
            
            
            article = form.save(commit=False)
            article.author = request.user
            article.first_name = request.user.first_name
            article.last_name = request.user.last_name
            article.box_number = mo[4]
            article.reqtotal_num = mo[3]
            article.starting_DID = mo1[0]
            article.duration = str(datemo2)
            article.ending_DID = int(mo1[0])+ int(mo[3])-1
            
            if mo2 == None:
                article.Box_type = "Normal"
            else:
                print(mo2.group())
                article.Box_type = str(mo2.group())

            
            article.save()
            return HttpResponseRedirect('/histo/')
            
            





    form1 = Boxmodel()
    form2 = BoxDisplayForm()

    return render(request, 'login/box_started.html', { 'form1':form1, 'form2':form2 } )
