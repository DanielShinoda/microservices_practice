from sqlmodel import Field, SQLModel


class Animals(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field()
    type: str = Field(index=True)
    feed_type: str = Field()
