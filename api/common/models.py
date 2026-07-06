from sqlmodel import SQLModel, Field

class CompanyCreate(SQLModel):
    name: str

class Company(CompanyCreate, table=True):
    id: int | None = Field(default=None, primary_key=True)
    __tablename__ = "companies"

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    __tablename__ = "users"
    username: str = Field(unique=True)
    hashed_password: str

class UserReturn(SQLModel):
    username: str

class UserCreate(SQLModel):
    username: str
    password: str