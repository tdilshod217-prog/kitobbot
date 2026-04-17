import asyncpg
from config import config
import os
class Database:
    def __init__(self):
        self.pool = None

    async def connect(self):
        # Ikkala ehtimolni ham tekshirish:
        dsn = os.getenv("DB_URL") or os.getenv("DATABASE_URL")
        
        if dsn:
            print("Ulanish DB_URL orqali amalga oshirilmoqda...")
            self.pool = await asyncpg.create_pool(dsn=dsn)
        else:
            # Agar DB_URL yo'q bo'lsa, Railway xostini configdan tekshiring
            print(f"DEBUG: Hostga ulanish: {config.DB_HOST}")
            self.pool = await asyncpg.create_pool(
                user=config.DB_USER,
                password=config.DB_PASSWORD,
                database=config.DB_NAME,
                host=config.DB_HOST,
                port=config.DB_PORT
            )

    async def add_user(self, telegram_id, username):
        query = """
        INSERT INTO users (username,telegram_id) 
        VALUES ($1, $2) 
        ON CONFLICT (telegram_id) DO NOTHING;
        """
        await self.pool.execute(query,telegram_id,username)

    async def get_user_role(self, telegram_id):
        query = "SELECT role FROM users WHERE telegram_id = $1;"
        return await self.pool.fetchval(query, telegram_id)

    async def set_user_role(self, telegram_id, role):
        query = "UPDATE users SET role = $1 WHERE telegram_id = $2;"
        await self.pool.execute(query, role, telegram_id)

    async def get_users(self):
        query = "SELECT telegram_id, username, role FROM users ORDER BY id DESC;"
        return await self.pool.fetch(query)
    
    async def get_user(self,telegram_id):
        query = "SELECT telegram_id, username, role FROM users where telegram_id=$1"
        return await self.pool.fetchrow(query,telegram_id)
    
#movie add
    async def add_movies(self,title,file_id,code):
        query="INSERT INTO movies (title,file_id,code) values ($1,$2,$3);"
        return await self.pool.execute(query,title,file_id,code)
    
#search movie
    async def search_movie(self,code:int):
        sql="""
        select id,title,file_id,code from movies WHERE code=$1;
        """
        return await self.pool.fetchrow(sql,code)
    
    async def get_bot_stats(self):
        users_count=await self.pool.fetchval("select count(*) from users")
        movie_count=await self.pool.fetchval("select count(*) from movies")
        return {
            "users": users_count,
            "movie": movie_count,
        }