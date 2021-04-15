from django import forms
from .models import Topic, Post

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'What is in your mind?'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    subject = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 1,'placeholder': 'What is your subject?'}
        ),
        max_length=255,
        help_text='The max length of the text is 255'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']

class PostForm(forms.ModelForm):
    message = forms.CharField(
        widget= forms.Textarea(
            attrs={'rows':5, 'placeholder': 'Type your message here'}
        ),
        max_length=4000,
        help_text= 'The max length of the text is 4000',
    )

    class Meta:
        model = Post
        fields = ['message', ]