import os
import sys
import json
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent))

from app import create_app
from app.routes import analyze_resume_with_ai, get_latest_resume
from app.db import update_resume_analysis

def test_analysis():
    app = create_app()
    with app.app_context():
        db_path = app.config['DATABASE']
        email = 'phani@gmail.com'
        resume = get_latest_resume(db_path, email)
        
        if not resume:
            print("No resume found for", email)
            return

        api_key = app.config.get('OPEN_API_KEY')
        print(f"Using API Key: {api_key[:10]}...")
        
        analysis = analyze_resume_with_ai(resume['file_content'], api_key)
        print("Analysis result keys:", analysis.keys())
        print("ATS Score:", analysis.get('ats_score'))
        
        if 'error' in analysis:
            print("ERROR found in analysis:", analysis['error'])
        else:
            # Update DB
            update_resume_analysis(db_path, resume['id'], json.dumps(analysis), analysis.get('ats_score', 0))
            print("Database updated successfully for resume ID", resume['id'])

if __name__ == "__main__":
    test_analysis()
