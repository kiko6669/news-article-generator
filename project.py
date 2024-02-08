import openai
import requests

# Set up OpenAI API key
openai.api_key = 'OPEN-AI-KEY'

# Fetch headline from News API
news_api_url = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=d67ecec5cecd4a5a9bc90016c7042e5d'
response_news = requests.get(news_api_url)

if response_news.status_code == 200:
    articles = response_news.json()['articles']
    headlines = [article['title'] for article in articles]
else:
    print('Failed to fetch headlines from News API. Status code:', response_news.status_code)
    headlines = []
    headlines = input('Enter your article headline: ')

# Prompt for article idea
content_idea = input(f'Enter your article idea based on the headline "{headlines}": ')

# Generate article title
response_title = openai.Completion.create(
    engine="gpt-3.5-turbo-instruct",
    prompt=f'Generate a catchy title for an article about {content_idea}.',
    max_tokens=10,
    temperature=0.5,
    stop=['\n']
)
article_title = response_title.choices[0].text.strip()

# Generate tags
response_tags = openai.Completion.create(
    engine="gpt-3.5-turbo-instruct",
    prompt=f'Generate relevant tags for an article about {content_idea}.',
    max_tokens=50,
    temperature=0.5,
    stop=['\n']
)
tags = response_tags.choices[0].text.strip().split(',')

# Generate article content
response_content = openai.Completion.create(
    engine="gpt-3.5-turbo-instruct",
    prompt=f'Generate an insightful article on {content_idea} in the most human way possible write only articles dont respond with anyting else.',
    temperature=0.7,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=['###']
)
article_text = response_content.choices[0].text.strip()

# Save article to a file
with open('article.txt', 'w') as f:
    f.write(article_text)

# Post article to Medium using the Medium API
medium_access_token = 'Medium_API-KEY'
headers = {
    'Authorization': f'Bearer {medium_access_token}',
    'Content-Type': 'application/json',
}

payload = {
    'title': article_title,
    'contentFormat': 'markdown',
    'content': article_text,
    'tags': tags,
    'publishStatus': 'public',  # Change to 'public' when ready to publish
}

response = requests.post('https://api.medium.com/v1/users/{user_id}/posts', headers=headers, json=payload)

if response.status_code == 201:
    print('Article posted to Medium successfully!')
else:
    print('Failed to post article to Medium. Status code:', response.status_code)
    print('Error message:', response.text)
