from django import forms

class StudentFeedback(forms.Form):
    name= forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter Your name", 'class': 'input-bottom-border'})
    )
    email= forms.EmailField(
        widget=forms.TextInput(attrs={"placeholder": "Enter Your email", 'class': 'input-bottom-border'})
    )
    course= forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter Course name", 'class': 'input-bottom-border'})
    )
    institute= forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter your Insitute", 'class': 'input-bottom-border'})
    )
    subject=[
        ('Best',"Best"),
        ("Better", "Better"),
        ("Average", "Average"),
        ("Good", "Good"),
        ("Bad", "Bad")
    ]
    subject_rating= forms.ChoiceField(
        choices=subject,
        widget=forms.RadioSelect(attrs={'class': 'radio-style'}),
        label="Understanding Of Subject"
    )
    teacher=[
        ('Best',"Best"),
        ("Better", "Better"),
        ("Average", "Average"),
        ("Good", "Good"),
        ("Bad", "Bad")
    ]
    subject_teacher= forms.ChoiceField(
        choices=teacher,
        widget=forms.RadioSelect(attrs={'class': 'radio-style'}),
        label="Teacher Reading Style"
    )
    communication=[
        ('Best',"Best"),
        ("Better", "Better"),
        ("Average", "Average"),
        ("Good", "Good"),
        ("Bad", "Bad")
    ]
    teacher_communication= forms.ChoiceField(
        choices=communication,
        widget=forms.RadioSelect(attrs={'class': 'radio-style'}),
        label= "Teacher Communication"
    )
    doubt=[
        ('Best',"Best"),
        ("Better", "Better"),
        ("Average", "Average"),
        ("Good", "Good"),
        ("Bad", "Bad")
    ]
    teacher_doubt= forms.ChoiceField(
        choices=doubt,
        widget=forms.RadioSelect(attrs={'class': 'radio-style'}),
        label= "Clearing Your Doubt"
    )
    project= [
        ('0',"0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4 or more", "4 or more")
    ]
    project_complete= forms.ChoiceField(
        choices=project,
        widget=forms.RadioSelect(attrs={'class': 'radio-style'}),
        label= "How Many Project Have U Done In This Course"
    )
    message= forms.CharField(
        widget=forms.Textarea(attrs={'class':'text-msg'}), 
        label="Suggesstion"
    )

    def clean(self):
        print("Total VAlidation")
        total_data= super().clean()
        print('Name Validation')
        inputname= total_data['name']
        if len(inputname) < 5:
            raise forms.ValidationError("Name Should be 5 chars onwords")
        
        print('Email Validation')
        inputemail= total_data['email']
        if inputemail[-10:] != "@gmail.com":
            raise forms.ValidationError("Email extension should be '@gmail.com'")
        
        print("Course Validation")
        inputcourse= total_data['course']
        if 10> len(inputcourse) > 15:
            raise forms.ValidationError("Course should be 10 to 15")
        
        print("institute Validation")
        inputinstitute= total_data['institute']
        if inputinstitute != "NareshIT" :
            raise forms.ValidationError("Institute Must be NareshIT")
        
        print("Message Validation")
        inputmsg= total_data['message']
        if 10 > len(inputmsg) > 100:
            raise forms.ValidationError("Message should be 10 to 100 chars")