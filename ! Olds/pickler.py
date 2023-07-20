import json
import pickle

def json_to_pickle(json_cookie_str):
    # Deserialize the JSON cookie into a Python dictionary
    cookie_dict = json.loads(json_cookie_str)

    # Serialize the dictionary into a pickle format
    pickle_cookie = pickle.dumps(cookie_dict)

    return pickle_cookie

# Read JSON cookie data from the file
with open("JsonCookie.json", "r") as json_file:
    json_cookie_str = json_file.read()

# Convert JSON cookie to a pickle cookie
pickle_cookie = json_to_pickle(json_cookie_str)

# Save the pickle cookie to a file
with open("PickledCookie.pkl", "wb") as pickle_file:
    pickle_file.write(pickle_cookie)
