from pydantic import BaseModel, ConfigDict, Field


class MajorAdd(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    major_name: str =  Field(..., description = "Имя факультета")
    major_description: str =  Field(None, description = "Описание факультета")
    count_students: int =  Field(0, description = "Количество студентов")


class MajorUpdateDescr(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    major_name: str =  Field(..., description = "Имя факультета")
    major_description: str =  Field(None, description = "Описание факультета")
