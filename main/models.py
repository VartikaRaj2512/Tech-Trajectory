from django.db import models
from sklearn.tree import DecisionTreeClassifier
import joblib


class LevelSelection(models.Model):

    # Constants for choices (0-6 corresponding to different levels)
    No_Knowledge = 0
    Beginner = 1
    Intermediate  = 2
    Proficient  = 3
    Advanced = 4
    Expert = 5
   

    # Choices for each field, mapping numbers to human-readable labels
    FIELD_CHOICES = [
        (No_Knowledge, 'No Knowledge'),
        (Beginner , 'Beginner'),
        (Intermediate , 'Intermediate'),
        (Proficient , 'Proficient'),
        (Advanced, 'Advanced'),
        (Expert, 'Expert'),
    ]

    # Fields representing different skill levels
    database_fundamentals = models.IntegerField(choices=FIELD_CHOICES,default=0)
    computer_architecture = models.IntegerField(choices=FIELD_CHOICES,default=0)
    distributed_computing_systems = models.IntegerField(choices=FIELD_CHOICES,default=0)
    cyber_security = models.IntegerField(choices=FIELD_CHOICES,default=0)
    networking = models.IntegerField(choices=FIELD_CHOICES,default=0)
    software_development = models.IntegerField(choices=FIELD_CHOICES, default=0)
    programming_skills = models.IntegerField(choices=FIELD_CHOICES, default=0)
    data_analyst = models.IntegerField(choices=FIELD_CHOICES, default=0)
    computer_forensics_fundamentals = models.IntegerField(choices=FIELD_CHOICES, default=0)
    technical_communication = models.IntegerField(choices=FIELD_CHOICES, default=0)
    ai_ml = models.IntegerField(choices=FIELD_CHOICES, default=0)
    software_engineering = models.IntegerField(choices=FIELD_CHOICES, default=0)
    business_analysis = models.IntegerField(choices=FIELD_CHOICES, default=0)
    communication_skills = models.IntegerField(choices=FIELD_CHOICES, default=0)
    data_science = models.IntegerField(choices=FIELD_CHOICES, default=0)
    troubleshooting_skills = models.IntegerField(choices=FIELD_CHOICES, default=0)
    graphics_designing = models.IntegerField(choices=FIELD_CHOICES, default=0)
    Role = models.CharField(max_length=100, blank=True)

    def save(self , *args , **kwargs):
        ml_model=joblib.load('ml_model/career_role_predictor.joblib')
        self.Role=ml_model.predict([[self.software_engineering,self.graphics_designing,self.troubleshooting_skills,self.data_science,self.business_analysis,self.database_fundamentals,self.computer_architecture,self.distributed_computing_systems,self.cyber_security,self.networking,self.software_development,self.programming_skills,self.data_analyst, self.communication_skills,self.technical_communication,self.computer_forensics_fundamentals,self.ai_ml]])
        return super().save(*args,*kwargs)
    def __str__(self):
        return f"Level Selection {self.id} - {self.Role}"
