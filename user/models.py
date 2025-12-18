from django.db import models
from agent.models import CustomUser

# Create your models here.

class NewRequest(models.Model):
    REQUEST_CHOICES = [
        ('requirements', 'Requirements'),
        ('problems', 'Problems'),
        ('issues', 'Issues'),
        ('complaint', 'Complaint'),
        ('service_request', 'Service Request'),
        ('inquiry', 'Inquiry'),
    ]

    STATUS_CHOICES = [
        ('waiting', 'Waiting'),
        ('assigned', 'Assigned'),
        ('resolved', 'Resolved'),
    ]

    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    request_type = models.CharField(max_length=20, choices=REQUEST_CHOICES)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='waiting')

    def __str__(self):
        return self.title
    
    assigned_agent = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_agent')

    def assign_to_agent(self, agent):
        self.status = 'assigned'
        self.assigned_agent = agent
        self.save()
