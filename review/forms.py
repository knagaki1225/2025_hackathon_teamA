from django import forms

class searchForm(forms.Form):
    words = forms.CharField(
        label=' ',
        max_length=30,
        widget=forms.TextInput(attrs={
            'class':'words',
            'placeholder':'words',
        })
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
            ('1m_ago', '～１ヶ月'),
            ('2m_ago', '～２か月'),
            ('3m_ago', '～３ヶ月'),
            ('5m_ago', '～５ヶ月'),
            ('1y_ago', '～１年'),
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