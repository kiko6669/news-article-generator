# News Article Generator
This Python script utilizes the OpenAI API to generate articles based on real-time headlines fetched from the News API. It prompts users for an article idea, generates a catchy title, relevant tags, and insightful content using GPT-3.5. Users can save the generated article to a file and optionally post it to Medium via the Medium API. Si

Example of generated Articles:
1:
![Screenshot 2024-02-08 134626](https://github.com/kiko6669/news-article-generator/assets/146574480/ea0bbbec-0b8e-4f54-8950-d3433607dff3)


2:
![Screenshot 2024-02-08 134634](https://github.com/kiko6669/news-article-generator/assets/146574480/710db94d-a8c9-487e-9cb7-45c288f8b71e)


3:
![Screenshot 2024-02-08 134641](https://github.com/kiko6669/news-article-generator/assets/146574480/c2950ccb-3594-4369-b672-4004b423dc22)


## Installation Guide:

1. Clone the Repository:

git clone https://github.com/kiko6669/news-article-generator.git

2. Navigate to the Project Directory:

cd news-article-generator

3. Install Dependencies:

pip install -r requirements.txt

4. Set Up API Keys:

Obtain an API key from https://newsapi.org/  and replace {News_API_KEY} in the project.py file with your API key. 

Obtain an API key from OpenAI and replace 'OPEN-AI-KEY' in the project.py file with your API key.

Get an access token from Medium and replace 'Medium_API-KEY' in the project.py file with your access token.

Update the Medium user ID in the URL 'https://api.medium.com/v1/users/{user_id}/posts' to your Medium user ID.

5. Run the Script:

python project.py

6. After running the script, you'll be prompted to provide an article idea based on the fetched headlines. Additionally, the script will print the news headlines fetched from the News API for your reference.

Once you enter the article idea, the script will generate a catchy title, relevant tags, and insightful content automatically using the OpenAI API. And it will post to medium auto # you can change between draft and public in script
