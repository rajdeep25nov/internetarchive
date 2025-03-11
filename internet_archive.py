import re
import json
import requests

def extracturls(text):
    
    url_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    urls = re.findall(url_pattern, text)
    return urls

def savetheurls(urls):
    
    with open("urls.json", "w") as f:
        json.dump(urls, f, indent=4)

if __name__ == "__main__":
    
    with open("sample_ocr.txt", "r") as f:
        text = f.read()

    
    urls = extracturls(text)
    print("Extracted URLs:", urls)

    
    savetheurls(urls)


    

def validate_url(url):
    try:
        response = requests.head(url, timeout=5)
        return response.status_code == 200
    except:
        return False

def validate_urls(urls):
    validated_urls = []
    for url in urls:
        status = "valid" if validate_url(url) else "invalid"
        validated_urls.append({"url": url, "status": status})
    return validated_urls

if __name__ == "__main__":
    # Read sample OCR text
    with open("sample_ocr.txt", "r") as f:
        text = f.read()

    # Extract URLs
    urls = extracturls(text)
    print("Extracted URLs:", urls)

    # Validate URLs
    validated_urls = validate_urls(urls)
    print("Validated URLs:", validated_urls)

    # Save URLs to JSON
    savetheurls(validated_urls)

def archive_url(url):
    try:
        response = requests.post(f"https://web.archive.org/save/{url}")
        return response.status_code == 200
    except:
        return False

def archive_urls(urls):
    archived_urls = []
    for url in urls:
        if url["status"] == "valid":
            archived = archive_url(url["url"])
            archived_urls.append({"url": url["url"], "status": url["status"], "archived": archived})
        else:
            archived_urls.append({"url": url["url"], "status": url["status"], "archived": False})
    return archived_urls

if __name__ == "__main__":
    # Read sample OCR text
    with open("sample_ocr.txt", "r") as f:
        text = f.read()

    # Extract URLs
    urls = extracturls(text)
    print("Extracted URLs:", urls)

    # Validate URLs
    validated_urls = validate_urls(urls)
    print("Validated URLs:", validated_urls)

    # Archive URLs
    archived_urls = archive_urls(validated_urls)
    print("Archived URLs:", archived_urls)

    # Save URLs to JSON
    savetheurls(archived_urls)




import re
import json

def clean_url(url):
    # Removing he extra spaces while preserving domain suffixes
    cleaned_url = re.sub(r'\s+', '', url)  # Remove all spaces
    
    # makin sure the URL starts with http:// or https://
    if not cleaned_url.startswith(('http://', 'https://')):
        cleaned_url = 'http://' + cleaned_url
    
    return cleaned_url

def extracturls(text):
    # Regex to find URLs not oerfect one wid spaces
    url_pattern = r'https?://\s*[^\s]+(?:\s*\.[^\s]+)*'
    urls = re.findall(url_pattern, text)
    # Clean extracted URLs
    cleaned_urls = [clean_url(url) for url in urls]
    return cleaned_urls

def savetheurls(urls):
    # to  save URLs to urls.json
    with open("urls.json", "w") as f:
        json.dump(urls, f, indent=4)

if __name__ == "__main__":
    # Read sample OCR text
    with open("sample_ocr.txt", "r") as f:
        text = f.read()

    # extract and clean URLS
    urls = extracturls(text)
    print("Extracted and Cleaned URLs:", urls)

    # Save URLS to JSON
    savetheurls(urls)

    from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def book_reader():
    return render_template("book_reader.html")

if __name__ == "__main__":
    app.run(debug=True)