from django import forms
from .models import Course
from ckeditor.widgets import CKEditorWidget

class CourseForm(forms.ModelForm):
    class Meta:

        model = Course
        fields = ['title', 'content']
        widgets = {
            'content': CKEditorWidget(attrs={'class': 'ckeditor'}),
        }

        def __init__(self, *args, **kwargs):
           super().__init__(*args, **kwargs)
           self.fields['content'].required = False

        


        
    
        


              