from uuid import UUID

from sqlmodel import SQLModel, Field


class CategoryBase(SQLModel):
    name: str
    icon: str


class Category(CategoryBase, table=True):
    id: UUID = Field(default=None, nullable=False, primary_key=True)


class CategoryCreate(CategoryBase):
    pass


class TutorialBase(SQLModel):
    title: str
    path: str


class Tutorial(TutorialBase, table=True):
    id: UUID = Field(default=None, nullable=False, primary_key=True)


class TutorialCreate(TutorialBase):
    pass
