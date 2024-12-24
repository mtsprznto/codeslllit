#models para recuperar la ip desde la base de datos supabase

class IpAddress:
    def __init__(self, ip):
        self.ip = ip
    
    def to_dict(self):
        return {
            "ip": self.ip
        }