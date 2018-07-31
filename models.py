from django.db import models

class student_feedback(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    student_id = models.IntegerField(null=False)
    username = models.CharField(max_length=40, default=0)
    course_id = models.IntegerField(null=False,default=0)
    course = models.CharField(max_length=40,default=0)
    datetime = models.DateTimeField(null = True, blank=True)
    rating = models.IntegerField(default=0)
    comment = models.CharField(max_length=200, blank=True)

    class Meta:
        db_table = 'classcast_student_feedback'

    def __str__(self):
        return u'%s-%s' % (str(self.student_id), str(self.course_id))
