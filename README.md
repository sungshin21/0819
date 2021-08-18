# 2021sw
<이곳저곳 홈페이지: 먹거리 추천과 관광명소 추천>

[장고 활용하기 절차(전체 페이지 확인)]
1. VS Code 터미널에 장고 설치하기(pip install django)
2. 경로를 project 폴더 내부로 이동시키기(cd project)
3. Django 8000서버로 프로젝트 실행하기(python manage.py runserver)

[리뷰 작성하기 절차]
1. MySQL 활용하여 TESTDB 데이터베이스 생성하기
2. NodeJS LTS 버전 설치하기(https://nodejs.org/en/)
3. 벡엔드 터미널에 node index 입력하기
4. 

[로그인, 회원가입 절차]
1. 터미널에 $ python manage.py createsuperuser 입력
2. 비밀번호까지 입력 후 (http://127.0.0.1:8000/admin/) 으로 이동
3. 회원가입한 사용자 확인 가능

[영업소 등록하기 절차]
1. XAMPP 설치(https://www.apachefriends.org/download.html)
2. Apache, MySQL start 버튼 누르기
3. shell에 sungshin 데이터베이스 만들기
4. 웹에 localhost/tables.php 입력하여 table 생성 확인하기
5. 영업소 등록하기 눌러서 정보를 입력하여 제출하기 -> 제출 성공 확인하기
6. 웹이 localhost/result.php 입력하여 table에 정보 입력받은 것 확인하기
