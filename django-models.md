# Django Models

### Instruct a model to enforce uniqueness across multiple fields

    from django.db import models
    
    
    class Snowflake(models.Model):
        
        longest_width = models.TextField(default='')
        arm1_m = models.TextField(default='')
        arm2_m = models.TextField(default='')
        arm3_m = models.TextField(default='')
        arm4_m = models.TextField(default='')
        arm5_m = models.TextField(default='')
        arm6_m = models.TextField(default='')
        
        class Meta:
   
            unique_together = ('longest_width', 'arm1_m', 'arm2_m', 'arm3_m', 'arm4_m', 'arm5_m', 'arm6_m')
            
### Instruct a model to enforce uniqueness across several sets
        
    from django.db import models
    from app.models import Immortals
    
    
    class Highlander(models.Model):
    
        name = models.TextField(default='Connor', choices=('Connor',))
        remake_number = models.TextField(default='')
        immortals = models.ForeignKey(Immortals, default=None)
        
        class Meta:
        
            unique_together = (('name', 'immortals'), ('name', remake_number'))


### Specify field which objects should ordered by

    from django.db import models
    
    
    class Duck(models.Model):
    
        height = models.DecimalField(decimal_places=1, max_digits=4, default=0)
        
        class Meta:
        
            ordering = ['height']

### Create and use a custom ID field

The below example overrides the default integer id field with a UUID datatype. 

    import uuid
    from django.db import models
    
    
    class Item(models.Model):
        
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
         
 