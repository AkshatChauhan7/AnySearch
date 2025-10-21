import os
import sys
from exa_py import Exa

def main():

    api_key = os.environ.get("EXA_API_KEY")

    if not api_key:
        print("Error: EXA_API_KEY environment variable not set.")
        print("Please set the variable before running the script.")
        print("  - Windows: $env:EXA_API_KEY = 'your-key'")
        print("  - Linux/Mac: export EXA_API_KEY='your-key'")
        print("\nFor the full web application, run: python app.py")
        sys.exit(1)
        
    exa = Exa(api_key)
    
    query = input('Search here: ')

    print(f"\nSearching for: '{query}'...")
    
    try:
        search_response = exa.search(
            query,
            num_results=5,
            type='neural',
            use_autoprompt=True
        )

        result_ids = [result.id for result in search_response.results]

        print(f"Found {len(result_ids)} results. Fetching contents...")

        if result_ids:
            contents_response = exa.get_contents(
                result_ids,
                highlights=True,
                text={"max_characters": 1000}
            )

            for result in contents_response.results:
                print(f'## Title: {result.title}')
                print(f'URL: {result.url}')
                
                if hasattr(result, 'highlights') and result.highlights:
                    print('Highlights:')
                    for highlight in result.highlights:
                        print(f' - {highlight.strip()}')
                
                elif hasattr(result, 'text') and result.text:
                    print('Content Snippet:')
                    print(f'{result.text}...')
                    
                print('-' * 30)

        else:
            print("No results found for your query.")

    except Exception as e:
        print(f"An error occurred: {e}")
        print("For the full web application with better error handling, run: python app.py")

if __name__ == "__main__":
    main()