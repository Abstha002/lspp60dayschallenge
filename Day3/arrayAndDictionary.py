#First program for List and dictionary
scores={                                #Here scores is the dictionaries key is name and value is a list of marks 
    "Ram":[20,50,90],
    "Shyam":[20,50,90],
    "SpiderMan":[90,98,56]
}
ranks={}   
for index, name in enumerate(scores):  #Here the enumerate method goes through all the key value in scores
    total=sum(scores[name])
    ranks[name]=total
    print(f"{index+1}. {name} Total Marks: {total}")

topper=max(ranks,key=ranks.get)  #max method if checks ranks.get(ram)=>160 ... then highest values
print(f"{topper} is Topper with {ranks[topper]} marks")


















def track_aws_services():
   
    services = [                                                 # List and inside of list there is dictonary
        {"name": "EC2", "category": "Compute", "cost_per_hour": 0.16},
        {"name": "S3", "category": "Storage", "cost_per_hour": 0.23},
        {"name": "Lambda", "category": "Compute", "cost_per_hour": 0.67},
        {"name": "RDS", "category": "Database", "cost_per_hour": 0.32}
    ]
    # Sort by name
    sorted_services = sorted(services, key=lambda x: x["name"])      #Here the lamba function create list base of name and sorted function sorts in alphabetically order
    print(sorted_services)
    # Filter Compute services
    compute_services = [s for s in services if s["category"] == "Compute"]  #Make a new list of only those services where the category is 'Compute
    return {"all_services": sorted_services, "compute_only": compute_services}

# Test
result = track_aws_services()  #result is dictionary as func returns dictonary
print("Sorted AWS Services:")
for service in result["all_services"]:
    print(f"{service['name']}: {service['category']} (${service['cost_per_hour']:.2f}/hr)")
print("\nCompute Services:")
for service in result["compute_only"]:
    print(f"{service['name']}: ${service['cost_per_hour']:.2f}/hr")