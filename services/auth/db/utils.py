from .conn import engine
from sqlalchemy import text
from .tables import Base

def test_conn():
    with engine.connect() as conn:
        conn.execute(text("SHOW TABLES"))

def create_table(table_name:str=None):
        if table_name:
            table = Base.metadata.tables.get(table_name)
            if table is not None:
                table.create(engine)
                print(f"Table '{table_name}' created.")
            else:
                print(f"Table '{table_name}' not found in metadata.")
        else:
            Base.metadata.create_all(engine)
            print("All tables created.")
            
def alter_table(updat_query:str):
    with engine.connect() as conn:
        try:
            try:
                conn.execute(text(updat_query))
                print("executed the query")
            except Exception as e:
                print(f"could not execute query")
            
            conn.commit()
            print("Database update completed.")
        except Exception as e:
            conn.rollback()
            print(f"An error occurred during update: {e}")
