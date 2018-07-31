from .models import student_feedback
from rest_framework import serializers

class student_feedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = student_feedback
        fields = '__all__'
        #('rating', 'comment')
