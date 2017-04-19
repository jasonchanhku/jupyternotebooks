import read
from collections import Counter

if __name__ == "__main__":
    df = read.load_data()
    headlines = df["headline"]
    headlines = headlines.tolist()
    new = ""
    for i in headlines:
        new += (str(i) + " ")
    new = new.strip().lower()
    new = new.replace(":", "")
    new = new.replace("(", "")
    new = new.replace(")", "")
    new = new.replace("\\", "")
    new = new.replace("\'", "")
    new = new.replace("?", "")
    new = new.replace("[", "")
    new = new.replace("]", "")
    new = new.replace("#", "")
    new = new.replace("&", "")
    new = new.split(" ")
    
    cnt = Counter()
    for word in new:
        cnt[word] += 1
    
    print(cnt.most_common(100))