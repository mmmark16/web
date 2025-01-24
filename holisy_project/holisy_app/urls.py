from django.urls import path, include
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
# schema_view = get_schema_view(
#    openapi.Info(
#       title="API",
#       default_version='v2',
#       description="Description",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="hardbeat34@gmail.com"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )

app_name = "holisy_app"

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/token/', obtain_auth_token, name='token'),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    # path('doc/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('doc/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('rooms/', RoomListView.as_view()),
    path('room/<int:pk>/', RoomDetailView.as_view()),
    path('room/create/', RoomCreateView.as_view()),
    path('room/update/<int:pk>/', RoomUpdateView.as_view()),
    path('room/delete/<int:pk>/', RoomDeleteView.as_view()),

    path('users/', UserListView.as_view()),
    path('employees/', EmployeeListView.as_view()),
    path('clients/', ClientListView.as_view()),
    path('user/<int:pk>/', UserDetailView.as_view()),
    path('user/create/', UserCreateView.as_view()),
    path('user/update/<int:pk>/', UserUpdateView.as_view()),
    path('user/delete/<int:pk>/', UserDeleteView.as_view()),


    path('services/', ServiceListView.as_view()),
    path('service/<int:pk>/', ServiceDetailView.as_view()),
    path('service/create/', ServiceCreateView.as_view()),
    path('service/update/<int:pk>/', ServiceUpdateView.as_view()),
    path('service/delete/<int:pk>/', ServiceDeleteView.as_view()),

    path('bookings/', BookingListView.as_view()),
    path('booking/<int:pk>/', BookingDetailView.as_view()),
    path('booking/create/', BookingCreateView.as_view()),
    path('booking/update/<int:pk>/', BookingUpdateView.as_view()),
    path('booking/delete/<int:pk>/', BookingDeleteView.as_view()),

    path('applications/', ApplicationListView.as_view()),
    path('application/<int:pk>/', ApplicationDetailView.as_view()),
    path('application/create/', ApplicationCreateView.as_view()),
    path('application/update/<int:pk>/', ApplicationUpdateView.as_view()),
    path('application/delete/<int:pk>/', ApplicationDeleteView.as_view()),
]
