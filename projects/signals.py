# from django.db.models.signals import post_save
# from .models import Projectmodel
# from django.dispatch import receiver
# from django.db import transaction


# def on_transaction_commit(func):
#     def inner(*args, **kwargs):
#         transaction.on_commit(lambda: func(*args, **kwargs))

#     return inner


# @receiver(post_save, sender=Projectmodel.Project)
# # @on_transaction_commit
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         instance.team.add(instance.creator)
#         print(instance.team.all())
#         print(instance.creator)
#         # instance.title = "yoboy"
#         # instance.save()
