import os
from datetime import timedelta
import secrets

class Config:
    # Security
    #SECRET_KEY = secrets.token_hex(16)
    SECRET_KEY = os.environ.get('SECRET_KEY') # or #'dev-secret-key-change-in-production'

    # Database
    DATABASE_PATH = os.path.join('database', 'ats_system.db')

    # File Upload
    UPLOAD_FOLDER = 'uploads'
    MAX_CONTENT_LENGTH = 100 * 1024 * 1024  # 100MB max file size
    ALLOWED_EXTENSIONS = {'pdf', 'docx'}

    # Session
    PERMANENT_SESSION_LIFETIME = timedelta(hours=2)

    # Application
    DEBUG = True
    HOST = '0.0.0.0'
    PORT = 5000

    # Resume Processing
    MAX_FILES_PER_BATCH = 10
    TEXT_PREVIEW_LENGTH = 500

    # Legal Firm Classifications (Tier 1/2 firms for preference scoring)
    TIER_1_FIRMS = [
        'Khaitan & Co', 'AZB Partners', 'Cyril Amarchand Mangaldas',
        'JSA Advocates and Solicitors', 'Trilegal', 'Shardul Amarchand Mangaldas',
        'Economic Laws Practice', 'IndusLaw', 'Luthra and Luthra'
    ]
    TIER_2_FIRMS = [
        'DSK Legal', 'Majmudar & Partners', 'Phoenix Legal', 'Sudhir Namdeo',
        'Abhishek Manu Singhvi & Co', 'Wadia Ghandy & Co', 'Crawford Bayley & Co',
        'Link Legal', 'Anand and Anand', 'Remfry & Sagar'
    ]

    @staticmethod
    def get_tier_firms():
        return Config.TIER_1_FIRMS + Config.TIER_2_FIRMS

