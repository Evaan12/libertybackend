from domain.models.academics import CurriculumPhilosophy, CurriculumPillar, Subject, GradeLevel

class AcademicsRepository:
    def get_philosophy(self):
        """
        Retrieves the first CurriculumPhilosophy object.
        """
        return CurriculumPhilosophy.objects.first()

    def get_all_pillars(self):
        """
        Retrieves all CurriculumPillar objects.
        """
        return CurriculumPillar.objects.all()

    def get_all_subjects(self):
        """
        Retrieves all Subject objects.
        """
        return Subject.objects.all()

    def get_all_grade_levels(self):
        """
        Retrieves all GradeLevel objects.
        """
        return GradeLevel.objects.order_by('id')