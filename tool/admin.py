from django.contrib import admin
from tool.models import User, Doctor,MachineLearningModel,SensorData
admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(MachineLearningModel)
admin.site.register(SensorData)
