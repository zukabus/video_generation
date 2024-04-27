import pandas as pd

def calculate_durations(text, wpm=160):
    words = text.split()
    wps = wpm / 60  # words per second
    durations = []
    start_time = 0
    
    words_per_segment = max(4 * wps, 10)  # at least 10 words per segment

    while words:
        segment = ' '.join(words[:int(words_per_segment)])
        duration = len(segment.split()) / wps
        end_time = start_time + duration
        durations.append((start_time, end_time, segment))
        words = words[int(words_per_segment):]
        start_time = end_time
    
    return durations

# Load the data from Excel
df = pd.read_excel('C:/Users/patel/Desktop/movieseat/subtitles.xlsx')

# Process each row in the dataframe
all_subtitles = []
for index, row in df.iterrows():
    subtitles = calculate_durations(row['text'], wpm=160)
    all_subtitles.extend([(index + 1, f"{start:.2f}", f"{end:.2f}", text) for (start, end, text) in subtitles])

# Create a new DataFrame
subtitles_df = pd.DataFrame(all_subtitles, columns=['index', 'start', 'end', 'text'])

# Save to Excel
subtitles_df.to_excel('C:/Users/patel/Desktop/movieseat/subtitles1.xlsx', index=False)
