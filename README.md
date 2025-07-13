# 🏏 IPL Win Predictor

A machine learning-powered web application that predicts the probability of a team winning an IPL (Indian Premier League) cricket match based on real-time match statistics.

## 🌟 Features

- **Real-time Predictions**: Get win probability predictions during live matches
- **Comprehensive Input Fields**: 
  - Batting and bowling team selection
  - Match venue (city)
  - Runs remaining to win
  - Balls remaining
  - Wickets in hand
  - Current run rate (CRR)
  - Required run rate (RRR)
  - Total runs scored so far
- **User-friendly Interface**: Clean, responsive web interface with dark theme
- **Autofill Example**: Quick demo with sample data
- **Instant Results**: Real-time probability calculation and win/lose prediction

## 🏗️ Architecture

- **Backend**: FastAPI (Python web framework)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Machine Learning**: Scikit-learn pipeline
- **Templates**: Jinja2 templating engine
- **Styling**: Custom dark theme CSS

## 📊 Model Information

The application uses a pre-trained machine learning pipeline (`pipe.pkl`) that includes:
- **Algorithm**: Classification model (likely Random Forest or similar)
- **Features**: 9 key match parameters
- **Output**: Win probability percentage and binary prediction (Win/Lose)
- **Training Data**: Historical IPL match data

### Supported Teams
- Chennai Super Kings
- Deccan Chargers
- Delhi Capitals
- Delhi Daredevils
- Kings XI Punjab
- Kolkata Knight Riders
- Mumbai Indians
- Rajasthan Royals
- Royal Challengers Bangalore
- Sunrisers Hyderabad

### Supported Cities
29 major cricket venues including:
- Indian cities: Mumbai, Delhi, Bangalore, Chennai, Kolkata, etc.
- International venues: Abu Dhabi, Cape Town, Johannesburg, etc.

## 🚀 Quick Start

### Prerequisites
- Python 3.11 or higher
- pip package manager

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ipl-win-predictor
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python -m uvicorn main:app --reload
   ```

4. **Access the application**
   - Open your browser and go to `http://localhost:8000`
   - The application will be available with hot-reload enabled

### Using the Application

1. **Fill in match details**:
   - Select batting and bowling teams
   - Choose the match venue
   - Enter current match statistics

2. **Get predictions**:
   - Click "Predict" to see win probability
   - Use "Autofill Example" for a quick demo

3. **Interpret results**:
   - Win probability percentage
   - Predicted outcome (Win/Lose)

## 🌐 Deployment

### Render Deployment

1. **Connect your repository** to Render
2. **Create a new Web Service**
3. **Configure the service**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Environment**: Python 3

### Environment Variables
- `PORT`: Automatically provided by Render

### Alternative Deployment Platforms

#### Heroku
```bash
# Create Procfile
echo "web: uvicorn main:app --host 0.0.0.0 --port \$PORT" > Procfile

# Deploy
heroku create your-app-name
git push heroku main
```

#### Railway
- Connect your GitHub repository
- Railway will auto-detect Python and install dependencies
- Set start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

## 📁 Project Structure

```
ipl-win-predictor/
├── main.py              # FastAPI application entry point
├── pipe.pkl             # Pre-trained machine learning model
├── requirements.txt     # Python dependencies
├── runtime.txt          # Python version specification
├── README.md           # This file
├── static/
│   └── style.css       # Custom CSS styles
└── templates/
    └── index.html      # Main HTML template
```

## 🔧 Technical Details

### Dependencies
- **FastAPI**: Modern web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI
- **Scikit-learn**: Machine learning library
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Jinja2**: Template engine
- **Python-multipart**: Form data handling

### API Endpoints
- `GET /`: Main application page with prediction form
- `POST /`: Process prediction form and return results

### Model Input Features
1. `batting_team`: Team currently batting
2. `bowling_team`: Team currently bowling
3. `city`: Match venue
4. `runs_left`: Runs needed to win
5. `balls_left`: Balls remaining
6. `wickets`: Wickets in hand
7. `total_runs_x`: Total runs scored so far
8. `crr`: Current run rate
9. `rrr`: Required run rate

## 🎨 UI/UX Features

- **Dark Theme**: Easy on the eyes with modern styling
- **Responsive Design**: Works on desktop and mobile devices
- **Bootstrap Integration**: Professional UI components
- **Form Validation**: Client-side and server-side validation
- **Autofill Demo**: Quick example with realistic data

## 🔍 Troubleshooting

### Common Issues

1. **ModuleNotFoundError: No module named 'pandas'**
   ```bash
   pip install -r requirements.txt
   ```

2. **Model loading errors**
   - Ensure `pipe.pkl` is in the root directory
   - Check scikit-learn version compatibility

3. **Port already in use**
   ```bash
   uvicorn main:app --reload --port 8001
   ```

### Version Compatibility
- Python: 3.11+
- Scikit-learn: 1.6.1 (specific version for model compatibility)
- FastAPI: 0.104.1
- Uvicorn: 0.24.0

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- IPL for the cricket data
- Scikit-learn community for the machine learning tools
- FastAPI team for the excellent web framework
- Bootstrap team for the UI components

## 📞 Support

For issues and questions:
- Create an issue in the repository
- Check the troubleshooting section above
- Ensure all dependencies are properly installed

---

**Note**: This application is for educational and entertainment purposes. Cricket predictions are based on historical data and should not be used for betting or gambling purposes.
