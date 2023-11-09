from django.urls import include, path

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('task/', include('tasks.urls')),
    path('directories/', include('directories.urls')),

]