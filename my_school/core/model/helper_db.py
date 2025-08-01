from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from core.config import setting


class HelperDb:
    def __init__(
        self,
        url: str,
        echo: bool,
        echo_pool: bool,
        pool_size: int,
        max_overflow: int,
    ):
        self.async_engine = create_async_engine(
            url=url,
            echo=echo,
            echo_pool=echo_pool,
            pool_size=pool_size,
            max_overflow=max_overflow,
        )
        self.fabric_session = async_sessionmaker(
            bind=self.async_engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    async def session_getter(self):
        async with self.fabric_session() as session:
            yield session
            await session.close()


db_helper = HelperDb(
    url=setting.db.url,
    echo=setting.db.echo,
    echo_pool=setting.db.echo_pool,
    pool_size=setting.db.pool_size,
    max_overflow=setting.db.max_overflow,
)
