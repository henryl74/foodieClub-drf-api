from rest_framework import permissions


# Help was taken from Code Institute's DRF API walkthrough project.
class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    Users can use the crud functionality if they are the owner,
    otherwise read only.
    '''

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
