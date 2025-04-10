from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View

class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = [
            {
                "id": 1,
                "name": "Java",
                "subcategories": [
                    {"name": "Java基礎"},
                    {"name": "Java応用"},
                ]
            },
            {
                "id": 2,
                "name": "Python",
                "subcategories": [
                    {"name": "Python基礎"},
                    {"name": "Python応用"},
                ]
            }
        ]
        context['categories'] = categories
        return context

class SubcategoryDetailView(View):
    def get(self, request, subcategory_name):
        subcategory = {
            "name": subcategory_name,
            "description": f"{subcategory_name} の詳細です。",
        }
        return render(request, 'subcategory.html', {'subcategory': subcategory})