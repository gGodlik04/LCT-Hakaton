from rest_framework import permissions


class ManagerPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        user = self.request.user

        if user.is_manager_user():
            return True
        return False


class EmployeePermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.type in ['GET', 'PATCH']:
            return True
        return False