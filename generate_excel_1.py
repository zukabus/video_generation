import pandas as pd

data = pd.read_excel()

# Sample data for subtitles
data = {
    'start': [0, 10, 20, 30, 40],
    'end': [8, 20, 30, 40, 50],
    'text': [
        "Late one night in an abandoned hospital, two thrill-seeking teenagers, Alex and Maria, explored the eerie, echoing hallways.",
        "As they passed the old surgical ward, the sound of a gurney rolling suddenly filled the air.",
        "The ghostly silhouette of a nurse appeared, pushing the gurney towards them, her face obscured by shadows.",
        "As she neared, she vanished, leaving behind the cold gust of wind and the distant sound of surgical tools clanging.",
        "Terrified but intrigued, they pressed on, only to hear their names whispered from the empty rooms."
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel
df.to_excel('C:/Users/patel/Desktop/movieseat/subtitles.xlsx', index=False)

