# FreightMate™ - Your Freight Comparison Specialist

FreightMate™ is a Streamlit-based web application designed to help users find the most cost-effective freight options by comparing rates, schedules, and routes.

## Features

- Freight Finder: Compare and find the cheapest freight options for specific routes
- Rate Calculator: Estimate freight rates based on weight and distance
- RAG-powered Q&A system for freight-related queries

## Deployment Instructions for Streamlit

### Prerequisites

- Python 3.7+
- pip (Python package installer)
- Git

### Step 1: Clone the repository

```bash
git clone https://github.com/your-username/freightmate.git
cd freightmate
```

### Step 2: Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Step 3: Install required packages

```bash
pip install -r requirements.txt
```

### Step 4: Set up environment variables

Create a `.env` file in the project root and add your OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key_here
```

### Step 5: Prepare the dataset

Ensure that your `freight_data.csv` file is in the project directory.

### Step 6: Run the Streamlit app locally

```bash
streamlit run app.py
```

The app should now be running on `http://localhost:8501`.

### Deployment to Streamlit Cloud

1. Push your code to a GitHub repository.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and sign in.
3. Click on "New app" and select your GitHub repository.
4. Set the main file path to `app.py`.
5. Add your OpenAI API key as a secret with the name `OPENAI_API_KEY`.
6. Deploy the app.

## Usage

1. Navigate through the different sections using the navigation menu.
2. Use the Freight Finder to compare rates for specific routes.
3. Utilize the Rate Calculator for quick freight cost estimates.
4. Ask FreightMate™ questions about freight rates and scheduling using the Q&A feature.

## Support

For any issues or questions, please open an issue on the GitHub repository or contact our support team at support@freightmate.com.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```

Remember to replace `your-username` with your actual GitHub username when you set up the repository. This README provides comprehensive instructions for deploying the FreightMate™ application on Streamlit Cloud.