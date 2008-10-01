from django.db import models
import datetime

class Application(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(max_length=400, blank=True)

    def __unicode__(self):
        return self.name
    
class ApplicationVersion(models.Model):
    application = models.ForeignKey(Application, related_name='versions')
    version = models.CharField(max_length=60)
    
    def __unicode__(self):
        display = ' '.join((self.application.name, self.version))
        return unicode(display)
    
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
    hostname = models.CharField(max_length=40)
    domain = models.CharField(max_length=40)
    description = models.TextField(max_length=400, blank=True)
    is_physical = models.BooleanField(default=True)
            
    # optional fields
    ip_addr = models.IPAddressField('IP Address', null=True, blank=True, default=None)
    mac_addr = models.CharField('MAC Address', max_length=20, null=True, blank=True)
    proc_speed = models.IntegerField('Processor speed (MHz)', null=True, blank=True)
    cores = models.IntegerField(null=True, blank=True)
    memory = models.IntegerField(null=True, blank=True)
    storage = models.IntegerField(null=True, blank=True)
    host = models.ForeignKey('self', related_name='guest_set', null=True, blank=True)
    dop = models.DateField('date of purchase', null=True, blank=True)
    applications = models.ManyToManyField(
        ApplicationVersion,
        related_name='servers_installed_on',
        null=True, blank=True
    )
    
    # metadata fields
    last_modified = models.DateTimeField('last modified', editable=False)
    
    # managers
    objects = models.Manager()
    physical_servers = PhysicalServerManager()
    virtual_servers = VirtualServerManager()
    
    def __unicode__(self):
        display = '.'.join((self.hostname, self.domain))
        return unicode(display)
    
    def save(self, force_insert=False, force_update=False):
        if self.ip_addr == '':
            self.ip_addr = None
        self.last_modified = datetime.datetime.now()
        super(Server, self).save(force_insert, force_update)
        
    def fqdn(self):
        "The fully qualified domain name of the server."
        return '.'.join((self.hostname, self.domain))
        
    @models.permalink
    def get_absolute_url(self):
        return ('server_detail', (), {
            'object_id': self.id})

