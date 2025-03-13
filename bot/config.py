"""
Configuration du bot Discord
Ce fichier contient toutes les clés API et identifiants nécessaires au fonctionnement du bot.
"""

# Discord Bot Token
DISCORD_TOKEN = "MTM0OTczNDM5OTc3MTY3MjcxNw.GVYZhS.Hjfn4qtt84c0eX5-CDv2z5-M65M4NEG2Y_v_AM"

# Shodan API Key for server scanning
SHODAN_API_KEY = "jFDeQ3YSxktFtYmmpZlh5iVqiIveRivJ"

# VirusTotal API Key for file and URL scanning
VIRUSTOTAL_API_KEY = "5aca43b33b094ee57ecdb33e0e913b238a1131953cac77f243dcf5defca462be"

# Discord Channel IDs
SECURITY_LOG_CHANNEL_ID = 1347560499625197670
ALERT_CHANNEL_ID = 1349760816601108543

# API Keys
IPINFO_API_KEY = "374447f9f9e094"

# Encryption key for message encryption (must be 64 hexadecimal characters for AES-256)
ENCRYPTION_KEY = "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"

# Rôles spéciaux
SPECIAL_ROLE_ID = 1347584071148109845
MEMBER_ROLE_ID = None  # À configurer via la commande !set_member_role
SCAMMER_ROLE_ID = None  # À configurer via la commande !set_scammer_role

# Canaux spéciaux
WELCOME_CHANNEL_ID = None  # À configurer si nécessaire

# Paramètres de sécurité
MAX_VERIFICATION_ATTEMPTS = 3 