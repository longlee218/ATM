from django.db import models
from Long.models import Branch, ATM, Bank


class Customer(models.Model):
    Sex = (
        ('M', 'Man'),
        ('W', 'Woman'),
        ('No', 'Unknown'),
    )
    type = (
        ('CMND', 'Chứng minh nhân dân'),
        ('TCC', 'Thẻ căn cước'),
        ('HC', 'Hộ chiếu'),
    )
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)
    customer_id = models.AutoField(primary_key=True, null=False, blank=False)
    id_type = models.CharField(max_length=4, choices=type)
    id_no = models.CharField(max_length=15, unique=True)
    full_name = models.CharField(max_length=32)
    birthday = models.DateField()
    gender = models.CharField(max_length=2, choices=Sex)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12, unique=True)
    email = models.EmailField(unique=True)


class Account(models.Model):
    choice = (
        ('1', 'Active'),
        ('2', 'Dormant'),
        ('0', 'Inactive'),
    )
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=False)
    account_no = models.CharField(max_length=15, primary_key=True)
    password = models.CharField(max_length=50)
    limit = models.BigIntegerField()
    balance = models.BigIntegerField()
    create_day = models.DateField()
    end_day = models.DateTimeField()
    status = models.CharField(max_length=1, choices=choice)


class Card(models.Model):
    type = (
        ('1', 'Thẻ tín dụng'),
        ('2', 'Thẻ ATM'),
        ('3', 'Thẻ ghi nợ'),
        ('4', 'Thẻ đảm bảo'),
        ('5', 'Thẻ Visa'),
    )
    choice = (
        ('1', 'Active'),
        ('0', 'Deactive'),
    )
    account_no = models.ForeignKey(Account, on_delete=models.CASCADE)
    card_no = models.CharField(primary_key=True, max_length=16)
    pin = models.CharField(max_length=6)
    create_date = models.DateField()
    end_date = models.DateField()
    card_type = models.CharField(max_length=1, choices=type)
    status = models.CharField(max_length=1, choices=choice)


class Transaction(models.Model):
    type = (
        ('RT', 'withdrawal'),
        ('CKC', 'internal transfer'),
        ('CKK', 'interbank transfer'),
    )
    choice = (
        ('1', 'success'),
        ('0', 'fail'),
    )
    transaction_id = models.AutoField(primary_key=True)
    transaction_type = models.CharField(max_length=3, choices=type)
    transaction_time = models.DateTimeField()
    balance = models.BigIntegerField()
    card_no = models.ForeignKey(Card, on_delete=models.CASCADE)
    atm_id = models.ForeignKey(ATM, on_delete=models.CASCADE)
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE)
    transaction_fee = models.IntegerField()
    status = models.CharField(max_length=1, choices=choice)
