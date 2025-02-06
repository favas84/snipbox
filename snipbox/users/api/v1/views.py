from rest_framework_simplejwt.views import TokenObtainPairView


class LoginView(TokenObtainPairView):
    """
    Custom Login API that returns JWT tokens along with user info.
    """

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.user

        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            response.data.update({
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                }
            })
        return response
