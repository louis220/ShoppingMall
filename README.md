# ShoppingMall

 - Django로 만든 ShoppingMall 

개발환경 
-django 2.2.16
-python 3.7.9
-oracle 12c 12.2.0.1.0 

django 2.2이상은 oracle 11g을 지원하지 않는다


 
 migration과 migrate를 실수하면 다시 하기 힘들기 때문에 table을 잘 짜야한다
  > django- admin startapp 이름
  > python manage.py makemigration 추가할DB 
  > python manage.py migrate -> DB에 반영
  > settiong에 app추가를 반드시 해줘야 함
  >> migrate를 다시 해야할때 물리적으로 지워준다
  >> python manage.py migrate --fake 이름 zero
  >> python manage.py migrate 이름 --fake
  >> 후에 다시 makemigrate 
