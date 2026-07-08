from supabase import Client, create_client
from dotenv import load_dotenv

from utils.secrets import get_secret

load_dotenv()

supabase_url = get_secret("SUPABASE_URL")
supabase_key = get_secret("SUPABASE_KEY")

if not supabase_url or not supabase_key:
    raise ValueError(
        "SUPABASE_URL and SUPABASE_KEY must be set via .env (local) "
        "or Streamlit secrets (deployment)."
    )

supabase: Client = create_client(
    supabase_url,
    supabase_key
)