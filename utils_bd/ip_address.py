from config import supabase


class IpAddressService:
    @staticmethod
    def register_ip(data):
        response = supabase.table("ipaddress").insert(data).execute()
        return response.data
    
    @staticmethod
    def get_all_ip():
        response = supabase.table("ipaddress").select("*").execute()
        return response.data
    
    @staticmethod
    def validate_ip_address(ipaddress):
        response = supabase.table("ipaddress").select("*").eq("ip_address", ipaddress).execute()
        #print(response.data)
        return response.data