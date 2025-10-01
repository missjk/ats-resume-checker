# ATS Resume Checker for M&A Intern Screening

A comprehensive Applicant Tracking System (ATS) built from scratch to automate resume screening for M&A (Mergers & Acquisitions) internship positions. This system uses rule-based parsing and criteria evaluation without relying on LLMs, ensuring consistent and explainable results.

## 🚀 Features

### Core Functionality
- **Bulk Resume Upload**: Process up to 10 PDF/DOCX files simultaneously
- **Automated Parsing**: Extract academic year, CGPA, coursework, and experience data
- **Multi-tier Classification**: Categorize candidates into M&A Team Matches, Shortlisted, and Others
- **Secure Authentication**: Login system with session management
- **Detailed Reporting**: Export results to CSV with comprehensive scoring breakdown

### Screening Criteria
- **Long-term Interns**: Academic year (3rd/4th/5th year), CGPA ≥7.5, Company Law + Contract Law courses
- **Short-term Interns**: Relaxed requirements (Academic year OR CGPA)  
- **Preference Scoring**: Additional points for moot court, tier firm experience, publications, etc.

### Technical Highlights
- **No LLM Dependency**: Pure rule-based extraction using regex patterns and keyword matching
- **Robust File Processing**: Handles various PDF/DOCX formats with error handling
- **Responsive UI**: Bootstrap-based interface with real-time validation
- **Scalable Architecture**: Modular design with separate parser and evaluator components

## 📋 Requirements

- Python 3.8+
- Flask 2.3.3
- PyPDF2 3.0.1
- python-docx 0.8.11
- Flask-Login 0.6.3
- spaCy 3.6.1 (optional, for enhanced NLP)

## ⚡ Quick Start

### 1. Installation
```bash
# Clone or extract the project files
cd ats-resume-checker

# Install required packages
pip install -r requirements.txt

# Optional: Install spaCy English model for better text processing
python -m spacy download en_core_web_sm
```

### 2. Run the Application
```bash
python app.py
```

The application will start at `http://localhost:5000`

### 3. Default Login Credentials
- **Username**: `admin`
- **Password**: `admin123`

### 4. Usage Workflow
1. **Login** with the provided credentials
2. **Upload Resumes** (up to 10 PDF/DOCX files)
3. **Select Course Type** (5-year or 3-year law program)
4. **Choose Focus** (Long-term or Short-term internship)
5. **View Results** with detailed categorization and scoring
6. **Export CSV** for further analysis

## 📁 Project Structure

```
ats-resume-checker/
├── app.py                  # Main Flask application
├── config.py              # Configuration settings
├── models.py               # Database models and authentication
├── resume_parser.py        # Core resume parsing logic
├── criteria_evaluator.py   # Evaluation and scoring engine
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── templates/             # HTML templates
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   ├── upload.html
│   ├── results.html
│   └── error.html
├── static/               # Static assets
│   ├── css/style.css
│   └── js/main.js
├── database/             # SQLite database (auto-created)
└── uploads/              # Temporary file storage (auto-created)
```

## 🎯 Screening Criteria Details

### Long-term Intern Requirements (ALL must be met)
1. **Academic Year**: 3rd/4th/5th year (5-year course) OR 2nd/3rd year (3-year course)
2. **Academic Performance**: CGPA ≥ 7.5/10, no backlogs
3. **Subject Knowledge**: Company Law coursework completion
4. **Contract Law**: Contract Law coursework completion

### Short-term Intern Requirements (Relaxed)
- Academic Year OR CGPA requirement (at least one must be met)
- Course requirements are not mandatory
- May be relaxed in exceptional circumstances

### Preference Scoring (Bonus Points)
- **Tier 1/2 Law Firm Experience**: +40 points
- **Moot Court Participation**: +50 points
- **M&A Specific Moots**: +30 points  
- **Legal Publications**: +30 points
- **Faculty Recommendations**: +20 points
- **Previous LegaLogic Internship**: +25 points

## 🔍 Technical Implementation

### Resume Parsing
- **PDF Extraction**: PyPDF2 with pdfplumber fallback
- **DOCX Processing**: python-docx for text and table extraction
- **Pattern Matching**: Regex patterns for CGPA, academic year, courses
- **Keyword Detection**: Fuzzy matching for legal terminology

### Criteria Evaluation
- **Rule-based Scoring**: Points system for each requirement
- **Multi-category Classification**: Long-term, short-term, and preference evaluation
- **Flexible Configuration**: Easy modification of criteria and scoring weights

### Security & Performance
- **Input Validation**: File type, size, and content validation
- **Secure File Handling**: Temporary storage with automatic cleanup
- **Session Management**: Flask-Login with secure password hashing
- **Error Handling**: Comprehensive error reporting and logging

## 📊 Result Categories

### 🌟 M&A Team Matches
Candidates who meet **ALL** long-term criteria:
- Academic year requirement ✓
- CGPA ≥ 7.5 ✓  
- Company Law coursework ✓
- Contract Law coursework ✓

### ⚠️ Shortlisted Candidates
Candidates who meet basic criteria:
- Academic year OR CGPA requirement
- May have some missing coursework

### 📋 Others
Candidates with insufficient criteria:
- Below minimum academic requirements
- Missing critical coursework
- Low preference scores

## 🛠️ Customization

### Modifying Criteria
Edit `criteria_evaluator.py` to adjust:
- Minimum CGPA requirements
- Academic year ranges
- Scoring weights
- Additional criteria

### Adding Keywords
Update `resume_parser.py` keyword lists:
- Company law terms
- Contract law variations  
- Legal research indicators
- Moot court competition names

### UI Customization
Modify templates and `static/css/style.css` for:
- Branding changes
- Color schemes
- Layout adjustments

## 🔒 Security Considerations

- Change default admin password in production
- Use environment variables for sensitive config
- Implement file upload size limits
- Add CSRF protection for forms
- Enable HTTPS in production deployment

## 🐛 Troubleshooting

### Common Issues
1. **PDF text extraction fails**: Install pdfplumber as fallback
2. **spaCy model missing**: Run `python -m spacy download en_core_web_sm`
3. **File upload errors**: Check file size limits and permissions
4. **Database issues**: Delete `database/` folder to reset

### Performance Optimization
- Adjust batch processing limits in `config.py`
- Optimize regex patterns for faster matching
- Implement caching for repeated operations
- Use production WSGI server (Gunicorn/uWSGI)

## 📈 Future Enhancements

- [ ] Add user management and role-based access
- [ ] Implement resume ranking algorithms
- [ ] Add email notification system
- [ ] Create detailed analytics dashboard
- [ ] Support for additional file formats
- [ ] Integration with HR systems
- [ ] Automated report generation

## 📞 Support

For technical support or feature requests, please refer to the system documentation or contact the development team.

---

**Built for M&A intern screening with precision, security, and scalability in mind.**
