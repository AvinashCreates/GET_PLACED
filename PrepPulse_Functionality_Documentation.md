# PrepPulse - Comprehensive Functionality and Working Documentation

## Overview

PrepPulse is an AI-powered placement preparation platform designed to help students enhance their campus placement readiness through intelligent tools and personalized guidance. The application integrates multiple features including AI chatbot assistance, resume analysis, mock test tracking, habit building, and comprehensive progress monitoring.

---

## Architecture and Technology Stack

### Backend Architecture
- **Framework**: Flask (Python web framework)
- **Database**: SQLite with relational schema
- **AI Integration**: OpenAI API (GPT-4o-mini for chat, TTS for speech synthesis)
- **Authentication**: Session-based with secure password hashing
- **Email Service**: SMTP integration for password reset functionality

### Frontend Architecture
- **Technology**: Vanilla JavaScript, HTML5, CSS3
- **UI Components**: Custom-built responsive components
- **Data Visualization**: Chart.js for progress tracking
- **File Handling**: PDF/DOCX resume upload and processing

### Database Schema
The application uses SQLite with 8 core tables:

1. **users** - User authentication and profile data
2. **first_login** - Tracks onboarding completion status
3. **onboarding_responses** - Stores initial self-assessment data
4. **skill_checklists** - JSON storage for technical skill assessments
5. **mock_tests** - Mock test records and performance tracking
6. **resumes** - Resume file metadata and AI analysis results
7. **habits** - Daily habit definitions and configurations
8. **habit_logs** - Daily habit completion tracking

---

## Core Functionality Analysis

### 1. Authentication System

#### User Registration and Login
- **Registration Flow**: Email validation, password confirmation, user creation
- **Login Process**: Email/password authentication with session management
- **Security Features**: 
  - Password hashing using Werkzeug's security functions
  - Session-based authentication
  - Admin shortcut (admin@gmail.com/admin) for administrative access

#### Password Reset System
- **Token-Based Reset**: Time-limited secure tokens using URLSafeTimedSerializer
- **Email Integration**: SMTP-based password reset emails
- **Security**: Token expiration (configurable, default 15 minutes)

#### Session Management
- **Session Storage**: Flask server-side sessions
- **Session Data**: User email, admin status, authentication state
- **Security**: Session invalidation on logout

### 2. AI-Powered Chatbot

#### Core Functionality
- **Model**: OpenAI GPT-4o-mini for conversational AI
- **Context Awareness**: Integrates user resume data and progress information
- **Response Format**: Concise, actionable placement preparation advice
- **Text-to-Speech**: Optional audio responses using OpenAI TTS

#### Technical Implementation
- **API Integration**: Direct OpenAI API calls with proper error handling
- **Context Building**: Dynamic context injection from user data
- **Response Processing**: Markdown rendering with DOMPurify sanitization
- **Audio Support**: Base64-encoded audio streaming for TTS responses

#### Chat Features
- **Real-time Messaging**: Asynchronous chat interface
- **Message History**: Persistent conversation display
- **Contextual Responses**: Resume-aware and progress-aware suggestions
- **Audio Playback**: Optional voice responses with player controls

### 3. Resume Analysis System

#### File Processing
- **Supported Formats**: PDF and DOCX files
- **Parsing Libraries**: PyPDF2 for PDF, python-docx for DOCX
- **File Storage**: Organized by user email in data/resumes directory
- **Security**: Filename sanitization and secure file handling

#### AI Analysis
- **ATS Scoring**: Automated ATS (Applicant Tracking System) compatibility scoring
- **Content Analysis**: Strengths, weaknesses, and improvement suggestions
- **Structured Output**: JSON-formatted analysis with actionable insights
- **Version Tracking**: Multiple resume versions with timestamp management

#### Analysis Features
- **Real-time Processing**: On-demand analysis with progress indicators
- **Detailed Feedback**: Section-wise resume evaluation
- **Improvement Suggestions**: Specific recommendations for enhancement
- **Score Tracking**: ATS score monitoring over time

### 4. Mock Test Tracking System

#### Test Management
- **CRUD Operations**: Create, read, update, delete mock test records
- **Data Fields**: Test name, source, score, max score, date, notes
- **Performance Tracking**: Historical performance analysis
- **Progress Visualization**: Score trends and improvement metrics

#### Statistical Analysis
- **Score Calculations**: Percentage scores and averages
- **Trend Analysis**: Performance over time visualization
- **Source Tracking**: Performance by test source/platform
- **Goal Setting**: Target score setting and progress monitoring

### 5. Skill Assessment System

#### Technical Skills Checklist
- **Categories**: Programming languages, frameworks, tools, databases
- **Self-Assessment**: Proficiency levels (Beginner, Intermediate, Advanced)
- **Progress Tracking**: Skill development monitoring
- **Personalization**: Department-specific skill recommendations

#### Dynamic Checklist Generation
- **AI-Powered**: Context-aware skill suggestions based on user profile
- **Customization**: User-defined skill categories and items
- **Progress Metrics**: Completion percentages and skill gaps
- **Recommendations**: Learning path suggestions based on assessment

### 6. Habit Tracking System

#### Daily Habits
- **Custom Habits**: User-defined daily study habits
- **Visual Tracking**: Streak visualization and completion history
- **Color Coding**: Customizable habit colors for visual organization
- **Position Management**: Drag-and-drop habit ordering

#### Progress Monitoring
- **Daily Logging**: Mark habits as complete/incomplete
- **Streak Calculation**: Consecutive day streak tracking
- **Calendar View**: Monthly habit completion visualization
- **Statistics**: Completion rates and trend analysis

### 7. Onboarding System

#### Initial Assessment
- **Department Selection**: Academic department identification
- **Self-Evaluation**: Problem-solving, resume readiness, interview readiness
- **Consistency Scoring**: Study habit assessment
- **Overall Score**: Placement readiness calculation

#### Personalization
- **Dashboard Customization**: Tailored content based on assessment
- **Recommendation Engine**: Personalized study suggestions
- **Goal Setting**: Individualized preparation goals
- **Progress Baseline**: Initial metrics for improvement tracking

### 8. Admin Panel

#### User Management
- **User Overview**: Complete user listing with details
- **Profile Management**: Edit user information and settings
- **Account Control**: User deletion and status management
- **Analytics**: User engagement and platform usage statistics

#### Database Management
- **Table Explorer**: Direct database table access
- **Query Interface**: Custom SQL query execution
- **Data Manipulation**: View, edit, delete database records
- **Backup Operations**: Data export and management capabilities

#### System Monitoring
- **Health Checks**: System status and performance monitoring
- **Error Tracking**: Application error logging and analysis
- **Usage Analytics**: Platform usage patterns and insights
- **Leaderboard Management**: User ranking and competition tracking

---

## API Endpoints and Routes

### Authentication Routes
- `GET/POST /login` - User authentication
- `GET/POST /register` - User registration
- `GET/POST /forgot-password` - Password reset request
- `GET/POST /reset-password/<token>` - Password reset confirmation
- `GET /logout` - Session termination

### Application Routes
- `GET /` - Landing page
- `GET /dashboard` - Main user dashboard
- `GET/POST /onboarding` - Initial user assessment
- `GET /mock-tests` - Mock test management page
- `GET /progress` - Habit and progress tracking
- `GET /resume` - Resume analysis interface

### API Endpoints
- `POST /chat` - AI chatbot interaction
- `GET/POST /api/mock-tests` - Mock test CRUD operations
- `PUT/DELETE /api/mock-tests/<id>` - Mock test management
- `GET/POST /api/habits` - Habit management
- `POST /api/habits/toggle` - Daily habit completion
- `GET /api/habits/logs` - Habit history retrieval
- `GET /api/leaderboard` - User rankings
- `POST /api/resume/upload` - Resume file upload
- `POST /api/resume/analyze` - Resume analysis request
- `GET /api/resume/latest` - Latest resume retrieval
- `POST /api/skill-checklist/update` - Skill assessment updates

### Admin Routes
- `GET /admin` - Admin dashboard
- `GET /api/admin/stats` - System statistics
- `GET /api/admin/users` - User management
- `GET/PUT/DELETE /api/admin/users/<email>` - User operations
- `GET /api/admin/tables` - Database table listing
- `GET /api/admin/tables/<name>` - Table data access
- `POST /api/admin/query` - Custom SQL queries

---

## Security Features

### Authentication Security
- **Password Hashing**: Werkzeug secure password hashing
- **Session Management**: Secure server-side sessions
- **Token Security**: Time-limited password reset tokens
- **Input Validation**: Form data sanitization and validation

### Data Protection
- **File Upload Security**: Filename sanitization and type validation
- **SQL Injection Prevention**: Parameterized database queries
- **XSS Protection**: Input sanitization and output encoding
- **CSRF Protection**: Flask CSRF token implementation

### API Security
- **Session Validation**: API endpoint authentication checks
- **Admin Authorization**: Role-based access control
- **Rate Limiting**: Implicit rate limiting through session management
- **Error Handling**: Secure error message display

---

## Performance and Optimization

### Database Optimization
- **Connection Management**: Efficient SQLite connection handling
- **Query Optimization**: Indexed queries and efficient joins
- **Data Caching**: Session-based data caching
- **Schema Design**: Normalized database structure

### Frontend Performance
- **Lazy Loading**: Dynamic content loading
- **Asset Optimization**: Minified CSS and JavaScript
- **Responsive Design**: Mobile-optimized interface
- **Progressive Enhancement**: Graceful degradation for older browsers

### API Performance
- **Async Processing**: Non-blocking AI API calls
- **Error Handling**: Robust error recovery mechanisms
- **Response Caching**: Client-side response caching
- **Resource Management**: Efficient memory usage

---

## Deployment and Configuration

### Environment Configuration
- **Environment Variables**: Secure configuration management
- **Database Setup**: Automatic SQLite database initialization
- **File Storage**: Organized file system structure
- **Logging**: Application error and access logging

### Dependencies
- **Python 3.9+**: Core runtime requirement
- **Flask**: Web framework
- **OpenAI**: AI API integration
- **PyPDF2/python-docx**: Document processing
- **Werkzeug**: Security utilities
- **itsdangerous**: Token security

### Configuration Files
- **.env**: Environment variables and secrets
- **requirements.txt**: Python dependencies
- **run.py**: Application entry point
- **base.txt**: Base configuration template

---

## User Experience and Interface

### Design Principles
- **User-Centric Design**: Intuitive interface focused on user needs
- **Responsive Layout**: Mobile-friendly design
- **Progressive Disclosure**: Information hierarchy and flow
- **Visual Feedback**: Loading states and success indicators

### Key Interface Features
- **Dashboard Widgets**: At-a-glance progress overview
- **Interactive Charts**: Visual progress representation
- **Drag-and-Drop**: Habit reordering functionality
- **Real-time Updates**: Dynamic content updates
- **Accessibility**: WCAG compliance considerations

### User Journey
1. **Registration**: Simple account creation process
2. **Onboarding**: Comprehensive initial assessment
3. **Dashboard**: Personalized preparation hub
4. **Feature Exploration**: Guided feature discovery
5. **Progress Tracking**: Continuous improvement monitoring

---

## Conclusion

PrepPulse represents a comprehensive approach to placement preparation, combining AI-powered guidance with robust tracking and analytics. The system's modular architecture allows for easy expansion and maintenance while providing users with a seamless, personalized preparation experience.

The application successfully integrates multiple complex features including AI chatbot assistance, automated resume analysis, comprehensive progress tracking, and administrative tools, all within a secure and user-friendly interface. The technology choices prioritize reliability, security, and scalability while maintaining development efficiency.

The platform's strength lies in its ability to provide personalized guidance through AI integration while maintaining detailed progress tracking and analytics, making it an effective tool for students preparing for campus placements.
