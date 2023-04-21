from .models import Category,Page


def global_data(request):
    data = {
        'categoryData': Category.objects.all(),
        'pageData': Page.objects.all(),
    }
    return data
