from django import forms

class EditMoreSubLeft(forms.Form):
    statuses = (('plan_to_watch','Plan to Watch'),('watching','Watching'),('completed','Completed'),('dropped','Dropped'),('on_hold','On Hold'))
    rating = (('10','10'),('9','9'),('8','8'),('7','7'),('6','6'),('5','5'),('4','4'),('3','3'),('2','2'),('1','1'),('0','-'))
    priority = (('2','Priority - 2'),('1',' Priority - 1'),('0','Priority - 0'))
    status = forms.ChoiceField(label=False, choices=statuses, widget=forms.Select(attrs={'class':'e-status'}))
    rating = forms.ChoiceField(label=False, choices=rating, widget=forms.Select(attrs={'class':'e-rating'}))
    priority = forms.ChoiceField(label=False, choices=priority, widget=forms.Select(attrs={'class':'e-prio'}))


class EditMoreSubRight(forms.Form):
    episodes = forms.IntegerField(label=False)
    rewatching = forms.BooleanField(label=False)
    rewatched = forms.IntegerField(label=False)