from config import supabase


class UserService:
    @staticmethod
    def register_user(data):
        #print(data)
        response = supabase.table("usuarios").insert(data).execute()
        
        return response.data
    
    @staticmethod
    def get_all_users():
        response = supabase.table("usuarios").select("*").execute()
        return response.data
    
    @staticmethod
    def validate_user_email(correo):
        response = supabase.table("usuarios").select("*").eq("correo", correo).execute()
        #print(response.data)
        return response.data
    
    @staticmethod
    def get_user_by_id(user_id):
        response = supabase.table("usuarios").select("*").eq("id", user_id).execute()
        if response.data:
            return response.data[0]
        else:
            return None