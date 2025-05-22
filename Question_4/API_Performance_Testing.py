import requests
import time

def endpointTest(endpoint, num_request):
    # Create empty lists to store response time
    time_respond = []

    # Print test config details
    print(f"Endpoint API: {endpoint}")
    print(f"Number of requests: {num_request}")
    print("-" * 25)

    # Loop through specified number of requests
    for i in range (num_request):
        try:
            # Record time of request for endpoint
            time_start = time.time()
            response =  requests.get(endpoint)
            time_end = time.time()

            # Calculate respond time in millisecond
            response_time = (time_end - time_start) * 1000
            time_respond.append(response_time)

            # Check if request is successful (status code : 200), if not then print the failed status code with response time
            if response.status_code == 200:
                print(f"Request {i+1}: Status {response.status_code}, Time: {response_time:.2f} ms")
            else:
                print(f"Request {i+1}: Failed with status {response.status_code}, Time: {response_time:.2f} ms")
        
        # Handling other network related error
        except requests.exceptions.RequestException as x:
            print(f"Request {i+1}: Failed with error {str(x)}")
    
def main():

    # Define the API endpoint to test
    test_endpoint = "https://restcountries.com/v3.1/all"

    # Calling endpointTest function with the test PI endpoint and number of requests
    endpointTest(test_endpoint, 5)

# Execute the main function
main()
