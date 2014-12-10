from haystack.forms import FacetedSearchForm
from django import forms



class SearchForm(FacetedSearchForm):
    attrs = {"id": "search_field","class":"search_field form-control", "placeholder":"Enter Movie Title...", "font-size": "24px"}
    q = forms.CharField(required=False, label='Search', widget=forms.widgets.TextInput(attrs=attrs))
