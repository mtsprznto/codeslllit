from config import supabase


class UserService:
    @staticmethod
    def register_user(data):
        response = supabase.table("usuarios").insert(data).execute()
        return response.data
    
    @staticmethod
    def get_all_users():
        response = supabase.table("usuarios").select("*").execute()
        return response.data
    
    @staticmethod
    def validate_user_email(correo):
        response = supabase.table("usuarios").select("*").eq("correo", correo).execute()
        print(response.data)
        return response.data