from collections import defaultdict


def solution(genres, plays):
    genre_total_plays = defaultdict(int)
    songs_by_genre = defaultdict(list)
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        genre_total_plays[genre] += play
        songs_by_genre[genre].append((i, play))
    
    sorted_genres = sorted(genre_total_plays.items(), key=lambda x: x[1], reverse=True)
    
    result = []
    for genre, _ in sorted_genres:
        sorted_songs = sorted(songs_by_genre[genre], key=lambda x: (-x[1], x[0]))
        for i in range(len(sorted_songs)):
            if i == 2:
                break
            result.append(sorted_songs[i][0])

    return result
