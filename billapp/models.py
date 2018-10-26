from django.db import models
from django.contrib.auth.models import User
# # Create your models here.
# class UserDetail(models.Model):
# 	user=models.OneToOneField(User, on_delete=models.CASCADE)
# 	user_name=models.CharField(max_length=100)
# 	phno=models.IntegerField(max_length=15)


class Bill(models.Model):
	# customer=models.ForeignKey(UserDetail, on_delete=models.CASCADE,null=True)
	user=models.ForeignKey(User, on_delete=models.CASCADE,default=0)
	name=models.CharField(max_length=100)
	amount=models.IntegerField(default=0)
	date=models.DateTimeField(auto_now_add=True)
	due_date=models.DateField()
	

	def __str__(self):
		return self.name

class Expense(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE,default=0)
	income=models.IntegerField(default=0)
	bill_1=models.IntegerField(default=0)
	bill_2=models.IntegerField(default=0)
	bill_3=models.IntegerField(default=0)

	


	def subtract(self):
		return self.income-(self.bill_1+self.bill_2+self.bill_3)	