from django.db import models


class Province(models.Model):
    province_id = models.CharField(primary_key=True, max_length=2)
    province_name = models.TextField()


class Bank(models.Model):
    bank_id = models.CharField(primary_key=True, max_length=8)
    bank_name = models.TextField()
    bank_headquarters = models.TextField()
    bank_phone_number = models.CharField(max_length=10)
    branches = models.ManyToManyField(Province, through="Branch")


class Branch(models.Model):
    province_id = models.ForeignKey(Province, on_delete=models.CASCADE)
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE)
    branch_id = models.CharField(max_length=5, primary_key=True)
    branch_name = models.CharField(max_length=100)
    branch_address = models.TextField()


class Employee(models.Model):
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=5, primary_key=True)
    full_name = models.CharField(max_length=50)
    username = models.CharField(max_length=32)
    emp_password = models.CharField(max_length=50)


class ATM(models.Model):
    choice = (
        ('1', 'Active'),
        ('0', 'Deactive'),
    )
    employee_id = models.OneToOneField(Employee, on_delete=models.CASCADE)
    atm_id = models.CharField(max_length=5, primary_key=True)
    address = models.TextField()
    atm_balance = models.BigIntegerField()
    status = models.CharField(max_length=1, choices=choice)


class HistoryMoney(models.Model):
    history_id = models.CharField(max_length=3, primary_key=True)
    atm_id = models.ForeignKey(ATM, on_delete=models.CASCADE)
    history_time = models.DateTimeField()
    money = models.BigIntegerField()

