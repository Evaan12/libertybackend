from domain.models.facilities import Facility

class FacilitiesRepository:
    """
    Handles database operations for the Facility model.
    """
    def get_all_facilities(self):
        """
        Retrieves all facility objects, ordered by their ID.
        """
        return Facility.objects.order_by('id').all()