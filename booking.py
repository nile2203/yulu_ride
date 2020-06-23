from rest_framework import serializers


class RMBookingDetails:
    def __init__(self, booking):
        self.booking = booking

    @staticmethod
    def create_booking(user, vehicle, pickup_location):
        if is_existing_booking(user):
            return None

        booking = BookingDetails.objects.create(user=user, vehicle=vehicle, pickup_location=pickup_location,
                                                status=BookingDetails.STATUS_CONFIRMED)

        return RMBookingDetails(booking=booking)


class BookingDetailsSerializer(serializers.ModelSerializer):
    @staticmethod
    def get_serialized(booking):
        return {}

    class Meta:
        model = BookingDetails
