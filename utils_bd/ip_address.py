from config import supabase


class IpAddressService:
    @staticmethod
    def register_ip(data):
        print(f"Data IP REGISTER (before insert): {data}")
        response = supabase.table("ipaddress").insert(data).execute()
        print(f"Response from Supabase: {response.data}")
        return response.data
    
    @staticmethod
    def get_all_ip():
        response = supabase.table("ipaddress").select("*").execute()
        return response.data
    
    @staticmethod
    def validate_ip_address(ipaddress, unique_id):
        response = supabase.table("ipaddress").select("*").eq("ip_address", ipaddress).eq("unique_id", unique_id).execute()
        print(f"Validating IP address: {ipaddress} and unique_id: {unique_id}")
        print(f"Response from database: {response.data}")
        return response.data
    
    # -------- UNIQUE ID SECTION --------
    





    
    @staticmethod
    def register_unique_id(data):
        print(f"Data REGISTER (before insert): {data}")
        response = supabase.table("ipaddress").insert(data).execute()
        print(f"Response from Supabase: {response.data}")
        return response.data

    @staticmethod
    def validate_unique_id(unique_id):
        response = supabase.table("ipaddress").select("*").eq("unique_id", unique_id).execute()
        print(f"Validating unique_id: {unique_id}")
        print(f"Response from database: {response.data}")
        return response.data
    














    #---------------------------
    @staticmethod
    def register_user_ip_data(data):
        response = supabase.table("ipaddress").insert(data).execute()
        print(f"Data REGISTER (before insert): {data}")
        print(f"Response from Supabase: {response.data}")
        return response.data

    @staticmethod
    def validate_user_ip_data(unique_id, user_agent):
        response = supabase.table("ipaddress").select("*").eq("unique_id", unique_id).eq("user_agent", user_agent).execute()
        print(f"Validating unique_id: {unique_id} and user_agent: {user_agent}")
        print(f"Response from database: {response.data}")
        return response.data
    













