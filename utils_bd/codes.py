from supabase import Client
from models.Code import Code
from config import supabase

class CodesService:
    
    @staticmethod
    def get_code():
        try:
            response = supabase.table('codes').select('*').limit(1).execute()
            if response.data:
                code_data = response.data[0]
                code = Code(code_data['code'])
                return code
            else:
                print("No data found")
        except Exception as e:
            print(f"Error fetching code: {e}")
        return None
    
    @staticmethod
    def delete_code(code):
        try:
            supabase.table('codes').delete().eq('code', code).execute()
        except Exception as e:
            print(f"Error deleting code: {e}")