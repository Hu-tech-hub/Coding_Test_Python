# 문제 23 : 베스트앨범 < - 오답 필요**

def solution(genres, plays):
  answer = []
  
  # 문제 분석 
  # 분류 우선도 : 많이 재생된 장르 순서
  play_dic = {} # 장르별 재생 횟수
  
  for i in genres:
    play_dic[i] = play_dic.get(i, 0) + plays[i]
  
  sorted_play_list = sorted(play_dic.items(), key=lambda x: x[1], reverse=True)
  
  # 장르 내 우선도 : 많이 재생된 노래 순서 -> 고유 번호 순서
  genre_dic = {}
  
  for genre, _ in sorted_play_list:
    genre_dic[genre] = []
    
  for i in range(len(genres)):
    genre_dic[genres[i]].append((plays[i], i))
    
  for genre, _ in sorted_play_list:
    genre_dic[genre].sort(key=lambda x: (-x[0],x[1]), reverse=False)
    answer.extend([idx for _, idx in genre_dic[genre][:2]])
  
  