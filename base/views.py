from django.contrib.auth.models import User
from django.db.models.query_utils import select_related_descend
from .models import Task
from django.db.models.base import Model
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView 
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin

#Pour faire l'inscription d'un utilisateur on import les 3 lignes en-dessous
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, UsernameField 
from django.contrib.auth import login
from django.http import request



# Create your views here.



class CustomLoginView(LoginView):
    template_name='base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        if User.username == "mme.janah":
            print(User.username)
        return reverse_lazy('tasks')


class RegisterPage(FormView):
    template_name='base/register.html'
    form_class = UserCreationForm #permet a'afficher formulaire
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('tasks')

        
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterPage,self).form_valid(form)

    def get(self,*args,**kwargs): #si user est connecté on l'empêche d'acceder à la page login
         if self.request.user.is_authenticated:
             return redirect('tasks')
         return super(RegisterPage,self).get(*args,**kwargs)



class TaskList(LoginRequiredMixin,ListView):
   model =Task
   context_object_name = 'liste' #pour changer ' object_list' qui affiche les data dans la page HTML, par notre propre attribut
   def get_context_data(self, **kwargs): # methode qui permet de afficher les taches d'user connecté (pas tous les taches des autre user)
       context = super().get_context_data(**kwargs)
       context['liste'] = context['liste'].filter(user = self.request.user)
       context['count'] = context['liste'].filter(check = False).count() # ramene les taches non cochés

       search_input = self.request.GET.get('search-area') or '' #recuperer le nom du champ html 
       if search_input:
           context['liste']=context['liste'].filter(systeme__startswith = search_input) #si on tape ->afficher les sys qui commancent par...

       context['search_input']=search_input  #si on cherche rien ->affiche la liste
       return context


class TaskGolabl(LoginRequiredMixin,ListView):
   model =Task
   context_object_name = 'listeG' #pour changer ' object_list' qui affiche les data dans la page HTML, par notre propre attribut
   template_name='base/accueil.html'
   def get_context_data(self, **kwargs): # methode qui permet de afficher les taches d'user connecté (pas tous les taches des autre user)
       context = super().get_context_data(**kwargs)
      # context['liste'] = context['liste'].filter(user = self.request.user)
       context['count'] = context['listeG'].filter(check = False).count() # ramene les taches non cochés

      # search_input = self.request.GET.get('search-area') or '' #recuperer le nom du champ html 
       search_drop = self.request.GET.get('search-drop')

       if search_drop:
           #context['listeG']=context['listeG'].filter(user__username= search_input) #si on tape ->afficher les sys qui commancent par...
           context['listeG']=context['listeG'].filter(user__username= search_drop)
      # context['search_input']=search_input  #si on cherche rien ->affiche la liste
       context['search_input']=search_drop
       return context
    



class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'detail'
    template_name='base/detail.html'  #pour que django prend en compte le nom fichier html


class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    fields=['systeme','service','check','action','remarque']
    success_url=reverse_lazy('create')

    def form_valid(self, form):   #pour que l user ajout des taches lié à lui même ,sans avoir la possibilté de choisir d'autre user
        form.instance.user = self.request.user
        return super(TaskCreate,self).form_valid(form)



class TaskUpadte(LoginRequiredMixin,UpdateView):
    model = Task
    fields=['systeme','service','check','action','remarque']
    success_url=reverse_lazy('tasks') # pour me rediriger à la page d'accueil 'tasks' et le nom d'url taskslist



class TaskDelete(LoginRequiredMixin,DeleteView): #LoginRequiredMixin : si user n'est pas connecté on le redirect vers page login,n'oublier pas d'ajouter dans settings.py : LOGIN_URL = 'login'
    model = Task
    context_object_name = 'liste'
    success_url=reverse_lazy('tasks')


