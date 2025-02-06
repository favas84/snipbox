from django.urls import path, include

urlpatterns = [
    path('v1/', include(('users.api.v1.urls', 'users'),
                         namespace='users-api-v1')),
]
