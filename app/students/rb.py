class RBStudent:
    def __init__(self, student_id: int | None = None,
                 course: int | None = None,
                 major_id: int | None = None,
                 enrollment_year: int | None = None):
        self.id = student_id
        self.course = course
        self.major_id = major_id
        self.enrollment_year = enrollment_year

    def to_dict(self) -> dict:
        data = {'id': self.id, 'course': self.course, 'major_id': self.major_id,
                'enrollment_year': self.enrollment_year}
        # Создаем копию словаря, чтобы избежать изменения словаря во время итерации
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data
    