# Django Views

### Set status code for render return

    ...
    return render(request, status=404)


### Use generic view directly within URLconf

    from django.conf.urls import url
    from django.views.generic import TemplateView
    
    
    urlpatterns = [
        url(r'^$', TemplateView.as_view(template_name='home.html')
    ]
    