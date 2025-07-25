import sqlite3
import json
from datetime import datetime
from flask import Flask, request, jsonify, render_template_string

# Create Flask app
app = Flask(__name__)

# Database setup
def init_db():
    """Initialize SQLite database"""
    conn = sqlite3.connect('jobs.db')
    cursor = conn.cursor()
    
    # Create jobs table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            position TEXT NOT NULL,
            status TEXT NOT NULL,
            date TEXT NOT NULL,
            salary TEXT,
            location TEXT,
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

# Helper function to get database connection
def get_db_connection():
    conn = sqlite3.connect('jobs.db')
    conn.row_factory = sqlite3.Row  # This makes rows behave like dictionaries
    return conn

# Routes
@app.route('/')
def home():
    """Serve the main HTML page"""
    with open('simple_job_tracker.html', 'r') as f:
        html_content = f.read()
    return html_content

# API Routes
@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    """Get all jobs"""
    conn = get_db_connection()
    jobs = conn.execute('SELECT * FROM jobs ORDER BY created_at DESC').fetchall()
    conn.close()
    
    # Convert to list of dictionaries
    jobs_list = []
    for job in jobs:
        jobs_list.append({
            'id': job['id'],
            'company': job['company'],
            'position': job['position'],
            'status': job['status'],
            'date': job['date'],
            'salary': job['salary'],
            'location': job['location'],
            'notes': job['notes'],
            'created_at': job['created_at']
        })
    
    return jsonify(jobs_list)

@app.route('/api/jobs', methods=['POST'])
def add_job():
    """Add a new job"""
    data = request.get_json()
    
    # Validate required fields
    if not data or not data.get('company') or not data.get('position'):
        return jsonify({'error': 'Company and position are required'}), 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO jobs (company, position, status, date, salary, location, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        data['company'],
        data['position'],
        data['status'],
        data['date'],
        data.get('salary', ''),
        data.get('location', ''),
        data.get('notes', '')
    ))
    
    job_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return jsonify({'id': job_id, 'message': 'Job added successfully'}), 201

@app.route('/api/jobs/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    """Delete a job"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM jobs WHERE id = ?', (job_id,))
    
    if cursor.rowcount == 0:
        conn.close()
        return jsonify({'error': 'Job not found'}), 404
    
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Job deleted successfully'})

@app.route('/api/jobs/<int:job_id>', methods=['PUT'])
def update_job(job_id):
    """Update a job"""
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE jobs 
        SET company=?, position=?, status=?, date=?, salary=?, location=?, notes=?
        WHERE id=?
    ''', (
        data['company'],
        data['position'],
        data['status'],
        data['date'],
        data.get('salary', ''),
        data.get('location', ''),
        data.get('notes', ''),
        job_id
    ))
    
    if cursor.rowcount == 0:
        conn.close()
        return jsonify({'error': 'Job not found'}), 404
    
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Job updated successfully'})

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get job statistics"""
    conn = get_db_connection()
    
    total = conn.execute('SELECT COUNT(*) FROM jobs').fetchone()[0]
    applied = conn.execute('SELECT COUNT(*) FROM jobs WHERE status = "applied"').fetchone()[0]
    interview = conn.execute('SELECT COUNT(*) FROM jobs WHERE status = "interview"').fetchone()[0]
    offer = conn.execute('SELECT COUNT(*) FROM jobs WHERE status = "offer"').fetchone()[0]
    rejected = conn.execute('SELECT COUNT(*) FROM jobs WHERE status = "rejected"').fetchone()[0]
    
    conn.close()
    
    return jsonify({
        'total': total,
        'applied': applied,
        'interview': interview,
        'offer': offer,
        'rejected': rejected
    })

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Initialize database
    init_db()
    
    # Run the app
    app.run(host='0.0.0.0', port=5000, debug=True)