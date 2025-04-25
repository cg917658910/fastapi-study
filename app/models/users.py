from sqlmodel import SQLModel,Field

class UserBase(SQLModel):
    username: str = Field(unique=True, index=True,max_length=255)
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)
    email: str | None = Field(default=None, index=True, max_length=255)

class UserCreate(UserBase):
    password: str = Field(min_length=10, max_length=50)
    
class UserPublic(UserBase):
    id: int

class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str
    
    