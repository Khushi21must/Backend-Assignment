# Backend-Assignment
Project Title - FAQ Model

Description - This project is a backend system designed to manage FAQs in multiple languages. It includes features such as WYSIWYG editor support, multilingual FAQ management, caching using Redis, and Google Translate API integration.

Features of this Project -
- Multilingual FAQ management
- WYSIWYG editor support for easy content creation
- Caching for faster response times (Redis)
- Integration with Google Translate API for automatic language detection
- API development for easy access to FAQ data

Installation Guide for the Project - 

1. Clone the repository: copy the url of the repository and clone it 
   ```bash
   git clone https://github.com/your-username/Backend-Assignment.git
   ```

2. Navigate to the project directory: change the directory to your project in your terminal 
   ```bash
   cd backend
   ```

3. Install dependencies: install all the required libraries
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables (if any). Create a `.env` file and add the following:
   ```
   SECRET_KEY=your_secret_key
   DB_NAME=your_db_name
   ```

5. Run the Django development server:
   ```bash
   python manage.py runserver
   ```

6. Access the project in your browser at `http://127.0.0.1:8000/`.

Usage -
- Once the server runs, you can access the FAQ management system through the frontend interface.
- Admin users can add, update, or delete FAQs.
- The system supports multiple languages, and the content will be automatically translated using the Google Translate API.

Contribution -
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request on GitHub.

Contact
For any inquiries, please contact me at khushijain21must@gmail.com.
