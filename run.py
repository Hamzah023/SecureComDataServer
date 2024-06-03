from app import create_app

app = create_app()

for rule in app.url_map.iter_rules(): # Iterate over the rules in the app's URL map
    print(rule)

if __name__ == '__main__':
    app.run(debug=True) #turn off debug=true when want one api key


