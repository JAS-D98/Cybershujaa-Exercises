from bs4 import BeautifulSoup
import requests
import pandas as pd

# Target URL containing country data
url = "https://www.scrapethissite.com/pages/simple/"

try:
    # Send HTTP request to the URL
    page = requests.get(url)
    page.raise_for_status()  # Raise an exception for HTTP errors
    
    # Parse the HTML content
    soup = BeautifulSoup(page.text, 'html.parser')
    
    # Initialize lists to store extracted data
    countries = []
    capitals = []
    populations = []
    areas = []
    
    # Find all country divs
    country_divs = soup.find_all('div', class_='country')
    
    for country in country_divs:
        # Extract country name (from h3 tag with class 'country-name')
        country_name = country.find('h3', class_='country-name').get_text(strip=True)
        countries.append(country_name)
        
        # Extract country info
        country_info = country.find('div', class_='country-info')
        
        # Extract capital (from span with class 'country-capital')
        capital = country_info.find('span', class_='country-capital').get_text(strip=True)
        capitals.append(capital)
        
        # Extract population (from span with class 'country-population')
        population = country_info.find('span', class_='country-population').get_text(strip=True)
        populations.append(population)
        
        # Extract area (from span with class 'country-area')
        area = country_info.find('span', class_='country-area').get_text(strip=True)
        areas.append(area)
        
        # Print individual country data (optional)
        print(f"Country: {country_name}")
        print(f"Capital: {capital}")
        print(f"Population: {population}")
        print(f"Area (km²): {area}")
        print("-" * 40)
    
    # Create a DataFrame from the collected data
    data = {
        'Country': countries,
        'Capital': capitals,
        'Population': populations,
        'Area (km²)': areas
    }
    df = pd.DataFrame(data)
    
    # Save to CSV file
    csv_filename = 'countries_data.csv'
    df.to_csv(csv_filename, index=False)
    print(f"\nData successfully saved to {csv_filename}")
    
    # Display the first few rows of the DataFrame (optional)
    print("\nSample of the extracted data:")
    print(df.head())

except requests.exceptions.RequestException as e:
    print(f"Error making HTTP request: {e}")
except Exception as e:
    print(f"An error occurred: {e}")