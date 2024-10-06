import requests
from bs4 import BeautifulSoup
import datetime


def web_scraper(url, keywords):
    # Making a request to the website
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while trying to access the URL: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # Looking for keywords and collecting phrases
    results = {}
    for word in keywords:
        print(f"Looking for: '{word}'...")
        matches = soup.find_all(string=lambda text: text and word.lower() in text.lower())

        # Collecting matching phrases and counting occurrences
        results[word] = {
            'count': len(matches),
            'phrases': [match.strip() for match in matches]
        }

    # Save the results with a timestamp
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"scraper_results_{timestamp}.txt"

    with open(filename, 'w') as file:
        file.write(f"Results for keywords: {', '.join(keywords)}\n\n")
        for word, data in results.items():
            file.write(f"{word}: {data['count']} occurrences\n")
            for phrase in data['phrases']:
                file.write(f" - {phrase}\n")

    print(f"All done! The results have been saved to: {filename}")


# Example usage
if __name__ == "__main__":
    url = 'https://news.ycombinator.com/'  # Change this to the URL you want to scrape
    keywords = ['Hacker', 'news', 'JavaScript', 'and']  # Add the keywords you want to search for here
    web_scraper(url, keywords)
















