from django import forms

class searchForm(forms.Form):
    words = forms.CharField(
        label=' ',
        max_length=30,
        widget=forms.TextInput(attrs={
            'class':'words',
            'placeholder':'words',
        }),
        required=False
    )

    review_num = forms.ChoiceField(
        label='総合評価',
        choices=[
            ('1', '★'),
            ('2', '★★'),
            ('3', '★★★'),
            ('4', '★★★★'),
            ('5', '★★★★★'),
        ],
        widget=forms.RadioSelect,
        required=False
    )
    
    result_date = forms.ChoiceField(
        label='投稿日',
        choices=[
            ('30', '～１ヶ月'),
            ('60', '～２か月'),
            ('90', '～３ヶ月'),
            ('150', '～５ヶ月'),
            ('365', '～１年'),
        ],
        widget=forms.RadioSelect,
        required=False
    )

    good = forms.MultipleChoiceField(
        label='いいね数が多い',
        choices=[('true', 'いいね数が多い')],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )