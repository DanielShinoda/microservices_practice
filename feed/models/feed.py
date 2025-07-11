from sqlmodel import Field, SQLModel


class Feed(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    type: str = Field(index=True)
    amount: int = Field(default=0)
