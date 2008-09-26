from django.db import models
import datetime

class Application(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(max_length=400, blank=True)
    version = models.CharField(max_length=60, blank=True)

    def __unicode__(self):
        return self.name
    
# manager for the server model (returns all physical servers)
class PhysicalServerManager(models.Manager):
    def get_query_set(self):
        return super(PhysicalServerManager, self).get_query_set().filter(is_physical=True)

# manager for the server model (returns all guest servers)
class VirtualServerManager(models.Manager):
    def get_query_set(self):
        return super(VirtualServerManager, self).get_query_set().filter(is_physical=False)
    
class Server(models.Model):
    # required fields
    name = models.CharField(max_length=40)
    description = models.TextField(max_length=400, blank=True)
    is_physical = models.BooleanField(default=True)
            
    # optional fields
    cores = models.IntegerField(null=True, blank=True)
    memory = models.IntegerField(null=True, blank=True)
    storage = models.IntegerField(null=True, blank=True)
    applications = models.ManyToManyField(Application, related_name='servers', null=True, blank=True)
    host = models.ForeignKey('self', related_name='guest_set', null=True, blank=True)
    dop = models.DateField('date of purchase', null=True, blank=True)
    
    # metadata fields
    last_modified = models.DateTimeField('last modified', editable=False)
    
    # managers
    objects = models.Manager()
    physical_servers = PhysicalServerManager()
    virtual_servers = VirtualServerManager()
    
    def __unicode__(self):
        return self.name
    
    def save(self, force_insert=False, force_update=False):
        self.last_modified = datetime.datetime.now()
        super(Server, self).save(force_insert, force_update)
        
    @models.permalink
    def get_absolute_url(self):
        return ('server_detail', (), {
            'object_id': self.id})

