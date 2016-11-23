from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.shortcuts import redirect, render_to_response
from .models import Post, Man
from blog.form import Man
from django.views.generic.edit import View

def post_list(request):
	if request.method == "POST":
		form = Man(request.POST)
		if form.is_valid():
			id=form.id
			name=form.name
			age=form.age
			us = add()
			ta = us.save(id,name,age)
			return redirect('govorit', pk=form.id)
	else:
		form = Man()
	return render(request, 'blog/shablon.html', {}) #
data = {
    'f': [
        {'id': 1, 'text': 'ololo'},
        {'id': 2, 'text': 'ololo2'},
        {'id': 3, 'text': 'cheeeekii breeki'},
    ]
}
content=[
		{
			'id' : 1,
			'author' : "Путник",
			'text' : "Нет, я не видел Оазис",
			'info' : "Очередной встречный путник. Ничем не отличается от сотен других встречных. Иногда может расспалагать ценной информацией, но не факт что захочет делиться ею за просто так"
		},
		{
			'id' : 2,
			'author' : "Сторож",
			'text' : "Проходи не задерживайся",
			'info' : "Злющий черт. Зарплата пропивается в том же баре который охраняет - можно сказать, работает за еду. Обладает скудным набором фраз по типу 'Проходи, не задерживайся' и 'Тебе сюда нельзя'"
		},
		{
			'id' : 3,
			'author' : "Бандит",
			'text' : "A nyy, cheeeekii breeki!",
			'info' : "А кого еще вы ожидали повстречать в Зоне Отчуждения, и каких повадок ждали от человека с именем Вася Кабан?"
		}
	]
from mysql import connector
class conn():
	def __init__(self):
		self.connection = connector.connect(user='root', password='root', host='127.0.0.1', database='1db')
	def spisok_id(self):
		c = self.connection.cursor()
		c.execute("SELECT id from users;")
		return (c.fetchall())
	def spisok_all(self):
		c = self.connection.cursor()
		c.execute("SELECT * from users;")
		return (c.fetchall())
	def age(self,id):
		self.id=int(id)
		c = self.connection.cursor()
		c.execute("SELECT name,age from users WHERE id = %s"% self.id)
		return (c.fetchall())

class add:
	def __init__(self):
		self.connection = connector.connect(user='root', password='root', host='127.0.0.1', database='1db')

	def save(self,id,name,age):
		self.id = id
		self.name = name
		self.age = age
		c = self.connection.cursor()
		c.execute("INSERT INTO users (id, name, age) VALUES (%s,%s,%s)", (self.id,self.name,self.age))
		self.connection.commit()
		c.close()

def books(request):
 us=conn()
 ta=us.spisok_id()
 take=[]
 for i in ta:
	 take.append(i[0])
 return render(request, 'blog/spisok.html', {"Text": take},{})


def govorit(request, pk):
	us = conn()
	ta = us.age(pk)
	take = []
	for i in ta:
		take.append(i[0])
		take.append(i[1])
	return render(request, 'blog/info.html', {"Text": take})

#def govorit(request, pk):

 #   return render(request, 'blog/info.html',{'post': post})
from django.http import HttpResponse
import datetime
class MyView(View):
	def get(self, request):
		us = conn()
		ta = us.spisok_all()
		take = []
		for i in ta:
			 take.append(i)
		return render_to_response('blog/test.html', {'current': take})