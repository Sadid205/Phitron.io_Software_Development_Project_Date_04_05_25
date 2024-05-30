from django.shortcuts import render,redirect
from . import forms  
# Create your views here.

def FormField(request):
    new_form = forms.ExampleForm()
    commentForm = forms.CommentForm()
    Form_widget_attribute = forms.Form_widget_attribute
    ()
    EmailForm = forms.EmailForm()
    BoolField = forms.BoolField()
    DatField = forms.DatField()
    DateWithField = forms.DateWithField()
    DateWithSelect = forms.DateWithSelect()
    Decimal = forms.Decimal()
    max = forms.max()
    labelWith = forms.LabelWith()
    initial = forms.InitialValue()
    initialBoolean = forms.InitialBoolean()
    initialDate = forms.InitialDate()
    multipleChoices = forms.MultipleChoice()
    radioSelect = forms.MultipleChoiceRadio()
    if request.method=='POST':
        geeksForm = forms.GeeksForm(request.POST)
        if geeksForm.is_valid():
            geeksForm.save()
            print(geeksForm.cleaned_data)
            return redirect('FormField')
    else:
        geeksForm = forms.GeeksForm()
    return render(request,'form.html',{'form':new_form,'commentForm':commentForm,'Form_widget_attribute':Form_widget_attribute,'EmailForm':EmailForm,'BoolField':BoolField,'DatField':DatField,'DateWithField':DateWithField,'DateWithSelect':DateWithSelect,'Decimal':Decimal,'max':max,'labelWith':labelWith,'initial':initial,'initialBool':initialBoolean,'initialDate':initialDate,'multipleChoices': multipleChoices,'radioSelect':radioSelect,'geeksForm':geeksForm})