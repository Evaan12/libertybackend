from domain.models.about import Mission, Vision, CoreValue, Milestone

class AboutRepository:
    def get_mission(self):
        """
        Safely retrieves the first Mission object.
        Returns the object or None if it does not exist.
        """
        try:
            # Using .first() is safer than .get() as it returns None if not found
            return Mission.objects.first()
        except Exception as e:
            # Log the error for debugging
            print(f"Error fetching mission: {e}")
            return None

    def get_vision(self):
        """
        Safely retrieves the first Vision object.
        Returns the object or None if it does not exist.
        """
        try:
            return Vision.objects.first()
        except Exception as e:
            print(f"Error fetching vision: {e}")
            return None

    def get_all_core_values(self):
        """
        Retrieves all CoreValue objects.
        Returns an empty queryset if none exist.
        """
        return CoreValue.objects.all()

    def get_all_milestones(self):
        """
        Retrieves all Milestone objects ordered by year.
        Returns an empty queryset if none exist.
        """
        return Milestone.objects.order_by('year')