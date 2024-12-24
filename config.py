import supabase
import streamlit as st
import os
from supabase import create_client, Client



@st.cache_resource
def init_supabase():
    url: str = st.secrets["supabase"]["URL_SUPABASE"]
    key: str = st.secrets["supabase"]["KEY_SUPABASE"]
    return supabase.create_client(url, key)

supabase = init_supabase()