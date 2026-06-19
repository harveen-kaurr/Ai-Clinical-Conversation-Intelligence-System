from database.supabase_client import supabase


class DatabaseService:

    @staticmethod
    def execute_query(query):
        try:
            response = query.execute()
            return response.data

        except Exception as e:
            print(f"Database Error: {e}")
            return None