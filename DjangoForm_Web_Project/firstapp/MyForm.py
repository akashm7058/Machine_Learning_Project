from django import forms

 
# creating a form
class InputForm(forms.Form):   #  form class must be inherited from 'Form' class
                                # 'form' is a key to your class 'InputForm'
 
    Student_Name = forms.CharField(max_length = 200)
    PRN_No= forms.IntegerField()
    Book_Issued =forms.CharField(max_length = 200)
    
    