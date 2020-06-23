from rest_framework.decorators import api_view
from rest_framework.response import Response

from seller_shop.ride.vehicle_details import RMVehicleLocation


@api_view(['POST'])
def api_book_ride(request):
    post_data = request.body
    user = request.user
    x_coordinate = post_data.get('x-coordinate')
    y_coordinate = post_data.get('y-coordinate')
    vehicle_type = post_data.get('type')
    if not (x_coordinate and y_coordinate):
        return Response(status=400)

    status, message, available_vehicles = RMVehicleLocation().get_available_vehicles(x_coordinate, y_coordinate)
    if status == 0:
        return Response(status=200)

    rm_booking = RMBookingDetails.create_booking(user, vehicle, pickup_location)
    if not rm_booking:
        return Response(status=200)

    serialized_booking = BookingDetailsSerializer.get_serialized(rm_booking.get_booking())
    return Response(serialized_booking, status=200)

