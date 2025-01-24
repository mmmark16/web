from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.templatetags.rest_framework import data
from rest_framework.views import APIView
from .models import *


# --------------------------------------------------------------------------Room


class RoomSerializer(serializers.ModelSerializer):
    """Список комнат"""

    class Meta:
        model = Room
        fields = ("room_number", "beds_number", "day_cost")


class RoomDetailSerializer(serializers.ModelSerializer):
    """Комната"""

    class Meta:
        model = Room
        fields = "__all__"


class RoomCreateSerializer(serializers.ModelSerializer):
    """Действия с комнатой"""

    class Meta:
        model = Room
        fields = "__all__"

    def create(self, validated_data):
        room = Room(**validated_data)
        room.save()
        return room


# --------------------------------------------------------------------------User


class UserSerializer(serializers.ModelSerializer):
    """Список сотрудников"""

    class Meta:
        model = User
        fields = ("first_name", "last_name", "post")


class UserDetailSerializer(serializers.ModelSerializer):
    """Сотрудник"""


    class Meta:
        model = User
        fields = "__all__"


class UserCreateSerializer(serializers.ModelSerializer):
    """Действия с сотрудником"""

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        employee = User(**validated_data)
        employee.save()
        return employee


# --------------------------------------------------------------------------Service


class ServiceSerializer(serializers.ModelSerializer):
    """Список услуг"""

    class Meta:
        model = Service
        fields = ("name",)


class ServiceDetailSerializer(serializers.ModelSerializer):
    """Услуга"""

    class Meta:
        model = Service
        fields = "__all__"


class ServiceCreateSerializer(serializers.ModelSerializer):
    """Действия с услугой"""

    class Meta:
        model = Service
        fields = "__all__"

    def create(self, validated_data):
        service = Service(**validated_data)
        service.save()
        return service


# --------------------------------------------------------------------------Booking


class BookingSerializer(serializers.ModelSerializer):
    """Список броней"""

    class Meta:
        model = Booking
        fields = ("client_id", "room_number", "arrival_date", "departure_date")


class BookingDetailSerializer(serializers.ModelSerializer):
    """Бронь"""

    class Meta:
        model = Booking
        fields = "__all__"

    status = serializers.CharField(source='get_status_display')


class BookingCreateSerializer(serializers.ModelSerializer):
    """Действия с бронью"""

    class Meta:
        model = Booking
        fields = "__all__"

    def create(self, validated_data):
        booking = Booking(**validated_data)
        booking.save()
        return booking


# --------------------------------------------------------------------------Application


class ApplicationSerializer(serializers.ModelSerializer):
    """Список заявок"""

    class Meta:
        model = Application
        fields = ("name", "status")


class ApplicationDetailSerializer(serializers.ModelSerializer):
    """Заявка"""

    class Meta:
        model = Application
        fields = "__all__"

    status = serializers.CharField(source='get_status_display')


class ApplicationCreateSerializer(serializers.ModelSerializer):
    """Действия с заявкой"""

    class Meta:
        model = Application
        fields = "__all__"

    def create(self, validated_data):
        application = Application(**validated_data)
        application.save()
        return application
