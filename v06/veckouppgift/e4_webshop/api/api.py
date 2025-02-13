import requests
from typing import Any


class Api():
    """
    A class dedicated to handle API calls.
    Will return the RAW JSON back to the caller and it is up to them to fix it.
    """
    
    def __init__(self, url: str) -> None:
        """
        Init for the API and only stores the URL
        """
        self._url = url


    def __call__(self) -> Any | None:
        """
        When the instance of the APi is called the request is executed
        Return
        """
        try:
            response = requests.get(self._url)

            if response.status_code == 200:
                data = response.json()
                return data
            
            else:
                print("Error:", response.status_code)
                return None
        
        except requests.exceptions.RequestException as e:
            print('Error:', e)
            return None
        
        except:
            print("Something else went wrong")
            return None
    

    def __del__(self):
        """
        Makes sure that the url gets destoryed
        """
        del(self._url)



if __name__ == "__main__":
    print("Wrong file")