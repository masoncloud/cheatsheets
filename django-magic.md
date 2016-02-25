# Django Magic

Here are some magical maneuvers for your displeasure. 

### Because URL definitions belong in the model, said no one ever

    [model.py]
    from django.db import models
    from django.core.urlresolvers import reverse
    
    
    class Foolery(models.Model)
    
        def get_absolute_url(self):
        
            return reverse('view_foolery', args=[self.id])
            
    
    [view.py]
    def new_foolery(request):
        
        foolery = Foolery.objects.create()
        
        return redirect(foolery)

    
    def view_foolery(request, foolery_id):
    
        foolery = Foolery.objects.get(id=foolery_id)
        
        return render(request, 'foolery.html', {'foolery': foolery})
        
       