from django.db import models

class EncodeQueueEntry(models.Model):
	id = models.CharField(max_length=10, primary_key=True, unique=True)
	original_filename = models.CharField(max_length=255, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	working_on = models.BooleanField(default=False)

	class Meta:
		ordering = ('created_at',)
