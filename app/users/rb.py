class RBUser:
    def __init__(self, email: str | None = None,
                 is_user: bool | None = True,
                 is_student: bool | None = None,
                 is_teacher: bool | None = None,
                 is_admin: bool | None = None,
                 is_super_admin: bool | None = None
                 ):
        self.email = email
        self.is_user = is_user
        self.is_student = is_student
        self.is_teacher = is_teacher
        self.is_admin = is_admin
        self.is_super_admin = is_super_admin

    def to_dict(self) -> dict:
        data = {'email': self.email, 'is_user': self.is_user,
                'is_student': self.is_student, 'is_teacher': self.is_teacher,
                'is_admin': self.is_admin, 'is_super_admin': self.is_super_admin}
        # Создаем копию словаря, чтобы избежать изменения словаря во время итерации
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data
