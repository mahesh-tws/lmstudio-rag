from scraper import scrape
from embedder import embed
from chat import startChat

# Starting URL
start_url = "https://thoughtswinsystems.com/"
# Starting depth
start_depth = 2

scrape(start_url, start_depth)
embed()
startChat()
