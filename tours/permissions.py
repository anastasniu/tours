from rest_framework import permissions

<<<<<<< HEAD
=======

>>>>>>> c21bb4f
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.student.user == request.user