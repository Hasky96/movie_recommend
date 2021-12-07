from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import tweepy
pd.set_option('display.max_row', 500)
pd.set_option('display.max_columns', 100)
import gensim
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
from gensim.models import Word2Vec
from konlpy.tag import Okt # 옛날 Twitter 클래스
okt = Okt()
import pickle
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
import random
# Word2Vec 모델 불러오기
embedding_model = gensim.models.Word2Vec.load('recommend\word2VecModel')

# 코사인 유사도 시스템 설정
with open('recommend\movie_dict.pickle', 'rb') as f:
    movie_dict = pickle.load(f)
df = pd.DataFrame(list(movie_dict.items()),columns = ['title','review'])  
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(df.review)
cos_similar = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series(df.index, index = df.title)
###------------ 추천시스템 -------------- ###

from movies.models import Movie
from movies.serializers import MovieSerializer
# 키워드 송출 시스템
@api_view(['POST'])
def movie_recommend(request):
    # 키워드 check (입력 키워드가 이상하면 다시)
    def keyword_check(keyword):
        try:
            keyword = okt.morphs(keyword, stem=True)
            FirstKeyword = keyword[0]
            # check embedding result
            VecWords = embedding_model.wv.most_similar(positive=[FirstKeyword], topn=100)
            Veclist1 = []
            for i in range(0,31):
                Veclist1.append(VecWords[i][0])
            context = {
                'state' : True,
                'Veclist1' : Veclist1[:10],
                'first_keyword' : keyword
            }
            return context
        except KeyError: 
            # keyError 값을 return 해줘야 하는데??
            # 리턴값이 XX 이면 ALTER 을 발생?
            context = {
                'state' : False,
                'Veclist1' : '다른 키워드를 넣어주세요!',
            }
            return context
    # 이때 키워드는 request 에 담겨서 넘어와야 한다.
    word  = request.data.get('inputKeyword')#로맨틱 #아련한
    context = keyword_check(word)
    return Response(context, status=status.HTTP_200_OK)

# 추천영화 전송 시스템

@api_view(['POST'])

def show_recommend_movie(request):
    FirstKeyword  = request.data.get('firstKeyword')# 첫번째 키워드
    SecondKeyword  = request.data.get('secoundKeyword')# 두번째 키워드
    ThirdKeyword  = request.data.get('thirdKeyword')# 세번째 키워드
    # list_num  = request.# 리스트
    Veclist1  = request.data.get('firstData')# 리스트
    Veclist2  = request.data.get('secoundData')# 리스트
    Veclist3  =request.data.get('thirdData')# 리스트
    # 벡터 가중치 설정
    myVec = [FirstKeyword]*3+Veclist1+[SecondKeyword]*2+Veclist2[:5]+[ThirdKeyword] + Veclist3[:5]
    # 테이블 불러오기
    mymyCut = pd.read_csv("recommend\CosDataTable.csv")
    # 코사인 유사도 확인
    mysent=""
    for i in myVec:
        mysent += "".join(i)
        mysent += " "
    mydf = pd.Series(['입력',mysent,mysent], index=["영화명","리뷰","word"])
    mymyCut = mymyCut.append(mydf, ignore_index=True)
    mymyCut.iloc[-1,:]
    # TFIDF 설정
    Tfidf = TfidfVectorizer() 
    Tfidf_matrix = Tfidf.fit_transform(mymyCut['word'])

    cos_similar = linear_kernel(Tfidf_matrix, Tfidf_matrix)

    def getRecommendation1(cos_similar= cos_similar):
        # idx = indices[title]
        simScores = list(enumerate(cos_similar[-1])) #코사인유사도
        # simScores : 튜플 (인덱스,코사인유사도)
        simScores = sorted(simScores, key=lambda x: x[1] ,reverse=True)
        # 코사인유사도 기준 내림차순 정렬된 튜플중 자기 제외하고 20개 뽑음
        simScores = simScores[1:21]
        # 상위 20개 영화의 인덱스값 저장
        movieidx = [i[0] for i in simScores]
        RecMovielist = mymyCut.iloc[movieidx] 
        return RecMovielist[['영화명','리뷰']]
    
    movie_list = getRecommendation1()
    context = {
        'movie_list' : movie_list
    }
    return Response(context, status=status.HTTP_200_OK)

@api_view(['POST'])
def title_recommend(request):
    def movie_Recommendation(title, cos_similar=cos_similar):
        try:
            idx = indices[title]
            # 모든 영화에 대해서 해당 영화와의 유사도를 구하기
            cos_like = list(enumerate(cos_similar[idx]))
            cos_like = sorted(cos_like, key=lambda x:x[1], reverse = True) # score 순으로 정렬

            cos_like = cos_like[1:21] # 가장 유사한 10개의 영화를 받아옴
            movie_indices = [i[0] for i in cos_like] # 인덱스 받아오기
            
            result_df = df.iloc[movie_indices].copy()  #기존에 읽어들인 데이터에서 해당 인덱스의 값을 가져오기 스코어 열을 추가
            result_df['score'] = [i[1] for i in cos_like]
            # 20개의
            context = {
                'state' : True,
                'Veclist1' : result_df,
            }
            return context
        except KeyError:
            context = {
                'state' : False,
                'Veclist1' : '다른 키워드를 넣어주세요!',
            }
            return context
    a = request.data.get('titleGet')
    context = movie_Recommendation(a)
    return Response(context, status=status.HTTP_200_OK)

@api_view(['POST'])
def catch_data(request):
    try:
        a = request.data.get('movieList')
        movie = get_object_or_404(Movie, title=a)
        serializer = MovieSerializer(movie)

        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        context = {
                'title' : '영화없음',
            }
        return Response(context, status=status.HTTP_200_OK)

@api_view(['GET'])
def detail_recommend(request,movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    genres = movie.genre.all()
    data = Movie.objects.filter(genre__in = genres).order_by('-vote_count').distinct()
    selctions = [0, 10, 20, 30, 40]
    pick = random.choice(selctions)
    data = data[pick:pick+24]
    title = []
    overview = []
    pp = []
    pk = []
    for i in range(len(data)):
        title .append(data[i].title)
        overview .append(data[i].overview)
        pp.append(data[i].poster_path)
        pk.append(data[i].pk)
    if movie.overview == '':
        movie.overview = '줄거리를 준비중 입니다'
    context = {
        'title' : title,
        'overview' : overview,
        'pp' : pp,
        'pk' : pk,
    }
    return Response(context, status=status.HTTP_200_OK)