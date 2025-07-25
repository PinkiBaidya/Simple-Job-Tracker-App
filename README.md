# Simple Job Tracker Project

A beginner-friendly job tracker application using basic web technologies.

## 🚀 What's Included

This project provides **two versions** of a job tracking application:

### Version 1: Basic HTML with Local Storage
- **File**: `simple_job_tracker.html`
- **Technologies**: HTML, CSS, JavaScript
- **Storage**: Browser localStorage (no server needed)
- **Features**: Add jobs, delete jobs, search, statistics

### Version 2: Full Stack with REST API
- **Files**: `simple_app.py` + `job_tracker_with_api.html`
- **Technologies**: HTML, CSS, JavaScript, Python Flask, SQLite
- **Storage**: SQLite database
- **Features**: Full CRUD operations, REST API, persistent storage

## 🎯 Features

- ✅ Add job applications with company, position, status, date, salary, location, notes
- ✅ Delete job applications
- ✅ Search by company or position
- ✅ Filter by status (Applied, Interview, Offer, Rejected)
- ✅ View statistics (total applications, by status)
- ✅ Responsive design for mobile and desktop
- ✅ Clean, simple interface

## 🛠️ How to Use

### Option 1: Simple Version (No Server)
1. Open `simple_job_tracker.html` in your web browser
2. Start adding your job applications!
3. Data is saved in your browser's local storage

### Option 2: Full Stack Version (With Server)
1. Install Python and Flask:
   ```bash
   pip install flask
   ```

2. Run the server:
   ```bash
   python simple_app.py
   ```

3. Open your browser and go to: `http://localhost:5000`

## 📊 REST API Endpoints

If you're using the full stack version, here are the API endpoints:

- `GET /api/jobs` - Get all jobs
- `POST /api/jobs` - Add a new job
- `DELETE /api/jobs/{id}` - Delete a job
- `PUT /api/jobs/{id}` - Update a job
- `GET /api/stats` - Get statistics

## 📱 How It Works

### The Simple Version
- Uses **localStorage** to save data in your browser
- When you add a job, it's saved locally
- When you refresh the page, your data is still there
- No internet connection needed after first load

### The Full Stack Version
- Uses **SQLite database** to store data permanently
- **Flask** server handles all the backend logic
- **REST API** allows the frontend to communicate with the backend
- Data persists even if you close the browser

## 🎨 Customization

### Change Colors
Edit the CSS section in the HTML file:
```css
.stat-card {
    background: #3498db; /* Change this color */
}
```

### Add New Status Options
In the JavaScript section, find the status options and add your own:
```html
<option value="phone-screen">Phone Screen</option>
<option value="technical-interview">Technical Interview</option>
```

### Add New Fields
1. Add the input field in the HTML form
2. Update the JavaScript to handle the new field
3. For the full stack version, update the database schema

## 🔧 Technical Details

### Frontend Technologies
- **HTML5**: Structure and semantic markup
- **CSS3**: Styling with flexbox and grid
- **JavaScript**: DOM manipulation and API calls
- **Responsive Design**: Works on all screen sizes

### Backend Technologies (Full Stack Version)
- **Python**: Programming language
- **Flask**: Web framework
- **SQLite**: Database
- **REST API**: Communication between frontend and backend

## 📝 Code Structure

```
simple_job_tracker.html     # Basic version with localStorage
simple_app.py              # Flask server with REST API
job_tracker_with_api.html   # Frontend that uses the API
jobs.db                    # SQLite database (created automatically)
README.md                  # This file
```

## 💡 Learning Opportunities

This project is perfect for beginners to learn:
- How HTML, CSS, and JavaScript work together
- How to store data locally vs in a database
- How REST APIs work
- How frontend and backend communicate
- Basic database operations (CRUD)

## 🐛 Troubleshooting

### "Jobs not loading" in API version
- Make sure the Flask server is running
- Check the browser console for errors
- Ensure you're accessing `localhost:5000`

### "Data disappeared" in simple version
- This happens if you clear browser data
- Use the API version for permanent storage

### Flask server won't start
- Make sure Python is installed
- Install Flask: `pip install flask`
- Check if port 5000 is available

## 🚀 Next Steps

Once you're comfortable with this project, you can:
1. Add user authentication
2. Add job application reminders
3. Export data to CSV/PDF
4. Add charts and graphs
5. Deploy to a cloud platform

## 📚 Resources for Learning

- [HTML/CSS/JS Tutorial](https://www.w3schools.com/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLite Tutorial](https://www.sqlitetutorial.net/)
- [REST API Best Practices](https://restfulapi.net/)

Happy job hunting! 🎯