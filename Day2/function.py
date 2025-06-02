#Simply function that prints hello world 
def printer():
    print("hello world !!! ")

printer()


#ppalindrome plus a vowel weight checker
def classify_text(text):
    text = text.lower().replace(" ", "")  # string method .lower(lowercase all the letter) and . replace(replace blank space with empty)
    # Check palindrome
    if text == text[::-1]:  #text[::-1]=> reverse the text given 
        return f"{text} is a palindrome"
    # Count vowels
    vowels = sum(1 for char in text if char in "aeiou") #generator statements
    vowel_ratio = vowels / len(text) if len(text) > 0 else 0 #checks if text length is 0 or not if yes return 0 else result 
    if vowel_ratio > 0.5:
        return f"{text} is vowel-heavy ({vowel_ratio:.2%} vowels)"
    return f"{text} is neither a palindrome nor vowel-heavy"

# Test cases
print(classify_text("Mom"))        # radar is a palindrome
print(classify_text("meow"))        # hello is neither a palindrome nor vowel-heavy
print(classify_text("xyz"))          # xyz is neither a palindrome nor vowel-heavy
print(classify_text("aaaaee"))          # xyz is neither a palindrome nor vowel-heavy




#program that calculates the price of aws instance based on hours 
def estimate_aws_cost(instance_type, hours):  # args are instance_type like t2.micro gives 0.0116 value
    pricing = {"t2.micro": 0.0116, "t2.small": 0.023, "t2.medium": 0.0464}  
    if instance_type not in pricing:                         #checks if key and value are present or not is the pricing array
        return f"Invalid instance type: {instance_type}"
    cost = pricing[instance_type] * hours
    return f"Estimated cost for {instance_type} ({hours} hours): ${cost:.2f}"  # the .2f is for two number after the decimal points

# Test cases
print(estimate_aws_cost("t2.micro", 10))   # Estimated cost for t2.micro (10 hours): $0.12
print(estimate_aws_cost("t2.small", 5))   # Estimated cost for t2.small (5 hours): $0.12
print(estimate_aws_cost("t3.meow", 1))   # Invalid instance type: t3.large


#simple json convertor (python dictionary to json)
import json

# Python dict to JSON string
data = {"name": "lspp", "Day": 2}
json_str = json.dumps(data)   # python dictionary to json 
print("python to json"+json_str);
# JSON string to Python dict
new_data = json.loads(json_str) # json  to python dictionary
print("json to python",new_data) #why , because python dictionary can't be concantenated