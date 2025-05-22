import requests
import time

def endpointTest(endpoint, num_request):
    time_respond = []
    print(f"Endpoint API: {endpoint}")
    print(f"Number of requests: {num_request}")
    print("-" * 25)

    for i in range (num_request):
        try:
            time_start = time.time()
            response =  requests.get(endpoint)
            time_end = time.time()

            response_time = (time_end - time_start) * 1000
            time_respond.append(response_time)

            if response.status_code == 200:
                print(f"Request {i+1}: Status {response.status_code}, Time: {response_time:.2f} ms")
            else:
                print(f"Request {i+1}: Failed with status {response.status_code}, Time: {response_time:.2f} ms")
        
        except requests.exceptions.RequestException as x:
            print(f"Request {i+1}: Failed with error {str(x)}")
    
def main():

    test_endpoint = "https://restcountries.com/v3.1/all"
    endpointTest(test_endpoint, 5)

main()
