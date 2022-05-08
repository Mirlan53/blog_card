from django.shortcuts import render

# Create your views here.
def blogs_index(request):
	blogs = [
		{'name': 'Мой первый блог', 'author': {'name': 'admin'}, 'publication_date': '16.04.2022'},
		{'name': 'Мой второй блог', 'author': {'name': 'admin'}, 'publication_date': '17.04.2022'},
		{'name': 'Мой третий блог', 'author': {'name': 'admin'}, 'publication_date': '18.04.2022'},	
	]
	context = {
		'blogs': blogs,
	}
	return render(request, 'blogs/index.html', context)

def user_page(request):
	# как передовать переменные
	user_data = {
		'user_name': 'Mirlan',
		'user_age': 17,
	}
	context = {
		'user_data': user_data,
	}
	return render(request, 'blogs/user.html', context)

def friend_page(request):
	# как передовать переменные
	friend_data = {
		'friend_name': 'Rasim',
		'friend_age': 17
	}
	context = {
		'friend_data': friend_data,
	}
	return render(request, 'blogs/friend.html', context)

def first_page(request):
<<<<<<< HEAD
	return render(request, 'blogs/first_page.html')

def piramyda_page(request):
	return render(request, 'blogs/piramyda.html')

def kolizey_page(request):
	return render(request, 'blogs/kolizey.html')

def ploshad_page(request):
	return render(request, 'blogs/ploshad.html')

def efeleva_page(request):
	return render(request, 'blogs/efeleva.html')

def reykhstag_page(request):
	return render(request, 'blogs/reykhstag.html')

def petergov_page(request):
	return render(request, 'blogs/petergov.html')

def luvr_page(request):
	return render(request, 'blogs/luvr.html')

def kreml_page(request):
	return render(request, 'blogs/kreml.html')


# Вторая страница
def second_page(request):
	return render(request, 'blogs/second.html')

def khram_page(request):
	return render(request, 'blogs/khram.html')

def tadzh_makhal_page(request):
	return render(request, 'blogs/tadzh_makhal.html')

def big_ben_page(request):
	return render(request, 'blogs/big_ben.html')

def statuya_page(request):
	return render(request, 'blogs/statuya.html')

def machu_pikchu_page(request):
	return render(request, 'blogs/machu_pikchu.html')

def fort_boyard_page(request):
	return render(request, 'blogs/fort_boyard.html')

def notr_dam_page(request):
	return render(request, 'blogs/notr_dam.html')

def kitayskaya_stena_page(request):
	return render(request, 'blogs/kitayskaya_stena.html')


# Третья страница
def third_page(request):
	return render(request, 'blogs/third.html')




# Четвертая страница
def fourth_page(request):
	return render(request, 'blogs/fourth.html')

=======
	first_data = {
		'first_name': 'Mirlan',
	}
	context = {
		'first_data': first_data,
	}
	return render(request, 'blogs/first_page.html', context)

def piramyda_page(request):
	piramyda_data = {
		'piramyda_name': 'Mika',
	}
	context = {
		'piramyda_data': piramyda_data,
	}
	return render(request, 'blogs/piramyda.html', context)

def kolizey_page(request):
	kolizey_data = {
		'kolizey_name': 'Mika',
	}
	context = {
		'kolizey_data': kolizey_data,
	}
	return render(request, 'blogs/kolizey.html', context)

def ploshad_page(request):
	ploshad_data = {
		'ploshad_name': 'Mika',
	}
	context = {
		'ploshad_data': ploshad_data,
	}
	return render(request, 'blogs/ploshad.html', context)

def efeleva_page(request):
	efeleva_data = {
		'efeleva_name': 'Mika',
	}
	context = {
		'efeleva_data': efeleva_data,
	}
	return render(request, 'blogs/efeleva.html', context)

def reykhstag_page(request):
	reykhstag_data = {
		'reykhstag_name': 'Mika',
	}
	context = {
		'reykhstag_data': reykhstag_data,
	}
	return render(request, 'blogs/reykhstag.html', context)

def petergov_page(request):
	petergov_data = {
		'petergov_name': 'Mika',
	}
	context = {
		'petergov_data': petergov_data,
	}
	return render(request, 'blogs/petergov.html', context)

def luvr_page(request):
	luvr_data = {
		'luvr_name': 'Mika',
	}
	context = {
		'luvr_data': luvr_data,
	}
	return render(request, 'blogs/luvr.html', context)

def kreml_page(request):
	kreml_data = {
		'kreml_name': 'Mika',
	}
	context = {
		'kreml_data': kreml_data,
	}
	return render(request, 'blogs/kreml.html', context)
>>>>>>> 54e7d8fd22b43bf5e8f31c1208bf24ad93721ef2
