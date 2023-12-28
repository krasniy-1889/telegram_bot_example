from pydantic import BaseModel


class UserBaseDTO(BaseModel):
    pass


class UserAddDTO(UserBaseDTO):
    telegram_id: int
    username: str
    first_name: str
    last_name: str
    is_bot: bool


class UserReadDTO(UserBaseDTO):
    id: int
    telegram_id: int
    username: str
    first_name: str
    last_name: str
    is_bot: bool
