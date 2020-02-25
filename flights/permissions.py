from rest_framework import permissions
from datetime import date , timedelta , datetime

class IsHoho(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.user == request.user  or request.user.is_staff :
            return True
        return False

class IsDodo(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        bb = obj.date- date.today()
        bbnd = bb.days
        if  bbnd >= 3 :
            return True
        return False
