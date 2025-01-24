from rest_framework import generics, permissions, status
from django.shortcuts import render
from django.urls import *
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class Logout(APIView):

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


# --------------------------------------------------------------------------Room


class RoomListView(generics.ListAPIView):
    """Вывод списка комнат"""
    serializer_class = RoomDetailSerializer
    queryset = Room.objects.all()


class RoomDetailView(generics.RetrieveAPIView):
    """Просмотр комнаты"""
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer


class RoomCreateView(generics.CreateAPIView):
    """Добавление комнаты"""
    queryset = Room.objects.all()
    serializer_class = RoomCreateSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class RoomUpdateView(generics.RetrieveUpdateAPIView):
    """Редактирование комнаты"""
    queryset = Room.objects.all()
    serializer_class = RoomCreateSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class RoomDeleteView(generics.DestroyAPIView):
    """Удаление комнаты"""
    queryset = Room.objects.filter()
    serializer_class = RoomDetailSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


# --------------------------------------------------------------------------User


class EmployeeListView(generics.ListAPIView):
    """Вывод списка сотрудников"""
    serializer_class = UserDetailSerializer
    queryset = User.objects.filter(is_staff=True)


class ClientListView(generics.ListAPIView):
    """Вывод списка клиентов"""
    serializer_class = UserDetailSerializer
    queryset = User.objects.filter(is_staff=False)


class UserListView(generics.ListAPIView):
    """Вывод списка пользователей"""
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()


class UserDetailView(generics.RetrieveAPIView):
    """Просмотр сотрудника"""
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserCreateView(generics.CreateAPIView):
    """Добавление сотрудника"""
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class UserUpdateView(generics.RetrieveUpdateAPIView):
    """Редактирование сотрудника"""
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class UserDeleteView(generics.DestroyAPIView):
    """Удаление сотрудника"""
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


# --------------------------------------------------------------------------Service


class ServiceListView(generics.ListAPIView):
    """Вывод списка услуг"""
    serializer_class = ServiceDetailSerializer
    queryset = Service.objects.all()


class ServiceDetailView(generics.RetrieveAPIView):
    """Просмотр услуги"""
    queryset = Service.objects.all()
    serializer_class = ServiceDetailSerializer


class ServiceCreateView(generics.CreateAPIView):
    """Добавление услуги"""
    queryset = Service.objects.all()
    serializer_class = ServiceCreateSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class ServiceUpdateView(generics.RetrieveUpdateAPIView):
    """Редактирование услуги"""
    queryset = Service.objects.all()
    serializer_class = ServiceCreateSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class ServiceDeleteView(generics.DestroyAPIView):
    """Удаление услуги"""
    queryset = Service.objects.filter()
    serializer_class = ServiceDetailSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


# --------------------------------------------------------------------------Booking


class BookingListView(generics.ListAPIView):
    """Вывод списка броней"""
    serializer_class = BookingDetailSerializer
    queryset = Booking.objects.all()


class BookingDetailView(generics.RetrieveAPIView):
    """Просмотр брони"""
    queryset = Booking.objects.all()
    serializer_class = BookingDetailSerializer


class BookingCreateView(generics.CreateAPIView):
    """Добавление брони"""
    queryset = Booking.objects.all()
    serializer_class = BookingCreateSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class BookingUpdateView(generics.RetrieveUpdateAPIView):
    """Редактирование брони"""
    queryset = Booking.objects.all()
    serializer_class = BookingCreateSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class BookingDeleteView(generics.DestroyAPIView):
    """Удаление брони"""
    queryset = Booking.objects.filter()
    serializer_class = BookingDetailSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


# --------------------------------------------------------------------------Application


class ApplicationListView(generics.ListAPIView):
    """Вывод списка заявок"""
    serializer_class = ApplicationDetailSerializer
    queryset = Application.objects.all()


class ApplicationDetailView(generics.RetrieveAPIView):
    """Просмотр заявки"""
    queryset = Application.objects.all()
    serializer_class = ApplicationDetailSerializer


class ApplicationCreateView(generics.CreateAPIView):
    """Добавление заявки"""
    queryset = Application.objects.all()
    serializer_class = ApplicationCreateSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class ApplicationUpdateView(generics.RetrieveUpdateAPIView):
    """Редактирование заявки"""
    queryset = Application.objects.all()
    serializer_class = ApplicationCreateSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class ApplicationDeleteView(generics.DestroyAPIView):
    """Удаление заявки"""
    queryset = Application.objects.filter()
    serializer_class = ApplicationDetailSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly
