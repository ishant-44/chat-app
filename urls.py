from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# Redirect the root URL to /chat/
def home(request):
    return redirect('chat:chat_home')  # Replace with your chat home view name

urlpatterns = [
    path('', home),  # Root URL will redirect to chat page
    path('admin/', admin.site.urls),
    path('accounts/', include('account1.urls')),  # Assuming this is your accounts app
    path('chat/', include('chat.urls')),  # Chat app URLs
]
