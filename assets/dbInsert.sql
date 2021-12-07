-- DB에 영화정보와 장르정보를 삽입하는 쿼리문입니다.
-- 쿼리에서 인서트문을 열어 복사해 사용하는걸 추천합니다.

-- 기존데이터 삭제를 원하시지 않는 분은 주석처리 해주세요
DELETE FROM movies_movie;
DELETE FROM movies_genre;
DELETE FROM movies_genre_movie;
-- 삽입되는 문장입니다.

.import C:\\Users\\SSAFY\\Desktop\\pjt-final\\assets\\genre_movie.csv movies_genre_movie
.import 파일 경로를 입력해 주세요\\assets\\genres.csv movies_genre
.import C:\\Users\\SSAFY\\Desktop\\pjt-final\\assets\\movies.csv movies_movie