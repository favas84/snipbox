from django.urls import path, include

urlpatterns = [
    path('v1/', include(('snippets.api.v1.urls', 'snippets'),
                         namespace='snippet-api-v1')),
]