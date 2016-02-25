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
    
    
    class Highlander(models.Model):
    
        name = 'Connor'
        remake_number = models.TextField(default='')
        immortals = models.ForeignKey(Immortals, default=None)
        
        class Meta
        
            unique_together = (('name', 'immortals'), ('name', remake_number'))
        